
import datetime


class LimitCount:
    """
    The LimitCount class contains how many requests have been made in a specified time period,
    as well as how long that time period is.
    It does NOT contain the actual limit for number of requests that can be made in that time period,
    just the number of requests that HAVE been made in that time period
    """

    def __init__(self, str_rep):
        """
        Creates a new LimitCount object from a string formatted the way Riot's API returns Limit information
        :param str_rep: string in format "<calls>:<time>"
        """
        nums = str_rep.split(':')

        self._calls = int(nums[0])

        seconds = int(nums[1])
        self._time = datetime.time(second=seconds)

    @property
    def calls(self):
        """the number of calls that have been made in the specified time period"""
        return self._calls

    @property
    def time(self):
        """the time period that this Limit is over. Is a datetime.time object."""
        return self._time


class RateLimitHeaders:
    """
    The RateLimitHeaders class contains all information that the Riot API returns regarding rate limiting.
    """
    def __init__(self, headers):
        """
        Creates a new RateLimitHeaders object by parsing the HTTP headers provided
        :param headers: dict of HTTP headers from a request to the Riot API
        """
        self._rate_limit_type = headers['X-Rate-Limit-Type']

        retry_after = headers['Retry-After']
        self._retry_after = int(retry_after) if retry_after is not None else None

        app_lim = headers['X-App-Rate-Limit-Count']

        self._app_rate_limit_count = [LimitCount(lim) for lim in app_lim.split(',')] if app_lim is not None else None

        method_lim = headers['X-Method-Rate-Limit-Count']
        self._method_rate_limit_count = [LimitCount(lim) for lim in method_lim.split(',')] if method_lim is not None else None

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
    def app_rate_limit_count(self):
        """
        The number of calls that have been made during a specific rate limit. See LimitCount for more information.
        
        Included in the response for all API calls that enforce an application rate limit.
        :return: list of LimitCount objects, or None if service is not rate limited
        """
        return self._app_rate_limit_count

    @property
    def method_rate_limit_count(self):
        """
        The number of calls to a specific method that have been made during a specific rate limit.
        
        Included in the response for all API calls that enforce a method rate limit.
        :return: list of LimitCount objects, or None if method is not rate limited
        """
        return self._method_rate_limit_count

