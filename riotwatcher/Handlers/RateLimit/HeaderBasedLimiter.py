
from datetime import datetime

from .. import RequestHandler


class HeaderBasedLimiter(RequestHandler):
    def __init__(self, limit_header, count_header, friendly_name=None):
        self._limit_header = limit_header
        self._count_header = count_header
        self._friendly_name = friendly_name

    @property
    def friendly_name(self):
        return self._friendly_name

    def preview_request(self, region, endpoint_name, method_name, url, query_params):
        """
        called before a request is processed.

        :param string region: the region of this request
        :param string endpoint_name: the name of the endpoint being requested
        :param string method_name: the name of the method being requested
        :param url: the URL that is being requested.
        :param query_params: dict: the parameters to the url that is being queried, e.g. ?key1=val&key2=val2

        :returns datetime: the time at which the next request can be made
        """
        pass

    def after_request(self, region, endpoint_name, method_name, url, response):
        """
        Called after a response is received and before it is returned to the user.

        :param string region: the region of this request
        :param string endpoint_name: the name of the endpoint that was requested
        :param string method_name: the name of the method that was requested
        :param url: The url that was requested
        :param response: the response received. This is a response from the Requests library
        """
        pass
