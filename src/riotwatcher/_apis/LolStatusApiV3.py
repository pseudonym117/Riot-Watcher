from . import NamedEndpoint
from .urls import LolStatusApiV3Urls


class LolStatusApiV3(NamedEndpoint):
    """
    This class wraps the LoL-Status-v3 Api calls provided by the Riot API.

    See https://developer.riotgames.com/api-methods/#lol-status-v3 for more detailed information
    """

    def __init__(self, base_api):
        """
        Initialize a new LolStatusApiV3 which uses the provided base_api

        :param BaseApi base_api: the root API object to use for making all requests.
        """
        super(LolStatusApiV3, self).__init__(base_api, LolStatusApiV3.__name__)

    def shard_data(self, region):
        """
        Get League of Legends status for the given shard.

        Requests to this API are not counted against the application Rate Limits.

        :param string region: the region to execute this request on

        :returns: ShardStatus
        """
        url, query = LolStatusApiV3Urls.shard_data(platform=region)
        return self._raw_request(self.shard_data.__name__, region, url, query)
