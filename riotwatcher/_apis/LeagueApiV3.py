
from . import NamedEndpoint


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
        return self._request(
            self.challenger_by_queue.__name__,
            region,
            '/lol/league/v3/challengerleagues/by-queue/{queue}'.format(queue=queue)
        )

    def masters_by_queue(self, region, queue):
        """
        Get the master league for a given queue.

        :param string region: the region to execute this request on
        :param string queue: the queue to get the challenger players for

        :returns: LeagueListDTO
        """
        return self._request(
            self.masters_by_queue.__name__,
            region,
            '/lol/league/v3/masterleagues/by-queue/{queue}'.format(queue=queue)
        )

    def by_summoner(self, region, summoner_id):
        """
        Get leagues in all queues for a given summoner ID

        :param string region: the region to execute this request on
        :param long summoner_id: the summoner ID to query

        :returns: Set[LeagueListDTO]
        """
        return self._request(
            self.by_summoner.__name__,
            region,
            '/lol/league/v3/leagues/by-summoner/{summonerId}'.format(summonerId=summoner_id)
        )

    def positions_by_summoner(self, region, summoner_id):
        """
        Get league positions in all queues for a given summoner ID

        :param string region: the region to execute this request on
        :param long summoner_id: the summoner ID to query

        :returns: Set[LeaguePositionDTO]
        """
        return self._request(
            self.positions_by_summoner.__name__,
            region,
            '/lol/league/v3/positions/by-summoner/{summonerId}'.format(summonerId=summoner_id)
        )
