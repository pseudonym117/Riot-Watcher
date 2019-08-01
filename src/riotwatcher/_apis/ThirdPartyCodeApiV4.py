from . import NamedEndpoint
from .urls import ThirdPartyCodeApiV4Urls


class ThirdPartyCodeApiV4(NamedEndpoint):
    """
    This class wraps the ThirdPartyCode-v4 Api calls provided by the Riot API.

    See https://developer.riotgames.com/api-methods/#third-party-code-v4 for more detailed
    information
    """

    def __init__(self, base_api):
        """
        Initialize a new ThirdPartyCodeApiV4 which uses the provided base_api

        :param BaseApi base_api: the root API object to use for making all requests.
        """
        super(ThirdPartyCodeApiV4, self).__init__(base_api, self.__class__.__name__)

    def by_summoner(self, region, encrypted_summoner_id):
        """
        FOR KR SUMMONERS, A 404 WILL ALWAYS BE RETURNED.

        Valid codes must be no longer than 256 characters and only use
        valid characters: 0-9, a-z, A-Z, and -

        :param string region:                   the region to execute this request on
        :param string encrypted_summoner_id:    Summoner ID

        :returns: string
        """
        url, query = ThirdPartyCodeApiV4Urls.by_summoner(
            platform=region, encrypted_summoner_id=encrypted_summoner_id
        )

        return self._raw_request(self.by_summoner.__name__, region, url, query)
