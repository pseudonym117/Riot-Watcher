from .Endpoint import TftEndpoint


class TftLeagueEndpoint(TftEndpoint):
    def __init__(self, url, **kwargs):
        nurl = "/league/v1" + url
        super(TftLeagueEndpoint, self).__init__(nurl, **kwargs)


class TftLeagueApiUrls(object):
    challenger = TftLeagueEndpoint("/challenger")
    by_summoner = TftLeagueEndpoint("/entries/by-summoner/{encrypted_summoner_id}")
    entries = TftLeagueEndpoint("/entries/{tier}/{division}")
    grandmaster = TftLeagueEndpoint("/grandmaster")
    by_id = TftLeagueEndpoint("/leagues/{league_id}")
    master = TftLeagueEndpoint("/master")
