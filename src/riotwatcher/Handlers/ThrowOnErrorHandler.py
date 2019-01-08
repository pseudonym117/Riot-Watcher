from . import RequestHandler
from .. import ApiError
from requests import HTTPError


class ThrowOnErrorHandler(RequestHandler):
    def after_request(self, region, endpoint_name, method_name, url, response):
        try:
            response.raise_for_status()
        except HTTPError as e:
            raise ApiError(*e.args, request=e.request, response=e.response)
