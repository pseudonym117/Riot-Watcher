from . import NamedEndpoint
from .urls import TftMatchApiUrls

class TftMatchApi(NamedEndpoint):
    """
    This class wraps the TFT Match Api calls provided by the Riot API.

    See https://developer.riotgames.com/apis#tft-match-v1 for more detailed information
    """

    def __init__(self, base_api):
        """
        Initializes a new TftMatchApi which uses the provided base_api

        :param BaseApi base_api: the root API object to use for making all requests.
        """
        super(TftMatchApi, self).__init__(base_api, self.__class__.__name__)
    
    def by_puuid(self, region, encrypted_puuid):
        url, query = TftMatchApiUrls.by_puuid(platform=region, encrypted_puuid=encrypted_puuid)
        return self._raw_request(self.by_puuid.__name__, region, url, query)
    
    def by_id(self, region, match_id):
        url, query = TftMatchApiUrls.by_id(platform=region, match_id=match_id)
        return self._raw_request(self.by_id.__name__, region, url, query)
