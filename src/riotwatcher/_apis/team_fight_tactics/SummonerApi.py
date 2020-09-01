from .. import BaseApi, NamedEndpoint
from .urls import SummonerApiUrls


class SummonerApi(NamedEndpoint):
    """
    This class wraps the TFT-Summoner-v1 Api calls provided by the Riot API.

    See https://developer.riotgames.com/apis#tft-summoner-v1 for more detailed information.
    """

    def __init__(self, base_api: BaseApi):
        """
        Initializes a new SummonerApi which uses the provided base_api

        :param BaseApi base_api: the root API object to use for making all requests.
        """
        super().__init__(base_api, self.__class__.__name__)

    def by_account(self, region: str, encrypted_account_id: str):
        """
        Get a summoner by account ID

        :returns: SummonerDTO
        """
        return self._request_endpoint(
            self.by_account.__name__,
            region,
            SummonerApiUrls.by_account,
            encrypted_account_id=encrypted_account_id,
        )

    def by_name(self, region: str, summoner_name: str):
        """
        Get a summoner by summoner name.

        :returns: SummonerDTO
        """
        return self._request_endpoint(
            self.by_name.__name__,
            region,
            SummonerApiUrls.by_name,
            summoner_name=summoner_name,
        )

    def by_puuid(self, region: str, puuid: str):
        """
        Get a summoner by PUUID.

        :returns: SummonerDTO
        """
        return self._request_endpoint(
            self.by_puuid.__name__, region, SummonerApiUrls.by_puuid, puuid=puuid
        )

    def by_id(self, region: str, encrypted_summoner_id: str):
        """
        Get a summoner by summoner ID

        :returns: SummonerDTO
        """
        return self._request_endpoint(
            self.by_id.__name__,
            region,
            SummonerApiUrls.by_id,
            encrypted_summoner_id=encrypted_summoner_id,
        )
