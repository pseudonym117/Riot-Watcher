from . import NamedEndpoint
from .urls import LeagueApiV3Urls


class LeagueApiV3(NamedEndpoint):
    """
    This class wraps the League-v3 Api calls provided by the Riot API.

    See https://developer.riotgames.com/api-methods/#league-v3/ for more detailed information
    """

    def __init__(self, base_api):
        """
        Initialize a new LeagueApiV3 which uses the provided base_api

        :param BaseApi base_api: the root API object to use for making all requests.
        """
        super(LeagueApiV3, self).__init__(base_api, self.__class__.__name__)

    def challenger_by_queue(self, region, queue):
        """
        Get the challenger league for a given queue.

        :param string region: the region to execute this request on
        :param string queue: the queue to get the challenger players for

        :returns: LeagueListDTO
        """
        url, query = LeagueApiV3Urls.challenger_by_queue(region=region, queue=queue)
        return self._raw_request(self.challenger_by_queue.__name__, region, url, query)

    def masters_by_queue(self, region, queue):
        """
        Get the master league for a given queue.

        :param string region: the region to execute this request on
        :param string queue: the queue to get the challenger players for

        :returns: LeagueListDTO
        """
        url, query = LeagueApiV3Urls.master_by_queue(region=region, queue=queue)
        return self._raw_request(self.masters_by_queue.__name__, region, url, query)

    def by_id(self, region, league_id):
        """
        Get league with given ID, including inactive entries

        :param string region: the region to execute this request on
        :param string league_id: the league ID to query

        :returns: LeagueListDTO
        """
        url, query = LeagueApiV3Urls.by_id(region=region, league_id=league_id)
        return self._raw_request(self.by_id.__name__, region, url, query)

    def positions_by_summoner(self, region, summoner_id):
        """
        Get league positions in all queues for a given summoner ID

        :param string region: the region to execute this request on
        :param long summoner_id: the summoner ID to query

        :returns: Set[LeaguePositionDTO]
        """
        url, query = LeagueApiV3Urls.positions_by_summoner(
            region=region, summoner_id=summoner_id
        )
        return self._raw_request(
            self.positions_by_summoner.__name__, region, url, query
        )
