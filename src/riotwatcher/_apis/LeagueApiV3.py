from . import NamedEndpoint
from .urls import LeagueApiV3Urls


class LeagueApiV3(NamedEndpoint):
    """
    This class wraps the League-v3 Api calls provided by the Riot API.

    See https://developer.riotgames.com/api-methods/#league-v3/ for more detailed information
    """

    def __init__(self, http_client):
        """
        Initialize a new LeagueApiV3 which uses the provided http_client

        :param HTTPClient http_client: the root API object to use for making all requests.
        """
        super(LeagueApiV3, self).__init__(http_client, self.__class__.__name__)

    async def challenger_by_queue(self, region, queue):
        """
        Get the challenger league for a given queue.

        :param string region: the region to execute this request on
        :param string queue: the queue to get the challenger players for

        :returns: LeagueListDTO
        """
        url, query = LeagueApiV3Urls.challenger_by_queue(region=region, queue=queue)
        return await self._raw_request(self.challenger_by_queue.__name__, region, url, query)

    async def masters_by_queue(self, region, queue):
        """
        Get the master league for a given queue.

        :param string region: the region to execute this request on
        :param string queue: the queue to get the challenger players for

        :returns: LeagueListDTO
        """
        url, query = LeagueApiV3Urls.master_by_queue(region=region, queue=queue)
        return await self._raw_request(self.masters_by_queue.__name__, region, url, query)

    async def by_id(self, region, league_id):
        """
        Get league with given ID, including inactive entries

        :param string region: the region to execute this request on
        :param string league_id: the league ID to query

        :returns: LeagueListDTO
        """
        url, query = LeagueApiV3Urls.by_id(region=region, league_id=league_id)
        return await self._raw_request(self.by_id.__name__, region, url, query)

    async def positions_by_summoner(self, region, summoner_id):
        """
        Get league positions in all queues for a given summoner ID

        :param string region: the region to execute this request on
        :param long summoner_id: the summoner ID to query

        :returns: Set[LeaguePositionDTO]
        """
        url, query = LeagueApiV3Urls.positions_by_summoner(
            region=region, summoner_id=summoner_id
        )
        return await self._raw_request(
            self.positions_by_summoner.__name__, region, url, query
        )
