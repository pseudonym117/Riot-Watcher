from . import NamedEndpoint
from .urls import ThirdPartyCodeApiV3Urls


class ThirdPartyCodeApiV3(NamedEndpoint):
    """
    This class wraps the ThirdPartyCode-v3 Api calls provided by the Riot API.

    See https://developer.riotgames.com/api-methods/#third-party-code-v3 for more detailed
    information
    """

    def __init__(self, base_api):
        """
        Initialize a new ThirdPartyCodeApiV3 which uses the provided base_api

        :param BaseApi base_api: the root API object to use for making all requests.
        """
        super(ThirdPartyCodeApiV3, self).__init__(
            base_api, ThirdPartyCodeApiV3.__name__
        )

    def by_summoner(self, region, summoner_id):
        """
        FOR KR SUMMONERS, A 404 WILL ALWAYS BE RETURNED.

        :param string region:       the region to execute this request on
        :param long summoner_id:    Summoner ID

        :returns: string
        """
        url, query = ThirdPartyCodeApiV3Urls.by_summoner(
            region=region, summoner_id=summoner_id
        )

        return self._raw_request(self.by_summoner.__name__, region, url, query)
