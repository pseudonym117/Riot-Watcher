from . import RegionEndpoint


class ChampionMasteryV3Endpoint(RegionEndpoint):
    def __init__(self, url, **kwargs):
        nurl = "/champion-mastery/v3" + url
        super(ChampionMasteryV3Endpoint, self).__init__(nurl, **kwargs)


class ChampionMasteryApiV3Urls(object):
    by_summoner = ChampionMasteryV3Endpoint(
        "/champion-masteries/by-summoner/{summoner_id}"
    )
    by_summoner_by_champion = ChampionMasteryV3Endpoint(
        "/champion-masteries/by-summoner/{summoner_id}/by-champion/{champion_id}"
    )
    scores_by_summoner = ChampionMasteryV3Endpoint("/scores/by-summoner/{summoner_id}")


class ChampionMasteryV4Endpoint(RegionEndpoint):
    def __init__(self, url, **kwargs):
        nurl = "/champion-mastery/v4" + url
        super(ChampionMasteryV4Endpoint, self).__init__(nurl, **kwargs)


class ChampionMasteryApiV4Urls(object):
    by_summoner = ChampionMasteryV4Endpoint(
        "/champion-masteries/by-summoner/{encrypted_summoner_id}"
    )
    by_summoner_by_champion = ChampionMasteryV4Endpoint(
        "/champion-masteries/by-summoner/{encrypted_summoner_id}/by-champion/{champion_id}"
    )
    scores_by_summoner = ChampionMasteryV4Endpoint(
        "/scores/by-summoner/{encrypted_summoner_id}"
    )
