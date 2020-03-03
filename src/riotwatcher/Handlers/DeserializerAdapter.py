from typing import Any

from requests import Response

from .RequestHandler import RequestHandler
from ..Deserializer import Deserializer


class DeserializerAdapter(RequestHandler):
    def __init__(self, deserializer: Deserializer):
        self._deserializer = deserializer

    def after_request(
        self,
        region: str,
        endpoint_name: str,
        method_name: str,
        url: str,
        response: Response,
    ) -> Any:
        return self._deserializer.deserialize(endpoint_name, method_name, response.text)

    def after_static_request(self, url: str, response: Response) -> Any:
        # TODO: add params to get endpoint_name and method_name
        return self._deserializer.deserialize(None, None, response.text)
