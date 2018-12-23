from . import NamedEndpoint
from .urls import ChampionApiV3Urls


class ChampionApiV3(NamedEndpoint):
    """
    This class wraps the Champion-v3 Api calls provided by the Riot API.

    See https://developer.riotgames.com/api-methods/#champion-v3 for more detailed information
    """

    def __init__(self, http_client):
        """
        Initialize a new ChampionApiV3 which uses the provided http_client

        :param HTTPClient http_client: the root API object to use for making all requests.
        """
        super(ChampionApiV3, self).__init__(http_client, self.__class__.__name__)

    async def rotations(self, region):
        """
        Returns champion rotations, including free-to-play and low-level free-to-play rotations.

        :returns: ChampionInfo
        """
        url, query = ChampionApiV3Urls.rotations(region=region)
        return await self._raw_request(self.rotations.__name__, region, url, query)
