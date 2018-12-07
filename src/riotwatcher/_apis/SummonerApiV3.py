from . import NamedEndpoint
from .urls import SummonerApiV3Urls


class SummonerApiV3(NamedEndpoint):
    """
    This class wraps the Summoner-v3 endpoint calls provided by the Riot API.

    See https://developer.riotgames.com/api-methods/#summoner-v3 for more detailed information
    """

    def __init__(self, base_api):
        """
        Initialize a new SummonerApiV3 which uses the provided base_api

        :param BaseApi base_api: the root API object to use for making all requests.
        """
        super(SummonerApiV3, self).__init__(base_api, SummonerApiV3.__name__)

    def by_account(self, region, account_id):
        """
        Get a summoner by account ID.

        :param string region:   The region to execute this request on
        :param long account_id: The account ID.

        :returns: SummonerDTO: represents a summoner
        """
        url, query = SummonerApiV3Urls.by_account(region=region, account_id=account_id)
        return self._raw_request(self.by_account.__name__, region, url, query)

    def by_name(self, region, summoner_name):
        """
        Get a summoner by summoner name

        :param string region:           The region to execute this request on
        :param string summoner_name:    Summoner Name

        :returns: SummonerDTO: represents a summoner
        """
        url, query = SummonerApiV3Urls.by_name(
            region=region, summoner_name=summoner_name
        )
        return self._raw_request(self.by_name.__name__, region, url, query)

    def by_id(self, region, summoner_id):
        """
        Get a summoner by summoner ID.

        :param string region:       The region to execute this request on
        :param long summoner_id:    Summoner ID

        :returns: SummonerDTO: represents a summoner
        """
        url, query = SummonerApiV3Urls.by_id(region=region, summoner_id=summoner_id)
        return self._raw_request(self.by_id.__name__, region, url, query)
