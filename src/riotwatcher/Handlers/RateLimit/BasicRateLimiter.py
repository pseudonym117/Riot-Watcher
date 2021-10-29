import datetime
import logging

from typing import Dict, Optional, Tuple

from ...RateLimiter import RateLimiter

from . import (
    ApplicationRateLimiter,
    MethodRateLimiter,
    OopsRateLimiter,
    InternalLimiter,
)

LOG = logging.getLogger(__name__)


class BasicRateLimiter(RateLimiter):
    __application_rate_limiter = ApplicationRateLimiter()

    def __init__(self):
        super().__init__()

        self._limiters: Tuple[InternalLimiter, InternalLimiter, InternalLimiter] = (
            BasicRateLimiter.__application_rate_limiter,
            MethodRateLimiter(),
            OopsRateLimiter(),
        )

    def wait_until(
        self, region: str, endpoint_name: str, method_name: str,
    ) -> Optional[datetime.datetime]:
        wait_until = max(
            [
                (
                    limiter.wait_until(region, endpoint_name, method_name),
                    limiter.friendly_name,
                )
                for limiter in self._limiters
            ],
            key=lambda lim_pair: lim_pair[0]
            if lim_pair[0]
            else datetime.datetime(datetime.MINYEAR, 1, 1),
        )

        if wait_until[0] is not None and wait_until[0] > datetime.datetime.now():
            to_wait = wait_until[0] - datetime.datetime.now()

            LOG.debug(
                "waiting for %s seconds due to %s limit...",
                to_wait.total_seconds(),
                wait_until[1],
            )
            return wait_until[0]
        return None

    def record_response(
        self,
        region: str,
        endpoint_name: str,
        method_name: str,
        status: int,
        headers: Dict[str, str],
    ):
        for limiter in self._limiters:
            limiter.update_limiter(
                region, endpoint_name, method_name, status, headers,
            )
