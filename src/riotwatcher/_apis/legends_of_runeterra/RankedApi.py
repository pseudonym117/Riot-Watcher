from .. import BaseApi, NamedEndpoint
from .urls import RankedApiUrls


class RankedApi(NamedEndpoint):
    """
    This class wraps the LoR-Ranked-V1 Api calls provided by the Riot API.

    See https://developer.riotgames.com/apis#lor-ranked-v1 for more detailed
    information
    """

    def __init__(self, base_api: BaseApi):
        """
        Initialize a new RankedApi which uses the provided base_api

        :param BaseApi base_api: the root API object to use for making all requests.
        """
        super().__init__(base_api, self.__class__.__name__)

    def leaderboards(self, region: str):
        """
        Get the players in Master tier.

        :returns: LeaderboardDto
        """
        return self._request_endpoint(
            self.leaderboards.__name__, region, RankedApiUrls.leaderboards
        )
