import datetime
import logging
import time

from requests import Response

from .RequestHandler import RequestHandler
from ..RateLimiter import RateLimiter

LOG = logging.getLogger(__name__)


class RateLimiterAdapter(RequestHandler):
    def __init__(self, limiter: RateLimiter):
        super().__init__()
        self._limiter = limiter

    def preview_request(
        self,
        region: str,
        endpoint_name: str,
        method_name: str,
        url: str,
        query_params: dict,
    ):
        """
        called before a request is processed.

        :param string region: the region of this request
        :param string endpoint_name: the name of the endpoint being requested
        :param string method_name: the name of the method being requested
        :param url: the URL that is being requested.
        :param query_params: dict: the parameters to the url that is being queried,
                                   e.g. ?key1=val&key2=val2
        """
        wait_until = self._limiter.wait_until(region, endpoint_name, method_name)

        if wait_until is not None and wait_until > datetime.datetime.now():
            to_wait = wait_until - datetime.datetime.now()

            LOG.info(
                "waiting for %s seconds...", to_wait.total_seconds(),
            )
            time.sleep(to_wait.total_seconds())

    def after_request(
        self,
        region: str,
        endpoint_name: str,
        method_name: str,
        url: str,
        response: Response,
    ) -> Response:
        """
        Called after a response is received and before it is returned to the user.

        :param string region: the region of this request
        :param string endpoint_name: the name of the endpoint that was requested
        :param string method_name: the name of the method that was requested
        :param url: The url that was requested
        :param response: the response received. This is a response from the "requests"
                         library
        """
        self._limiter.record_response(
            region, endpoint_name, method_name, response.status_code, response.headers
        )

        return response
