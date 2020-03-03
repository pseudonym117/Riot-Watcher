import datetime
import logging

from typing import Dict

log = logging.getLogger(__name__)


class OopsRateLimiter:
    def __init__(self):
        self._friendly_name = "429_Limit"
        self._retry_at = None

    @property
    def friendly_name(self) -> str:
        return self._friendly_name

    def wait_until(self, region: str, endpoint_name: str, method_name: str) -> datetime:
        if self._retry_at is not None:
            if self._retry_at > datetime.datetime.now():
                return self._retry_at
            self._retry_at = None
        return datetime.datetime(datetime.MINYEAR, 1, 1)

    def update_limiter(
        self,
        region: str,
        endpoint_name: str,
        method_name: str,
        status: int,
        headers: Dict[str, str],
    ):
        if status == 429:
            retry_after = headers.get("Retry-After")
            limit_type = headers.get("X-Rate-Limit-Type")

            if retry_after is not None:
                log.info(
                    'hit 429 from "%s" limit! retrying after %s seconds',
                    limit_type,
                    retry_after,
                )
                self._retry_at = datetime.datetime.now() + datetime.timedelta(
                    seconds=int(retry_after)
                )
            else:
                log.info(
                    'hit 429 from "%s" limit! no retry after header...', limit_type
                )
