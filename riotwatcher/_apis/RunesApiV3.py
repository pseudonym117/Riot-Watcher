
from . import NamedEndpoint


class RunesApiV3(NamedEndpoint):
    """
    This class wraps the Runes-v3 endpoint calls provided by the Riot API.
    See https://developer.riotgames.com/api-methods/#runes-v3 for more detailed information
    """
    def __init__(self, base_api):
        """
        Initialize a new RunesApiV3 which uses the provided base_api

        :param BaseApi base_api: the root API object to use for making all requests.
        """
        super(RunesApiV3, self).__init__(base_api, RunesApiV3.__name__)

    def by_summoner(self, region, summoner_id):
        """
        Get rune pages for a given summoner ID.

        :param string region:       The region to execute this request on
        :param long summoner_id:    Summoner ID

        :returns: RunePagesDto
        """
        return self._request(
            self.by_summoner.__name__,
            region,
            '/lol/platform/v3/runes/by-summoner/{summonerId}'.format(summonerId=summoner_id)
        )
