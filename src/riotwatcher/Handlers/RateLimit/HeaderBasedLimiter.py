import logging
import threading

from .Limits import LimitCollection, RawLimit


class HeaderBasedLimiter(object):
    def __init__(self, limit_header, count_header, friendly_name=None):
        self._limit_header = limit_header
        self._count_header = count_header
        self._friendly_name = friendly_name

        self._limits = {}
        self._limits_lock = threading.Lock()

    @property
    def friendly_name(self):
        return self._friendly_name

    def _get_limit_scope(self, region, endpoint_name, method_name):
        return ""

    def __get_limit(self, region, endpoint_name, method_name):
        scope = self._get_limit_scope(region, endpoint_name, method_name)

        if scope not in self._limits:
            with self._limits_lock:
                # double check this hasnt been added by another thread already
                if scope not in self._limits:
                    self._limits[scope] = LimitCollection()
                return self._limits[scope]

        return self._limits[scope]

    def wait_until(self, region, endpoint_name, method_name):
        scoped_limit = self.__get_limit(region, endpoint_name, method_name)

        return scoped_limit.wait_until()

    def update_limiter(self, region, endpoint_name, method_name, response):
        raw_limits = self._extract_headers(response)

        if raw_limits is None:
            return

        scoped_limit = self.__get_limit(region, endpoint_name, method_name)

        scoped_limit.update_limits(raw_limits)

    def _extract_headers(self, response):
        limits = HeaderBasedLimiter._extract_single_header(self._limit_header, response)
        counts = HeaderBasedLimiter._extract_single_header(self._count_header, response)

        if limits is None or counts is None:
            return None

        if len(limits) != len(counts):
            logging.warning(
                'header "%s" and "%s" have different sizes!',
                self._limit_header,
                self._count_header,
            )

        combined_limits = list(zip(counts, limits))

        for limit in combined_limits:
            if limit[0][1] != limit[1][1]:
                logging.warning(
                    'seems that limits for headers "%s" and "%s" did not match up correctly! '
                    + 'There may be issues in rate limiting. Headers were: "%s", "%s"'
                    + 'Limits from "%s" will be used.',
                    self._limit_header,
                    self._count_header,
                    response.headers.get(self._limit_header),
                    response.headers.get(self._count_header),
                    self._limit_header,
                )

        values = [
            RawLimit(count=limit[0][0], limit=limit[1][0], time=limit[0][1])
            for limit in combined_limits
        ]

        return values

    @staticmethod
    def _extract_single_header(header, response):
        values = response.headers.get(header)

        if values is None:
            return None

        values = values.split(",")

        values = [[int(val) for val in value.split(":")] for value in values]

        return values
