from .. import BaseApi, NamedEndpoint
from .urls import AccountApiUrls


class AccountApi(NamedEndpoint):
    """
    This class wraps the Account-v1 Api calls provided by the Riot API.

    See https://developer.riotgames.com/apis#account-v1 for more detailed information
    """

    def __init__(self, base_api: BaseApi):
        """
        Initialize a new AccountApi which uses the provided base_api

        :param BaseApi base_api: the root API object to use for making all requests.
        """
        super().__init__(base_api, self.__class__.__name__)

    def by_puuid(self, region: str, puuid: str):
        """
        Get account by puuid

        :returns: AcountDto
        """
        return self._request_endpoint(
            self.by_puuid.__name__, region, AccountApiUrls.by_puuid, puuid=puuid
        )

    def by_riot_id(self, region: str, game_name: str, tag_line: str):
        """
        Get account by riot id

        :returns: AccountDto
        """
        return self._request_endpoint(
            self.by_riot_id.__name__,
            region,
            AccountApiUrls.by_riot_id,
            game_name=game_name,
            tag_line=tag_line,
        )

    def active_shard(self, region: str, game: str, puuid: str):
        """
        Get active shard for a player

        :returns: ActiveShardDto
        """
        return self._request_endpoint(
            self.active_shard.__name__,
            region,
            AccountApiUrls.active_shard,
            game=game,
            puuid=puuid,
        )
