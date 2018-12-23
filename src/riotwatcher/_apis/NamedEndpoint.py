class NamedEndpoint(object):
    """
    Helper class to inject endpoint name into calls to a HTTPClient instance without
    the child class explicitly adding the name every time.
    """

    def __init__(self, http_client, endpoint_name):
        """
        Initialize a new NamedEndpoint which uses the provided http_client and
        injects the provided endpoint_name into calls to _request

        :param HTTPClient http_client:     the root API object to use for making all requests.
        :param string endpoint_name: the name of the child endpoint
        """
        self._http_client = http_client
        self._endpoint_name = endpoint_name

    async def _raw_request(self, method_name, region, url, query_params):
        """
        Sends a request through the HTTPClient instance provided, injecting the provided endpoint_name
        into the method call, so the caller doesn't have to.

        :param string method_name:  The name of the calling method
        :param string region:       The region to execute this request on
        :param string url:          The full URL to the method being requested.
        :param dict query_params:   Query parameters to be provided in the HTTP request
        """
        return await self._http_client._request(
            self._endpoint_name, method_name, region, url, query_params
        )
