from requests import Response

from . import RequestHandler


class JsonifyHandler(RequestHandler):
    def after_request(
        self,
        region: str,
        endpoint_name: str,
        method_name: str,
        url: str,
        response: Response,
    ) -> dict:
        return response.json()

    def after_static_request(self, url: str, response: Response) -> dict:
        return response.json()
