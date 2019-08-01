from . import NamedEndpoint
from .urls import LeagueApiV4Urls


class LeagueApiV4(NamedEndpoint):
    """
    This class wraps the League-v4 Api calls provided by the Riot API.

    See https://developer.riotgames.com/api-methods/#league-v4/ for more detailed information
    """

    def __init__(self, base_api):
        """
        Initialize a new LeagueApiV4 which uses the provided base_api

        :param BaseApi base_api: the root API object to use for making all requests.
        """
        super(LeagueApiV4, self).__init__(base_api, self.__class__.__name__)

    def challenger_by_queue(self, region, queue):
        """
        Get the challenger league for a given queue.

        :param string region:   the region to execute this request on
        :param string queue:    the queue to get the challenger players for

        :returns: LeagueListDTO
        """
        url, query = LeagueApiV4Urls.challenger_by_queue(platform=region, queue=queue)
        return self._raw_request(self.challenger_by_queue.__name__, region, url, query)

    def grandmaster_by_queue(self, region, queue):
        """
        Get the grandmaster league for a given queue.

        :param string region:   the region to execute this request on
        :param string queue:    the queue to get the grandmaster players for

        :returns: LeagueListDTO
        """
        url, query = LeagueApiV4Urls.grandmaster_by_queue(platform=region, queue=queue)
        return self._raw_request(self.grandmaster_by_queue.__name__, region, url, query)

    def masters_by_queue(self, region, queue):
        """
        Get the master league for a given queue.

        :param string region:   the region to execute this request on
        :param string queue:    the queue to get the master players for

        :returns: LeagueListDTO
        """
        url, query = LeagueApiV4Urls.master_by_queue(platform=region, queue=queue)
        return self._raw_request(self.masters_by_queue.__name__, region, url, query)

    def by_id(self, region, league_id):
        """
        Get league with given ID, including inactive entries

        :param string region:       the region to execute this request on
        :param string league_id:    the league ID to query

        :returns: LeagueListDTO
        """
        url, query = LeagueApiV4Urls.by_id(platform=region, league_id=league_id)
        return self._raw_request(self.by_id.__name__, region, url, query)

    def by_summoner(self, region, encrypted_summoner_id):
        """
        Get league entries in all queues for a given summoner ID

        :param string region:                   the region to execute this request on
        :param string encrypted_summoner_id:    the summoner ID to query

        :returns: Set[LeagueEntryDTO]
        """
        url, query = LeagueApiV4Urls.by_summoner(
            platform=region, encrypted_summoner_id=encrypted_summoner_id
        )
        return self._raw_request(self.by_summoner.__name__, region, url, query)

    def entries(self, region, queue, tier, division, page=1):
        """
        Get all the league entries

        :param string region:   the region to execute this request on
        :param string queue:    the queue to query, i.e. RANKED_SOLO_5x5
        :param string tier:     the tier to query, i.e. DIAMOND
        :param string division: the division to query, i.e. III
        :param int page:        the page for the query to paginate to. Starts at 1.

        :returns: Set[LeagueEntryDTO]
        """
        url, query = LeagueApiV4Urls.entries(
            platform=region, queue=queue, tier=tier, division=division, page=page
        )
        return self._raw_request(self.entries.__name__, region, url, query)

    def positions_by_summoner(self, region, encrypted_summoner_id):
        """
        DEPRECATED

        Get league positions in all queues for a given summoner ID

        :param string region:                   the region to execute this request on
        :param string encrypted_summoner_id:    the summoner ID to query

        :returns: Set[LeaguePositionDTO]
        """
        url, query = LeagueApiV4Urls.positions_by_summoner(
            platform=region, encrypted_summoner_id=encrypted_summoner_id
        )
        return self._raw_request(
            self.positions_by_summoner.__name__, region, url, query
        )
