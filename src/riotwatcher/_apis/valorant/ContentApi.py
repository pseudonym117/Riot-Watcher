from .. import BaseApi, NamedEndpoint
from .urls import ContentApiUrls


class ContentApi(NamedEndpoint):
    """
    This class wraps the Val-Content-v1 Api calls provided by the Riot API.

    See https://developer.riotgames.com/apis#val-content-v1 for more detailed
    information
    """

    def __init__(self, base_api: BaseApi):
        """
        Initialize a new ContentApi which uses the provided base_api

        :param BaseApi base_api: the root API object to use for making all requests.
        """
        super().__init__(base_api, self.__class__.__name__)

    def contents(self, region: str, locale: str = None):
        """
        Get content optionally filtered by locale

        :returns: ContentDto
        """
        return self._request_endpoint(
            self.contents.__name__, region, ContentApiUrls.contents, locale=locale
        )
