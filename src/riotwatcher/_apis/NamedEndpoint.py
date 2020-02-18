from . import BaseApi

from .Endpoint import Endpoint


class NamedEndpoint:
    """
    Helper class to inject endpoint name into calls to a BaseApi instance without
    the child class explicitly adding the name every time.
    """

    def __init__(self, base_api: BaseApi, endpoint_name: str):
        """
        Initialize a new NamedEndpoint which uses the provided base_api and
        injects the provided endpoint_name into calls to _request

        :param BaseApi base_api:     the root API object to use for making all requests.
        :param string endpoint_name: the name of the child endpoint
        """
        self._base_api = base_api
        self._endpoint_name = endpoint_name

    def _request_endpoint(
        self, method_name: str, region: str, endpoint: Endpoint, **kwargs
    ):
        """
        Sends a request through the BaseApi instance provided, injecting the provided endpoint_name
        into the method call, so the caller doesn't have to.

        :param string method_name:  The name of the calling method
        :param string region:       The region to execute this request on
        :oaram Endpoint endpoint:   The endpoint to use to build URL and query parameters
        """
        url, query = endpoint(platform=region, **kwargs)
        return self._base_api.raw_request(
            self._endpoint_name, method_name, region, url, query
        )
