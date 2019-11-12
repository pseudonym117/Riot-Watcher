from . import NamedEndpoint
from .urls import TftLeagueApiUrls

class TftLeagueApi(NamedEndpoint):
    """
    This class wraps the League-v4 Api calls provided by the Riot API.

    See https://developer.riotgames.com/apis#tft-league-v1 for more detailed information
    """

    def __init__(self, base_api):
        """
        Initialize a new TftLeagueApi which uses the provided base_api

        :param BaseApi base_api: the root API object to use for making all requests.
        """
        super(TftLeagueApi, self).__init__(base_api, self.__class__.__name__)

    def challenger(self, region):
        url, query = TftLeagueApiUrls.challenger(platform=region)
        return self._raw_request(self.challenger.__name__, region, url, query)
    
    def by_summoner(self, region, encrypted_summoner_id):
        url, query = TftLeagueApiUrls.by_summoner(platform=region, encrypted_summoner_id=encrypted_summoner_id)
        return self._raw_request(self.by_summoner.__name__, region, url, query)
    
    def entries(self, region, tier, division):
        url, query = TftLeagueApiUrls.entries(platform=region, tier=tier, division=division)
        return self._raw_request(self.entries.__name__, region, url, query)
    
    def grandmaster(self, region):
        url, query = TftLeagueApiUrls.grandmaster(platform=region)
        return self._raw_request(self.grandmaster.__name__, region, url, query)
    
    def by_id(self, region, league_id):
        url, query = TftLeagueApiUrls.by_id(platform=region, league_id=league_id)
        return self._raw_request(self.by_id.__name__, region, url, query)
    
    def master(self, region):
        url, query = TftLeagueApiUrls.master(platform=region)
        return self._raw_request(self.master.__name__, region, url, query)
