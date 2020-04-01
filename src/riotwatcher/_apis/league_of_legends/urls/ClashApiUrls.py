from .LeagueEndpoint import LeagueEndpoint

class ClashV1Endpoint(LeagueEndpoint):
    def __init__(self, url, **kwargs):
        nurl = f"/clash/v1{url}"
        super().__init__(nurl, **kwargs)


class ClashApiV1Urls:
    by_summoner_id = ClashV1Endpoint("/players/by-summoner/{summoner_id}")
    by_team_id = ClashV1Endpoint("/teams/{team_id}")
    tournaments = ClashV1Endpoint("/tournaments")
    tournament_by_team_id = ClashV1Endpoint("/tournaments/by-team/{team_id}")
    by_tournament_id = ClashV1Endpoint("/tournaments/{tournament_id}")
