
class LolStatusApiV3:
    """
    This class wraps the LoL-Status-v3 Api calls provided by the Riot API.
    See https://developer.riotgames.com/api-methods/#lol-status-v3 for more detailed information
    """
    def __init__(self, base_api):
        """
        Initialize a new LolStatusApiV3 which uses the provided base_api

        :param base_api BaseApi: the root API object to use for making all requests.
        """
        self._base_api = base_api

    def shard_data(self, region):
        """
        Get League of Legends status for the given shard.

        :param region string: the region to execute this request on

        :returns: ShardStatus
        """
        return self._base_api.request(region, '/lol/status/v3/shard-data')
