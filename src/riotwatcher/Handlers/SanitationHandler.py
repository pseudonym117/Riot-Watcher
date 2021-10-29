import re

from . import IllegalArgumentError, RequestHandler


class SanitationHandler(RequestHandler):
    """
    The SanitationHandler class provides some basic sanity checks to parameters to
    ensure safe usage.

    Only check as of now is ensuring that region doesn't cause HTTP requests to unknown
    servers, which would allow a malicious user to steal API keys.
    """

    def __init__(self):
        super().__init__()
        self._region_expr = re.compile("[a-zA-Z0-9]+")

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

        :param string endpoint_name: the name of the endpoint being requested
        :param string method_name: the name of the method being requested
        :param url: the URL that is being requested.
        :param query_params: dict: the parameters to the url that is being queried,
                                   e.g. ?key1=val&key2=val2
        """
        region_ok = self._region_expr.fullmatch(region)
        if region_ok is None:
            raise IllegalArgumentError("region", region)
