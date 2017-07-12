
class LeagueApiV3:
    """
    This class wraps the League-v3 Api calls provided by the Riot API.
    See https://developer.riotgames.com/api-methods/#league-v3/ for more detailed information
    """
    def __init__(self, base_api):
        """
        Initialize a new LeagueApiV3 which uses the provided base_api

        :param base_api BaseApi: the root API object to use for making all requests.
        """
        self._base_api = base_api

    def challenger_by_queue(self, region, queue):
        """
        Get the challenger league for a given queue.

        :param region string: the region to execute this request on
        :param queue string: the queue to get the challenger players for

        :returns: LeagueListDTO
        """
        return self._base_api.request(region, '/lol/league/v3/challengerleagues/by-queue/{queue}'.format(queue=queue))

    def masters_by_queue(self, region, queue):
        """
        Get the master league for a given queue.

        :param region string: the region to execute this request on
        :param queue string: the queue to get the challenger players for

        :returns: LeagueListDTO
        """
        return self._base_api.request(region, '/lol/league/v3/masterleagues/by-queue/{queue}'.format(queue=queue))

    def leagues_by_summoner(self, region, summoner_id):
        """
        Get leagues in all queues for a given summoner ID

        :param region string: the region to execute this request on
        :param summoner_id long: the summoner ID to query

        :returns: Set[LeagueListDTO]
        """
        return self._base_api.request(
            region,
            '/lol/league/v3/leagues/by-summoner/{summonerId}'.format(summonerId=summoner_id)
        )

    def positions_by_summoner(self, region, summoner_id):
        """
        Get league positions in all queues for a given summoner ID

        :param region string: the region to execute this request on
        :param summoner_id long: the summoner ID to query

        :returns:Set[LeaguePositionDTO]
        """
        return self._base_api.request(
            region,
            '/lol/league/v3/positions/by-summoner/{summonerId}'.format(summonerId=summoner_id)
        )
