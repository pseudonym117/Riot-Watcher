import datetime
import logging


class OopsRateLimiter(object):
    def __init__(self):
        self._friendly_name = "429_Limit"
        self._retry_at = None

    @property
    def friendly_name(self):
        return self._friendly_name

    def wait_until(self, region, endpoint_name, method_name):
        if self._retry_at is not None:
            if self._retry_at > datetime.datetime.now():
                return self._retry_at
            self._retry_at = None
        return datetime.datetime(datetime.MINYEAR, 1, 1)

    def update_limiter(self, region, endpoint_name, method_name, response):
        if response.status_code == 429:
            retry_after = response.headers.get("Retry-After")
            limit_type = response.headers.get("X-Rate-Limit-Type")

            if retry_after is not None:
                logging.info(
                    'hit 429 from "%s" limit! retrying after %s seconds',
                    limit_type,
                    retry_after,
                )
                self._retry_at = datetime.datetime.now() + datetime.timedelta(
                    seconds=int(retry_after)
                )
            else:
                logging.info(
                    'hit 429 from "%s" limit! no retry after header...', limit_type
                )
