from .. import BaseApi, NamedEndpoint
from .urls import SpectatorApiV5Urls


class SpectatorApiV5(NamedEndpoint):
    """
    This class wraps the Spectator-v5 endpoint calls provided by the Riot API.

    See https://developer.riotgames.com/api-methods/#spectator-v5 for more detailed
    information
    """

    def __init__(self, base_api: BaseApi):
        """
        Initialize a new SpectatorApiV5 which uses the provided base_api

        :param BaseApi base_api: the root API object to use for making all requests.
        """
        super().__init__(base_api, self.__class__.__name__)

    def by_summoner(self, region: str, encrypted_puuid: str):
        """
        Get current game information for the given PUUID

        :param string region:                   The region to execute this request on
        :param string encrypted_puuid:          The PUUID of the summoner.

        :returns: CurrentGameInfo
        """
        return self._request_endpoint(
            self.by_summoner.__name__,
            region,
            SpectatorApiV5Urls.by_summoner,
            encrypted_puuid=encrypted_puuid,
        )

    def featured_games(self, region: str):
        """
        Get list of featured games.

        :param string region: The region to execute this request on

        :returns: FeaturedGames
        """
        return self._request_endpoint(
            self.featured_games.__name__, region, SpectatorApiV5Urls.featured_games
        )
