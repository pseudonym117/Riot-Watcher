from .LeagueEndpoint import LeagueEndpoint


class ChampionMasteryV4Endpoint(LeagueEndpoint):
    def __init__(self, url, **kwargs):
        nurl = f"/champion-mastery/v4{url}"
        super().__init__(nurl, **kwargs)


class ChampionMasteryApiV4Urls:
    by_puuid = ChampionMasteryV4Endpoint("/champion-masteries/by-puuid/{puuid}")
    by_puuid_by_champion = ChampionMasteryV4Endpoint(
        "/champion-masteries/by-puuid/{puuid}/by-champion/{champion_id}"
    )
    top_by_puuid = ChampionMasteryV4Endpoint(
        "/champion-masteries/by-puuid/{puuid}/top", count=int
    )
    scores_by_puuid = ChampionMasteryV4Endpoint("/scores/by-puuid/{puuid}")
