from .. import BaseApi, NamedEndpoint
from .urls import MatchApiUrls


class MatchApi(NamedEndpoint):
    """
    This class wraps the TFT-Match-v1 Api calls provided by the Riot API.

    See https://developer.riotgames.com/apis#tft-match-v1 for more detailed information
    """

    def __init__(self, base_api: BaseApi):
        """
        Initializes a new MatchApi which uses the provided base_api

        :param BaseApi base_api: the root API object to use for making all requests.
        """
        super().__init__(base_api, self.__class__.__name__)

    def by_puuid(self, region: str, puuid: str, count: int = 20):
        """
        Get a list of match ids by PUUID.

        :returns: List[string]
        """
        return self._request_endpoint(
            self.by_puuid.__name__,
            region,
            MatchApiUrls.by_puuid,
            puuid=puuid,
            count=count,
        )

    def by_id(self, region: str, match_id: str):
        """
        Get a match by match id.

        :returns: MatchDto
        """
        return self._request_endpoint(
            self.by_id.__name__, region, MatchApiUrls.by_id, match_id=match_id
        )
