import datetime
import logging
import threading

from collections import namedtuple
from typing import Iterable, Optional


log = logging.getLogger(__name__)

RawLimit = namedtuple("RawLimit", ["count", "limit", "time"])


class LimitCollection:
    def __init__(self):
        self._limits = {}
        self._limits_lock = threading.Lock()

    def wait_until(self) -> datetime.datetime:
        # we dont really want to update the limits as we process them
        # may be able to move the max() call outside the lock though
        with self._limits_lock:
            limits_waits = [limit.wait_until() for key, limit in self._limits.items()]
            return max(limits_waits) if limits_waits else None

    def update_limits(self, raw_limits: Iterable[RawLimit]):
        for raw_limit in raw_limits:
            if raw_limit.time not in self._limits:
                with self._limits_lock:
                    # check again in case it has already been added
                    if raw_limit.time not in self._limits:
                        self._limits[raw_limit.time] = Limit()
            self._limits[raw_limit.time].set_raw_limit(raw_limit)


class Limit:
    def __init__(self):
        self._start_time = None
        self._raw_limit = RawLimit(0, 0, 0)

        self._lock = threading.Lock()

    @property
    def start_time(self) -> Optional[datetime.datetime]:
        return self._start_time

    @property
    def duration(self) -> int:
        return self._raw_limit.time

    @property
    def count(self) -> int:
        return self._raw_limit.count

    @property
    def limit(self) -> int:
        return self._raw_limit.limit

    def set_raw_limit(self, raw_limit: RawLimit):
        enter_time = datetime.datetime.now()

        # try to ensure some thread safety
        with self._lock:
            reset_timer = False

            # if the time increment changed, we dont really know anything anymore
            # and should reset our timer
            if self._raw_limit.time != raw_limit.time:
                reset_timer = True
                if not (
                    self._raw_limit.time == 0
                    and self._raw_limit.limit == 0
                    and self._raw_limit.count == 0
                ):
                    log.warning(
                        "overwriting time limit, previously %s, now %s. This may cause rate limitting issues.",
                        self._raw_limit.time,
                        raw_limit.time,
                    )

            if self._raw_limit.limit != raw_limit.limit:
                log.info(
                    "rate limit changed from %s/%ss to %s/%ss",
                    self._raw_limit.limit,
                    self._raw_limit.time,
                    raw_limit.limit,
                    raw_limit.time,
                )

            # if the count is 1, that means we should reset our timers
            if raw_limit.count == 1:
                reset_timer = True

            if reset_timer:
                self._raw_limit = raw_limit
                self._start_time = enter_time
            else:
                # double check that we arent assigning a lower, non-1 value to
                # our count. This may be screwy if a bunch of requests are sent
                # as the rate limit is getting reset, but I dont think there
                # is a more elegant solution.
                if self._raw_limit.count > raw_limit.count:
                    raw_limit = RawLimit(
                        self._raw_limit.count, raw_limit.limit, raw_limit.time
                    )
                self._raw_limit = raw_limit

    def wait_until(self) -> datetime.datetime:
        if self.count >= self.limit:
            return self._start_time + datetime.timedelta(seconds=self.duration)
        return datetime.datetime(datetime.MINYEAR, 1, 1)
