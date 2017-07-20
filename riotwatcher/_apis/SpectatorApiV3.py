
from . import NamedEndpoint


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
        return self._request(
            self.by_summoner.__name__,
            region,
            '/lol/spectator/v3/active-games/by-summoner/{summonerId}'.format(summonerId=summoner_id)
        )

    def featured_games(self, region):
        """
        Get list of featured games.

        :param string region: The region to execute this request on

        :returns: FeaturedGames
        """
        return self._request(
            self.featured_games.__name__,
            region,
            '/lol/spectator/v3/featured-games'
        )
