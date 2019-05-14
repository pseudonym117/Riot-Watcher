import requests

from .RequestHandler import RequestHandler

ApiError = requests.HTTPError


class ThrowOnErrorHandler(RequestHandler):
    def after_request(self, region, endpoint_name, method_name, url, response):
        try:
            response.raise_for_status()
        except requests.HTTPError as err:
            raise ApiError(*err.args, request=err.request, response=err.response)
