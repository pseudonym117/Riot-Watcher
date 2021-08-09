from .. import BaseApi, NamedEndpoint
from .urls import LolStatusApiV4Urls


class LolStatusApiV4(NamedEndpoint):
    """
    This class wraps the LoL-Status-v4 Api calls provided by the Riot API.

    See https://developer.riotgames.com/api-methods/#lol-status-v3 for more detailed information
    """

    def __init__(self, base_api: BaseApi):
        """
        Initialize a new LolStatusApiV4 which uses the provided base_api

        :param BaseApi base_api: the root API object to use for making all requests.
        """
        super().__init__(base_api, LolStatusApiV4.__name__)

    def platform_data(self, region: str):
        """
        Get League of Legends status for the given platform.

        Requests to this API are not counted against the application Rate Limits.

        :param string region: the region to execute this request on

        :returns: PlatformStatus
        """
        return self._request_endpoint(
            self.platform_data.__name__, region, LolStatusApiV4Urls.platform_data
        )
