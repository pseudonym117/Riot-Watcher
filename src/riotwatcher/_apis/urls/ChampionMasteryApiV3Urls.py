from . import RegionEndpoint


class ChampionMasteryEndpoint(RegionEndpoint):
    def __init__(self, url, **kwargs):
        nurl = "/champion-mastery/v3" + url
        super(ChampionMasteryEndpoint, self).__init__(nurl, **kwargs)


class ChampionMasteryApiV3Urls(object):
    by_summoner = ChampionMasteryEndpoint(
        "/champion-masteries/by-summoner/{summoner_id}"
    )
    by_summoner_by_champion = ChampionMasteryEndpoint(
        "/champion-masteries/by-summoner/{summoner_id}/by-champion/{champion_id}"
    )
    scored_by_summoner = ChampionMasteryEndpoint("/scores/by-summoner/{summoner_id}")
