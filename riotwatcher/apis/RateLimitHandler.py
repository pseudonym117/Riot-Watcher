
from RateLimitHeaders import RateLimitHeaders


class RequestHandler:
    def __init__(self):
        pass

    def preview_request(self, url):
        """
        called before a request is processed.
        :param url: the URL that is being requested.
        """
        pass

    def after_request(self, url, response):
        """
        Called after a response is received and before it is returned to the user.
        :param url: The url that was requested
        :param response: the response received. This is a response from the Requests library
        """
        pass


class RateLimitHandler(RequestHandler):
    """
    The RateLimitHandler class is meant to be extended in order to provide more sophisticated rate limiting
    functionality. This class only provides the necessary preview and after request functions which should
    be overwritten by more complex RateLimitHandlers.
    
    This class does keep track of the last header that has been received, and stores this in the last_rate_headers
    property, so that this can be inspected when desired.
    """

    def __init__(self):
        """Initializes the RateLimitHandler class"""
        super(RateLimitHandler, self).__init__()
        self._last_rate_headers = None

    @property
    def last_rate_headers(self):
        """
        Contains the last RateLimitHeaders that have been received. These are not stored for static method calls.
        :return: RateLimitHeaders object for the last request processed.
        """
        return self._last_rate_headers

    def preview_request(self, url):
        """
        called before a request is processed.
        :param url: the URL that is being requested.
        """
        super(RateLimitHandler, self).preview_request(url)

    def after_request(self, url, response):
        """
        Called after a response is received and before it is returned to the user.
        :param url: The url that was requested
        :param response: the response received. This is a response from the Requests library
        """
        super(RateLimitHandler, self).after_request(url, response)

        headers = RateLimitHeaders(response.headers)

        if headers.app_rate_limit_count is not None or headers.method_rate_limit_count is not None:
            self._last_rate_headers = RateLimitHeaders(response.headers)
