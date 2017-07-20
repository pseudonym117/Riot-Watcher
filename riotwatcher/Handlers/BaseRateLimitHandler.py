
from . import RequestHandler
from . import RateLimitHeaders


class BaseRateLimitHandler(RequestHandler):
    """
    The BaseRateLimitHandler class is meant to be extended in order to provide more sophisticated rate limiting
    functionality. This class only provides the necessary preview and after request functions which should
    be overwritten by more complex RateLimitHandlers.

    This class does keep track of the last header that has been received, and stores this in the last_rate_headers
    property, so that this can be inspected when desired.
    """

    def __init__(self):
        """Initializes the BaseRateLimitHandler class"""
        super(BaseRateLimitHandler, self).__init__()
        self._last_rate_headers = None
        self._app_rate_limit_start_times = None
        self._app_limits = None

    @property
    def app_limits(self):
        return self._app_limits

    @property
    def last_rate_headers(self):
        """
        Contains the last RateLimitHeaders that have been received. These are not stored for static method calls.
        :return: RateLimitHeaders object for the last request processed.
        """
        return self._last_rate_headers

    @property
    def app_rate_limit_start_times(self):
        """
        Contains the start time of the current app rate limits (roughly). Cannot be
        absolutely sure of these, as only Riot has that information
        :return list of datetime objects
        """
        return self._app_rate_limit_start_times

    def preview_request(self, endpoint_name, method_name, url, query_params):
        """
        called before a request is processed.

        :param string endpoint_name: the name of the endpoint being requested
        :param string method_name: the name of the method being requested
        :param url: the URL that is being requested.
        :param query_params: dict: the parameters to the url that is being queried, e.g. ?key1=val&key2=val2
        """
        super(BaseRateLimitHandler, self).preview_request(endpoint_name, method_name, url, query_params)

    def after_request(self, endpoint_name, method_name, url, response):
        """
        Called after a response is received and before it is returned to the user.

        :param string endpoint_name: the name of the endpoint that was requested
        :param string method_name: the name of the method that was requested
        :param url: The url that was requested
        :param response: the response received. This is a response from the Requests library
        """
        super(BaseRateLimitHandler, self).after_request(endpoint_name, method_name, url, response)

        headers = RateLimitHeaders(response.headers, self.last_rate_headers)

        if headers.app_rate_limit_count is not None or headers.method_rate_limit_count is not None:
            self._last_rate_headers = headers

        if headers.app_rate_limit is not None:
            self._app_limits = headers.app_rate_limit
