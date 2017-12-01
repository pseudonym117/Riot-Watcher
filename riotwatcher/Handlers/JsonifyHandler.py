
from . import RequestHandler


class JsonifyHandler(RequestHandler):
    def after_request(self, region, endpoint_name, method_name, url, response):
        return response.json()
