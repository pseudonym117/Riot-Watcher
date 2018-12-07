import datetime
import logging
import time

from .. import RequestHandler

from . import ApplicationRateLimiter, MethodRateLimiter, OopsRateLimiter


class RateLimitHandler(RequestHandler):
    def __init__(self):
        super(RateLimitHandler, self).__init__()

        self._limiters = (
            ApplicationRateLimiter(),
            MethodRateLimiter(),
            OopsRateLimiter(),
        )

    def preview_request(self, region, endpoint_name, method_name, url, query_params):
        """
        called before a request is processed.

        :param string region: the region of this request
        :param string endpoint_name: the name of the endpoint being requested
        :param string method_name: the name of the method being requested
        :param url: the URL that is being requested.
        :param query_params: dict: the parameters to the url that is being queried,
                                   e.g. ?key1=val&key2=val2
        """
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

            logging.info(
                "waiting for %s seconds due to %s limit...",
                to_wait.total_seconds(),
                wait_until[1],
            )
            time.sleep(to_wait.total_seconds())

    def after_request(self, region, endpoint_name, method_name, url, response):
        """
        Called after a response is received and before it is returned to the user.

        :param string region: the region of this request
        :param string endpoint_name: the name of the endpoint that was requested
        :param string method_name: the name of the method that was requested
        :param url: The url that was requested
        :param response: the response received. This is a response from the Requests library
        """
        for limiter in self._limiters:
            limiter.update_limiter(region, endpoint_name, method_name, response)

        return response
