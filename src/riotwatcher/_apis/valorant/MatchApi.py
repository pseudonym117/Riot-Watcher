from .. import BaseApi, NamedEndpoint
from .urls import MatchApiUrls


class MatchApi(NamedEndpoint):
    def __init__(self, base_api: BaseApi):
        super().__init__(base_api, self.__class__.__name__)

    def by_id(self, region: str, match_id: str):
        return self._request_endpoint(
            self.by_id.__name__, region, MatchApiUrls.by_id, match_id=match_id
        )

    def matchlist_by_puuid(self, region: str, puuid: str):
        return self._request_endpoint(
            self.matchlist_by_puuid.__name__,
            region,
            MatchApiUrls.matchlist_by_puuid,
            puuid=puuid,
        )
