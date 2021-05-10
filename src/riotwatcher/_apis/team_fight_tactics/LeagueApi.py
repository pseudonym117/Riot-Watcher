from .. import BaseApi, NamedEndpoint
from .urls import LeagueApiUrls


class LeagueApi(NamedEndpoint):
    """
    This class wraps the Tft-League-v1 Api calls provided by the Riot API.

    See https://developer.riotgames.com/apis#tft-league-v1 for more detailed information
    """

    def __init__(self, base_api: BaseApi):
        """
        Initialize a new LeagueApi which uses the provided base_api

        :param BaseApi base_api: the root API object to use for making all requests.
        """
        super().__init__(base_api, self.__class__.__name__)

    def challenger(self, region: str):
        """
        Get the challenger league

        :returns: LeagueListDTO
        """
        return self._request_endpoint(
            self.challenger.__name__, region, LeagueApiUrls.challenger
        )

    def by_summoner(self, region: str, encrypted_summoner_id: str):
        """
        Get league entries for a given summoner ID

        :returns: Set[LeagueEntryDTO]
        """
        return self._request_endpoint(
            self.by_summoner.__name__,
            region,
            LeagueApiUrls.by_summoner,
            encrypted_summoner_id=encrypted_summoner_id,
        )

    def entries(self, region: str, tier: str, division: str, page: int = 1):
        """
        Get all the league entries

        :returns: Set[LeagueEntryDTO]
        """
        return self._request_endpoint(
            self.entries.__name__,
            region,
            LeagueApiUrls.entries,
            tier=tier,
            division=division,
            page=page,
        )

    def grandmaster(self, region: str):
        """
        Get the grandmaster league.

        :returns: LeagueListDTO
        """
        return self._request_endpoint(
            self.grandmaster.__name__, region, LeagueApiUrls.grandmaster
        )

    def by_id(self, region: str, league_id: str):
        """
        Get league with given ID, including inactive entries

        :returns: LeagueListDTO
        """
        return self._request_endpoint(
            self.by_id.__name__, region, LeagueApiUrls.by_id, league_id=league_id
        )

    def master(self, region: str):
        """
        Get the master league

        :returns: LeagueListDTO
        """
        return self._request_endpoint(
            self.master.__name__, region, LeagueApiUrls.master
        )

    def rated_ladders(self, region: str, queue: str):
        """
        Get the top rated ladders 

        :returns: TopRatedLadderEntryDto
        """
        return self._request_endpoint(
            self.rated_ladders.__name__,
            region,
            LeagueApiUrls.rated_ladders,
            queue=queue,
        )
