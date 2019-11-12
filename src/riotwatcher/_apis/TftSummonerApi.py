from . import NamedEndpoint
from .urls import TftSummonerApiUrls

class TftSummonerApi(NamedEndpoint):
    """
    This class wraps the TFT Summoner Api calls provided by the Riot API.

    See https://developer.riotgames.com/apis#tft-summoner-v1 for more detailed information.
    """
    def __init__(self, base_api):
        """
        Initializes a new TftSummonerApi which uses the provided base_api

        :param BaseApi base_api: the root API object to use for making all requests.
        """
        super(TftSummonerApi, self).__init__(base_api, self.__class__.__name__)

    def by_account(self, region, encrypted_account_id):
        url, query = TftSummonerApiUrls.by_account(platform=region, encrypted_account_id=encrypted_account_id)
        return self._raw_request(self.by_account.__name__, region, url, query)
    
    def by_name(self, region, summoner_name):
        url, query = TftSummonerApiUrls.by_name(platform=region, summoner_name=summoner_name)
        return self._raw_request(self.by_name.__name__, region, url, query)
    
    def by_puuid(self, region, encrypted_puuid):
        url, query = TftSummonerApiUrls.by_puuid(platform=region, encrypted_puuid=encrypted_puuid)
        return self._raw_request(self.by_puuid.__name__, region, url, query)
    
    def by_id(self, region, encrypted_sumoner_id):
        url, query = TftSummonerApiUrls.by_id(platform=region, encrypted_sumoner_id=encrypted_sumoner_id)
        return self._raw_request(self.by_id.__name__, region, url, query)
