from . import RegionEndpoint


class LeagueEndpoint(RegionEndpoint):
    def __init__(self, url, **kwargs):
        nurl = "/league/v3" + url
        super(LeagueEndpoint, self).__init__(nurl, **kwargs)


class LeagueApiV3Urls(object):
    challenger_by_queue = LeagueEndpoint("/challengerleagues/by-queue/{queue}")
    master_by_queue = LeagueEndpoint("/masterleagues/by-queue/{queue}")
    by_id = LeagueEndpoint("/leagues/{league_id}")
    positions_by_summoner = LeagueEndpoint("/positions/by-summoner/{summoner_id}")
