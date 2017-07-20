
from . import NamedEndpoint


class MasteriesApiV3(NamedEndpoint):
    """
    This class wraps the Masteries-v3 Api calls provided by the Riot API.
    See https://developer.riotgames.com/api-methods/#masteries-v3 for more detailed information
    """
    def __init__(self, base_api):
        """
        Initialize a new MasteriesApiV3 which uses the provided base_api

        :param BaseApi base_api: the root API object to use for making all requests.
        """
        super(MasteriesApiV3, self).__init__(base_api, MasteriesApiV3.__name__)

    def by_summoner(self, region, summoner_id):
        """
        Get mastery pages for a given summoner ID

        :param string region: the region to execute this request on
        :param long summoner_id: the summoner ID to query

        :returns: MasteryPagesDto: This object contains masteries information.
        """
        return self._request(
            self.by_summoner.__name__,
            region,
            '/lol/platform/v3/masteries/by-summoner/{summonerId}'.format(summonerId=summoner_id)
        )
