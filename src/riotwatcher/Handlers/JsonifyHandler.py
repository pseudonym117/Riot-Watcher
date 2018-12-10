from . import RequestHandler


class JsonifyHandler(RequestHandler):
    def after_request(self, region, endpoint_name, method_name, url, response):
        return response.json()

    def after_static_request(self, url, response):
        return response.json()
