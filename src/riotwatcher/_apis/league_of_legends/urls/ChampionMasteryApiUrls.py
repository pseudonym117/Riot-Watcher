from .LeagueEndpoint import LeagueEndpoint


class ChampionMasteryV4Endpoint(LeagueEndpoint):
    def __init__(self, url, **kwargs):
        nurl = f"/champion-mastery/v4{url}"
        super().__init__(nurl, **kwargs)


class ChampionMasteryApiV4Urls:
    by_summoner = ChampionMasteryV4Endpoint(
        "/champion-masteries/by-summoner/{encrypted_summoner_id}"
    )
    by_summoner_by_champion = ChampionMasteryV4Endpoint(
        "/champion-masteries/by-summoner/{encrypted_summoner_id}/by-champion/{champion_id}"
    )
    scores_by_summoner = ChampionMasteryV4Endpoint(
        "/scores/by-summoner/{encrypted_summoner_id}"
    )
