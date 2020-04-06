from .LeagueEndpoint import LeagueEndpoint


class ClashV1Endpoint(LeagueEndpoint):
    def __init__(self, url, **kwargs):
        nurl = f"/clash/v1{url}"
        super().__init__(nurl, **kwargs)


class ClashApiV1Urls:
    by_summoner = ClashV1Endpoint("/players/by-summoner/{summoner_id}")
    by_team = ClashV1Endpoint("/teams/{team_id}")
    tournaments = ClashV1Endpoint("/tournaments")
    tournament_by_team = ClashV1Endpoint("/tournaments/by-team/{team_id}")
    by_tournament = ClashV1Endpoint("/tournaments/{tournament_id}")
