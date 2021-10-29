import datetime
import logging
import threading

from typing import Dict, List, Optional

from .InternalLimiter import InternalLimiter
from .Limits import LimitCollection, RawLimit

LOG = logging.getLogger(__name__)


class HeaderBasedLimiter(InternalLimiter):
    def __init__(self, limit_header: str, count_header: str, friendly_name: str = None):
        super().__init__()
        self._limit_header = limit_header
        self._count_header = count_header
        self._friendly_name = friendly_name

        self._limits: Dict[str, LimitCollection] = {}
        self._limits_lock = threading.Lock()

    @property
    def friendly_name(self) -> str:
        return self._friendly_name

    def _get_limit_scope(
        self, region: str, endpoint_name: str, method_name: str
    ) -> str:
        return ""

    def __get_limit(
        self, region: str, endpoint_name: str, method_name: str
    ) -> LimitCollection:
        scope = self._get_limit_scope(region, endpoint_name, method_name)

        if scope not in self._limits:
            with self._limits_lock:
                # double check this hasnt been added by another thread already
                if scope not in self._limits:
                    self._limits[scope] = LimitCollection()
                return self._limits[scope]

        return self._limits[scope]

    def wait_until(
        self, region: str, endpoint_name: str, method_name: str
    ) -> datetime.datetime:
        scoped_limit = self.__get_limit(region, endpoint_name, method_name)

        return scoped_limit.wait_until()

    def update_limiter(
        self,
        region: str,
        endpoint_name: str,
        method_name: str,
        status: int,
        headers: Dict[str, str],
    ):
        raw_limits = self._extract_headers(headers)

        if raw_limits is None:
            return

        scoped_limit = self.__get_limit(region, endpoint_name, method_name)

        scoped_limit.update_limits(raw_limits)

    def _extract_headers(self, headers: Dict[str, str]) -> Optional[List[RawLimit]]:
        limits = HeaderBasedLimiter._extract_single_header(self._limit_header, headers)
        counts = HeaderBasedLimiter._extract_single_header(self._count_header, headers)

        if limits is None or counts is None:
            return None

        if len(limits) != len(counts):
            LOG.warning(
                'header "%s" and "%s" have different sizes!',
                self._limit_header,
                self._count_header,
            )

        combined_limits = list(zip(counts, limits))

        for limit in combined_limits:
            if limit[0][1] != limit[1][1]:
                LOG.warning(
                    " ".join(
                        [
                            'seems that limits for headers "%s" and "%s" did not match',
                            "up correctly! There may be issues in rate limiting.",
                            'Headers were: "%s", "%s".',
                            'Limits from "%s" will be used.',
                        ]
                    ),
                    self._limit_header,
                    self._count_header,
                    headers.get(self._limit_header),
                    headers.get(self._count_header),
                    self._limit_header,
                )

        values = [
            RawLimit(count=limit[0][0], limit=limit[1][0], time=limit[0][1])
            for limit in combined_limits
        ]

        return values

    @staticmethod
    def _extract_single_header(
        header: str, headers: Dict[str, str]
    ) -> Optional[List[List[int]]]:
        values = headers.get(header)

        if values is None:
            return None

        values = values.split(",")

        values = [[int(val) for val in value.split(":")] for value in values]

        return values
