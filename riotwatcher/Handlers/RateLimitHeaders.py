
import datetime

from . import LimitCount


class RateLimitHeaders(object):
    """
    The RateLimitHeaders class contains all information that the Riot API returns regarding rate limiting.
    """
    def __init__(self, headers, last_headers=None):
        """
        Creates a new RateLimitHeaders object by parsing the HTTP headers provided
        :param headers: dict of HTTP headers from a request to the Riot API
        :param last_headers: previous RateLimitHeaders object, used to determine
            what the actual start time of each rate limit is
        """
        self._time = datetime.datetime.now()

        self._rate_limit_type = headers.get('X-Rate-Limit-Type')

        retry_after = headers.get('Retry-After')
        self._retry_after = int(retry_after) if retry_after is not None else None

        self._app_rate_limit = None
        app_lim = headers.get('X-App-Rate-Limit')

        if app_lim is not None:
            limit_strings = app_lim.split(',')
            self._app_rate_limit = [LimitCount(lim_str) for lim_str in limit_strings]

        self._app_rate_limit_count = None
        app_lim_count = headers.get('X-App-Rate-Limit-Count')

        if app_lim_count is not None:
            limit_strings = app_lim_count.split(',')
            if last_headers is not None and last_headers.app_rate_limit_count is not None:
                strings_with_old_limits = zip(limit_strings, last_headers.app_rate_limit_count)

                self._app_rate_limit_count = [
                    LimitCount(lim_str, last_limit=old_limit) for lim_str, old_limit in strings_with_old_limits
                ]
            else:
                self._app_rate_limit_count = [LimitCount(lim_str) for lim_str in limit_strings]

        self._method_rate_limit = None
        method_lim = headers.get('X-Method-Rate-Limit')

        if method_lim is not None:
            limit_strings = method_lim.split(',')
            self._method_rate_limit = [LimitCount(lim_str) for lim_str in limit_strings]

        self._method_rate_limit_count = None
        method_lim_count = headers.get('X-Method-Rate-Limit-Count')

        if method_lim_count is not None:
            method_limit_strings = method_lim_count.split(',')
            if last_headers is not None and last_headers.method_rate_limit_count is not None:
                strings_with_old_limits = zip(method_limit_strings, last_headers.method_rate_limit_count)

                self._method_rate_limit_count = [
                    LimitCount(lim_str, last_limit=old_limit)
                    for lim_str, old_limit in strings_with_old_limits
                ]
            else:
                self._method_rate_limit_count = [LimitCount(lim_str) for lim_str in method_limit_strings]

    @property
    def time(self):
        """
        The time that this RateLimitHeaders instance was created. This should be used
        to tell how much time there is until you can make another request.

        :return datetime the time the last header was created
        """
        return self._time

    @property
    def rate_limit_type(self):
        """
        The rate limit type, either "method", "service", or "application".

        Included in any 429 response. "method" indicates you have exceeded the individual limits for that method.
        "application" indicates you have exceeded the total rate limit for your application.
        "service" is returned if the underlying platform service is rate limiting it's connections from the Riot API
        layer, regardless of your own personal ratelimits.
        :return string indicating which type of rate limit is being enforced, or None if there was no limit
        """
        return self._rate_limit_type

    @property
    def retry_after(self):
        """
        The remaining number of seconds before the rate limit resets. Applies to both user and service rate limits.

        Included in any 429 response where the rate limit was enforced by the API infrastructure.
        Not included in any 429 response where the rate limit was enforced by the underlying service to which the
        request was proxied.
        :return: int if this header was included, else None
        """
        return self._retry_after

    @property
    def app_rate_limit(self):
        return self._app_rate_limit

    @property
    def app_rate_limit_count(self):
        """
        The number of calls that have been made during a specific rate limit. See LimitCount for more information.

        Included in the response for all API calls that enforce an application rate limit.
        :return: list of LimitCount objects, or None if service is not rate limited
        """
        return self._app_rate_limit_count

    @property
    def method_rate_limit(self):
        return self._method_rate_limit

    @property
    def method_rate_limit_count(self):
        """
        The number of calls to a specific method that have been made during a specific rate limit.

        Included in the response for all API calls that enforce a method rate limit.
        :return: list of LimitCount objects, or None if method is not rate limited
        """
        return self._method_rate_limit_count
