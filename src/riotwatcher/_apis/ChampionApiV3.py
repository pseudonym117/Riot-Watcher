from . import NamedEndpoint
from .urls import ChampionApiV3Urls


class ChampionApiV3(NamedEndpoint):
    """
    This class wraps the Champion-v3 Api calls provided by the Riot API.

    See https://developer.riotgames.com/api-methods/#champion-v3 for more detailed information
    """

    def __init__(self, base_api):
        """
        Initialize a new ChampionApiV3 which uses the provided base_api

        :param BaseApi base_api: the root API object to use for making all requests.
        """
        super(ChampionApiV3, self).__init__(base_api, self.__class__.__name__)

    def rotations(self, region):
        """
        Returns champion rotations, including free-to-play and low-level free-to-play rotations.

        :returns: ChampionInfo
        """
        url, query = ChampionApiV3Urls.rotations(platform=region)
        return self._raw_request(self.rotations.__name__, region, url, query)
