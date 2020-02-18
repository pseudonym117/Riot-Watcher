from .TftEndpoint import TftEndpoint


class TftLeagueEndpoint(TftEndpoint):
    def __init__(self, url: str, **kwargs):
        nurl = "/league/v1" + url
        super().__init__(nurl, **kwargs)


class TftLeagueApiUrls:
    challenger = TftLeagueEndpoint("/challenger")
    by_summoner = TftLeagueEndpoint("/entries/by-summoner/{encrypted_summoner_id}")
    entries = TftLeagueEndpoint("/entries/{tier}/{division}", page=int)
    grandmaster = TftLeagueEndpoint("/grandmaster")
    by_id = TftLeagueEndpoint("/leagues/{league_id}")
    master = TftLeagueEndpoint("/master")
