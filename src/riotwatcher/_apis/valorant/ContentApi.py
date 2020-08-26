from .. import BaseApi, NamedEndpoint
from .urls import ContentApiUrls


class ContentApi(NamedEndpoint):
    def __init__(self, base_api: BaseApi):
        super().__init__(base_api, self.__class__.__name__)

    def contents(self, region: str, locale: str = None):
        return self._request_endpoint(
            self.contents.__name__, region, ContentApiUrls.contents, locale=locale
        )
