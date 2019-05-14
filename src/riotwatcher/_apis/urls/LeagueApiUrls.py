from .Endpoint import RegionEndpoint


class LeagueV4Endpoint(RegionEndpoint):
    def __init__(self, url, **kwargs):
        nurl = "/league/v4" + url
        super(LeagueV4Endpoint, self).__init__(nurl, **kwargs)


class LeagueApiV4Urls(object):
    challenger_by_queue = LeagueV4Endpoint("/challengerleagues/by-queue/{queue}")
    grandmaster_by_queue = LeagueV4Endpoint("/grandmasterleagues/by-queue/{queue}")
    by_id = LeagueV4Endpoint("/leagues/{league_id}")
    master_by_queue = LeagueV4Endpoint("/masterleagues/by-queue/{queue}")
    by_summoner = LeagueV4Endpoint("/entries/by-summoner/{encrypted_summoner_id}")
    entries = LeagueV4Endpoint("/entries/{queue}/{tier}/{division}", page=int)

    # deprecated
    positions_by_summoner = LeagueV4Endpoint(
        "/positions/by-summoner/{encrypted_summoner_id}"
    )
