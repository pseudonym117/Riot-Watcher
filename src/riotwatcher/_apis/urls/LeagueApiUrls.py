from . import RegionEndpoint


class LeagueV3Endpoint(RegionEndpoint):
    def __init__(self, url, **kwargs):
        nurl = "/league/v3" + url
        super(LeagueV3Endpoint, self).__init__(nurl, **kwargs)


class LeagueApiV3Urls(object):
    challenger_by_queue = LeagueV3Endpoint("/challengerleagues/by-queue/{queue}")
    master_by_queue = LeagueV3Endpoint("/masterleagues/by-queue/{queue}")
    by_id = LeagueV3Endpoint("/leagues/{league_id}")
    positions_by_summoner = LeagueV3Endpoint("/positions/by-summoner/{summoner_id}")


class LeagueV4Endpoint(RegionEndpoint):
    def __init__(self, url, **kwargs):
        nurl = "/league/v4" + url
        super(LeagueV4Endpoint, self).__init__(nurl, **kwargs)


class LeagueApiV4Urls(object):
    challenger_by_queue = LeagueV4Endpoint("/challengerleagues/by-queue/{queue}")
    grandmaster_by_queue = LeagueV4Endpoint("/grandmasterleagues/by-queue/{queue}")
    by_id = LeagueV4Endpoint("/leagues/{league_id}")
    master_by_queue = LeagueV4Endpoint("/masterleagues/by-queue/{queue}")
    positions_by_summoner = LeagueV4Endpoint(
        "/positions/by-summoner/{encrypted_summoner_id}"
    )
