from .. import BaseApi, NamedEndpoint
from .urls import SummonerApiV4Urls


class SummonerApiV4(NamedEndpoint):
    """
    This class wraps the Summoner-v4 endpoint calls provided by the Riot API.

    See https://developer.riotgames.com/api-methods/#summoner-v4 for more detailed
    information
    """

    def __init__(self, base_api: BaseApi):
        """
        Initialize a new SummonerApiV4 which uses the provided base_api

        :param BaseApi base_api: the root API object to use for making all requests.
        """
        super().__init__(base_api, self.__class__.__name__)

    def by_account(self, region: str, encrypted_account_id: str):
        """
        Get a summoner by account ID.

        :param string region:               The region to execute this request on
        :param string encrypted_account_id: The account ID.

        :returns: SummonerDTO: represents a summoner
        """
        return self._request_endpoint(
            self.by_account.__name__,
            region,
            SummonerApiV4Urls.by_account,
            encrypted_account_id=encrypted_account_id,
        )

    def by_name(self, region: str, summoner_name: str):
        """
        Get a summoner by summoner name

        :param string region:           The region to execute this request on
        :param string summoner_name:    Summoner Name

        :returns: SummonerDTO: represents a summoner
        """
        return self._request_endpoint(
            self.by_name.__name__,
            region,
            SummonerApiV4Urls.by_name,
            summoner_name=summoner_name,
        )

    def by_puuid(self, region: str, encrypted_puuid: str):
        """
        Get a summoner by PUUID.

        :param string region:           The region to execute this request on
        :param string encrypted_puuid:  PUUID

        :returns: SummonerDTO: represents a summoner
        """
        return self._request_endpoint(
            self.by_puuid.__name__,
            region,
            SummonerApiV4Urls.by_puuid,
            encrypted_puuid=encrypted_puuid,
        )

    def by_id(self, region: str, encrypted_summoner_id: str):
        """
        Get a summoner by summoner ID.

        :param string region:                   The region to execute this request on
        :param string encrypted_summoner_id:    Summoner ID

        :returns: SummonerDTO: represents a summoner
        """
        return self._request_endpoint(
            self.by_id.__name__,
            region,
            SummonerApiV4Urls.by_id,
            encrypted_summoner_id=encrypted_summoner_id,
        )
