from . import NamedEndpoint
from .urls import SpectatorApiV3Urls


class SpectatorApiV3(NamedEndpoint):
    """
    This class wraps the Spectator-v3 endpoint calls provided by the Riot API.

    See https://developer.riotgames.com/api-methods/#spectator-v3 for more detailed information
    """

    def __init__(self, base_api):
        """
        Initialize a new SpectatorApiV3 which uses the provided base_api

        :param BaseApi base_api: the root API object to use for making all requests.
        """
        super(SpectatorApiV3, self).__init__(base_api, SpectatorApiV3.__name__)

    def by_summoner(self, region, summoner_id):
        """
        Get current game information for the given summoner ID

        :param string region:       The region to execute this request on
        :param long summoner_id:    The ID of the summoner.

        :returns: CurrentGameInfo
        """
        url, query = SpectatorApiV3Urls.by_summoner(
            region=region, summoner_id=summoner_id
        )
        return self._raw_request(self.by_summoner.__name__, region, url, query)

    def featured_games(self, region):
        """
        Get list of featured games.

        :param string region: The region to execute this request on

        :returns: FeaturedGames
        """
        url, query = SpectatorApiV3Urls.featured_games(region=region)
        return self._raw_request(self.featured_games.__name__, region, url, query)
