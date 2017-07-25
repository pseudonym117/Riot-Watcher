
class RequestHandler(object):
    def __init__(self):
        pass

    def preview_request(self, endpoint_name, method_name, url, query_params):
        """
        called before a request is processed.

        :param string endpoint_name: the name of the endpoint being requested
        :param string method_name: the name of the method being requested
        :param url: the URL that is being requested.
        :param query_params: dict: the parameters to the url that is being queried, e.g. ?key1=val&key2=val2
        """
        pass

    def after_request(self, endpoint_name, method_name, url, response):
        """
        Called after a response is received and before it is returned to the user.

        :param string endpoint_name: the name of the endpoint that was requested
        :param string method_name: the name of the method that was requested
        :param url: The url that was requested
        :param response: the response received. This is a response from the Requests library
        """
        pass
