from . import BaseApi, NamedEndpoint
from .urls import LorRankedApiUrls


class LorRankedApi(NamedEndpoint):
    """
    This class wraps the LOR-RANKED-V1 Api calls provided by the Riot API.

    See https://developer.riotgames.com/apis#lor-ranked-v1 for more detailed
    information
    """

    def __init__(self, base_api: BaseApi):
        """
        Initialize a new LorRankedApi which uses the provided base_api

        :param BaseApi base_api: the root API object to use for making all requests.
        """
        super().__init__(base_api, self.__class__.__name__)

    def leaderboards(self, region: str):
        url, query = LorRankedApiUrls.leaderboards(platform=region)

        return self._raw_request(self.leaderboards.__name__, region, url, query)
