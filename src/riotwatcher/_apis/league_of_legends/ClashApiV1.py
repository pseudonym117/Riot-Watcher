from .. import BaseApi, NamedEndpoint
from .urls import ClashApiV1Urls


class ClashApiV1(NamedEndpoint):
    """
    This class wraps the Clash-v1 endpoint calls provided by the Riot API.

    See https://developer.riotgames.com/apis#clash-v1 for more detailed information
    """

    def __init__(self, base_api: BaseApi):
        """
        Initialize a new SummonerApiV4 which uses the provided base_api

        :param BaseApi base_api: the root API object to use for making all requests.
        """
        super().__init__(base_api, self.__class__.__name__)

    def by_summoner_id(self, region: str, summoner_id: str):
        """
        Get players by summoner ID.

        :param string region:               The region to execute this request on.
        :param string summoner_id:          The summoner ID.

        :returns: List[PlayerDTO]: represents the summoner's info for the current clash.
        """
        return self._request_endpoint(
            self.by_summoner_id.__name__,
            region,
            ClashApiV1Urls.by_summoner_id,
            summoner_id=summoner_id,
        )

    def by_team_id(self, region: str, team_id: str):
        """
        Get team by ID.

        :param string region:               The region to execute this request on
        :param string team_id:              Team ID

        :returns: TeamDTO: represents a clash team
        """
        return self._request_endpoint(
            self.by_team_id.__name__,
            region,
            ClashApiV1Urls.by_team_id,
            team_id=team_id,
        )

    def tournaments(self, region: str):
        """
        Get all active or upcoming tournaments.

        :param string region:           The region to execute this request on

        :returns: List[TournamentDTO]: represents all of the current tournaments active
        """
        return self._request_endpoint(
            self.tournaments.__name__,
            region,
            ClashApiV1Urls.tournaments,
        )

    def tournament_by_team_id(self, region: str, team_id: str):
        """
        Get tournament by team ID.

        :param string region:                   The region to execute this request on
        :param string team_id:                  Team ID

        :returns: TournamentDTO: represents a clash tournament
        """
        return self._request_endpoint(
            self.tournament_by_team_id.__name__,
            region,
            ClashApiV1Urls.tournament_by_team_id,
            team_id=team_id,
        )
    
    def by_tournament_id(self, region: str, tournament_id: str):
        """
        Get tournament by ID.

        :param string region:                   The region to execute this request on
        :param string tournament_id:            Tournament ID

        :returns: TournamentDTO: represents a clash tournament
        """
        return self._request_endpoint(
            self.by_tournament_id.__name__,
            region,
            ClashApiV1Urls.by_tournament_id,
            tournament_id=tournament_id,
        )
