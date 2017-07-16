
from . import RequestHandler


class JsonifyHandler(RequestHandler):
    def __init__(self):
        super(JsonifyHandler, self).__init__()

    def after_request(self, endpoint_name, method_name, url, response):
        return response.json()
