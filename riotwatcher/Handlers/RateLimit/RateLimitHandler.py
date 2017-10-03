
import threading

from .. import RequestHandler


class BaseRateLimitHandler(RequestHandler):
    def __init__(self):
        super(BaseRateLimitHandler, self).__init__()

        self._regions_lock = threading.Lock()
        self._regions = []

    def _get_region_limiter(self, region):
        if region not in self._regions:
            with self._regions_lock:
                # double check that another thread hasnt just added this
                if region not in self._regions:
                    self._regions[region] = RegionLimiter(region)
        return self._regions[region]

    def preview_request(self, region, endpoint_name, method_name, url, query_params):
        """
        called before a request is processed.

        :param string region: the region of this request
        :param string endpoint_name: the name of the endpoint being requested
        :param string method_name: the name of the method being requested
        :param url: the URL that is being requested.
        :param query_params: dict: the parameters to the url that is being queried, e.g. ?key1=val&key2=val2
        """
        return self._get_region_limiter(region)
                   .preview_request(
                        region,
                        endpoint_name,
                        method_name,
                        url,
                        query_params
                   )

    def after_request(self, region, endpoint_name, method_name, url, response):
        """
        Called after a response is received and before it is returned to the user.

        :param string region: the region of this request
        :param string endpoint_name: the name of the endpoint that was requested
        :param string method_name: the name of the method that was requested
        :param url: The url that was requested
        :param response: the response received. This is a response from the Requests library
        """
        return self._get_region_limiter(region)
                   .after_request(
                        region,
                        endpoint_name,
                        method_name,
                        url,
                        response
                   )
