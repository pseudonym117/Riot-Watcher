from abc import ABC, abstractmethod
from contextlib import asynccontextmanager, contextmanager
from datetime import datetime, timedelta
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple
import time
import asyncio
import threading


# todo: make this safe for python 3.6... maybe


@dataclass
class RateLimitData:
    name: str
    window_start: datetime
    window_duration: timedelta
    limit: int
    used_requests: int
    pending_requests: int

    def allow_next_request_at(self) -> Optional[datetime]:
        now = datetime.now()
        if now > self.window_start + self.window_duration:
            return None
        if self.used_requests + self.pending_requests < self.limit:
            return None
        return self.window_start + self.window_duration


class RateLimitedError(Exception):
    def __init__(self, limit_name: str, retry_at: datetime):
        self.limit_name = limit_name
        self.retry_at = retry_at

    @property
    def sleep_for(self) -> timedelta:
        return self.retry_at - datetime.now()

    def wait(self):
        sleep_for = self.sleep_for.total_seconds()
        time.sleep(sleep_for)

    async def wait_async(self):
        sleep_for = self.sleep_for.total_seconds()
        await asyncio.sleep(sleep_for)


class RateLimitStorage(ABC):
    @abstractmethod
    def is_initialized(self, permit: str) -> bool:
        raise NotImplementedError()

    @abstractmethod
    @contextmanager
    def get_permits_or_throw(self, *permits: str):
        raise NotImplementedError()

    @abstractmethod
    @asynccontextmanager
    async def get_permits_or_throw_async(self, *permits: str):
        raise NotImplementedError()

    @abstractmethod
    def set_limit_info(
        self,
        permit_name: str,
        limit: int,
        window_duration: timedelta,
        window_start: datetime = datetime.now(),
        used_requests: int = 0,
        pending_requests: int = 0,
    ):
        raise NotImplementedError()

    @abstractmethod
    async def set_limit_info_async(
        self,
        permit_name: str,
        limit: int,
        window_duration: timedelta,
        window_start: datetime = datetime.now(),
        used_requests: int = 0,
        pending_requests: int = 0,
    ):
        raise NotImplementedError()


class LocalMemoryRateLimitStorate(RateLimitStorage):
    def __init__(self):
        self._permits: Dict[str, RateLimitData] = {}
        self._permits_lock = threading.Lock()
        self._async_permits_lock = asyncio.Lock()

    def is_initialized(self, permit: str) -> bool:
        return permit in self._permits

    def set_limit_info(
        self,
        permit_name: str,
        limit: int,
        window_duration: timedelta,
        window_start: datetime = datetime.now(),
        used_requests: int = 0,
        pending_requests: int = 0,
    ):
        with self._permits_lock:
            self._set_limit_info_no_lock(
                permit_name,
                limit,
                window_duration,
                window_start,
                used_requests,
                pending_requests,
            )

    async def set_limit_info_async(
        self,
        permit_name: str,
        limit: int,
        window_duration: timedelta,
        window_start: datetime = datetime.now(),
        used_requests: int = 0,
        pending_requests: int = 0,
    ):
        async with self._async_permits_lock:
            self._set_limit_info_no_lock(
                permit_name,
                limit,
                window_duration,
                window_start,
                used_requests,
                pending_requests,
            )

    def _set_limit_info_no_lock(
        self,
        permit_name: str,
        limit: int,
        window_duration: timedelta,
        window_start: datetime,
        used_requests: int,
        pending_requests: int,
    ):
        self._permits[permit_name] = RateLimitData(
            permit_name,
            window_start=window_start,
            window_duration=window_duration,
            limit=limit,
            used_requests=used_requests,
            pending_requests=pending_requests,
        )

    @contextmanager
    def get_permits_or_throw(self, *permits: str):
        with self._permits_lock:
            self._start_get_permits_no_lock(*permits)
        yield
        with self._permits_lock:
            self._end_get_permits_no_lock(*permits)

    @asynccontextmanager
    async def get_permits_or_throw_async(self, *permits: str):
        async with self._async_permits_lock:
            self._start_get_permits_no_lock(*permits)
        yield
        async with self._async_permits_lock:
            self._end_get_permits_no_lock(*permits)

    def _start_get_permits_no_lock(self, *permits: str):
        next_times: List[Tuple[str, datetime]] = []
        for permit_name in permits:
            # todo: handle first requests
            permit = self._permits[permit_name]
            next_at = permit.allow_next_request_at()
            if next_at is not None:
                next_times.append((permit_name, next_at,))
        if next_times:
            retry_at = max(next_times, key=lambda tuple: tuple[1])
            raise RateLimitedError(*retry_at)
        for permit_name in permits:
            self._permits[permit_name].pending_requests += 1

    def _end_get_permits_no_lock(self, *permits: str):
        for permit_name in permits:
            permit = self._permits[permit_name]
            permit.pending_requests -= 1

            now = datetime.now()
            while now > permit.window_start + permit.window_duration:
                # todo: this is likely a bad place to restart the window
                permit.window_start = permit.window_start + permit.window_duration
                permit.used_requests = 0

            permit.used_requests += 1


class RateLimitedStrategy(ABC):
    @abstractmethod
    def handle_rate_limited(self, error: RateLimitedError):
        raise NotImplementedError()

    @abstractmethod
    async def handle_rate_limited_async(self, error: RateLimitedError):
        raise NotImplementedError()


class SleepingRateLimitedStrategy(RateLimitedStrategy):
    def handle_rate_limited(self, error: RateLimitedError):
        error.wait()

    async def handle_rate_limited_async(self, error: RateLimitedError):
        await error.wait_async()


class RateLimiter:
    def __init__(
        self, storage: RateLimitStorage, rate_limited_strategy: RateLimitedStrategy
    ):
        self._storage = storage
        self._rate_limited_strategy = rate_limited_strategy

    @contextmanager
    def get_token(self, *permits: str):
        while True:
            try:
                with self._storage.get_permits_or_throw(*permits):
                    yield
            except RateLimitedError as e:
                self._rate_limited_strategy.handle_rate_limited(e)

    @asynccontextmanager
    async def get_token_async(self, *permits: str):
        while True:
            try:
                async with self._storage.get_permits_or_throw_async(*permits):
                    yield
            except RateLimitedError as e:
                await self._rate_limited_strategy.handle_rate_limited_async(e)
