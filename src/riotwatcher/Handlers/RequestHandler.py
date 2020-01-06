class RequestHandler:
    def __init__(self):
        pass

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

    def after_request(
        self, region: str, endpoint_name: str, method_name: str, url: str, response
    ):
        """
        Called after a response is received and before it is returned to the user.

        :param string region: the region of this request
        :param string endpoint_name: the name of the endpoint that was requested
        :param string method_name: the name of the method that was requested
        :param url: The url that was requested
        :param response: the response received. This is a response from the Requests library
        """

    def preview_static_request(self, url: str, query_params: dict):
        """
        Called before a request to DataDragon is processed

        :param url: The url that was requested
        """

    def after_static_request(self, url: str, response):
        """
        Called after a response is received and before it is returned to the user.

        :param url: The url that was requested
        :param response: the response received. This is a response from the Requests library
        """
