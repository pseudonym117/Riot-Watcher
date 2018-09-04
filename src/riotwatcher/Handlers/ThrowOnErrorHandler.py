
from . import RequestHandler


class ThrowOnErrorHandler(RequestHandler):
    def after_request(self, region, endpoint_name, method_name, url, response):
        response.raise_for_status()
