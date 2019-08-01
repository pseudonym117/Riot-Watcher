from . import NamedEndpoint
from .urls import SpectatorApiV4Urls


class SpectatorApiV4(NamedEndpoint):
    """
    This class wraps the Spectator-v4 endpoint calls provided by the Riot API.

    See https://developer.riotgames.com/api-methods/#spectator-v4 for more detailed information
    """

    def __init__(self, base_api):
        """
        Initialize a new SpectatorApiV3 which uses the provided base_api

        :param BaseApi base_api: the root API object to use for making all requests.
        """
        super(SpectatorApiV4, self).__init__(base_api, self.__class__.__name__)

    def by_summoner(self, region, encrypted_summoner_id):
        """
        Get current game information for the given summoner ID

        :param string region:                   The region to execute this request on
        :param string encrypted_summoner_id:    The ID of the summoner.

        :returns: CurrentGameInfo
        """
        url, query = SpectatorApiV4Urls.by_summoner(
            platform=region, encrypted_summoner_id=encrypted_summoner_id
        )
        return self._raw_request(self.by_summoner.__name__, region, url, query)

    def featured_games(self, region):
        """
        Get list of featured games.

        :param string region: The region to execute this request on

        :returns: FeaturedGames
        """
        url, query = SpectatorApiV4Urls.featured_games(platform=region)
        return self._raw_request(self.featured_games.__name__, region, url, query)
