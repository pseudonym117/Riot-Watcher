
from . import RequestHandler


class ThrowOnErrorHandler(RequestHandler):
    def __init__(self):
        super(ThrowOnErrorHandler, self).__init__()

    def after_request(self, endpoint_name, method_name, url, response):
        response.raise_for_status()
