
class MasteriesApiV3:
    """
    This class wraps the Masteries-v3 Api calls provided by the Riot API.
    See https://developer.riotgames.com/api-methods/#masteries-v3 for more detailed information
    """
    def __init__(self, base_api):
        """
        Initialize a new MasteriesApiV3 which uses the provided base_api

        :param base_api BaseApi: the root API object to use for making all requests.
        """
        self._base_api = base_api

    def by_summoner(self, region, summoner_id):
        """
        Get mastery pages for a given summoner ID

        :param region string: the region to execute this request on
        :param summoner_id long: the summoner ID to query

        :returns: MasteryPagesDto - This object contains masteries information.
        """
        return self._base_api.request(
            region,
            '/lol/platform/v3/masteries/by-summoner/{summonerId}'.format(summonerId=summoner_id)
        )
