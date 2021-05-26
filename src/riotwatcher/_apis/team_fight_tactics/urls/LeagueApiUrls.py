from .TftEndpoint import TftEndpoint


class LeagueEndpoint(TftEndpoint):
    def __init__(self, url: str, **kwargs):
        nurl = "/league/v1" + url
        super().__init__(nurl, **kwargs)


class LeagueApiUrls:
    challenger = LeagueEndpoint("/challenger")
    by_summoner = LeagueEndpoint("/entries/by-summoner/{encrypted_summoner_id}")
    entries = LeagueEndpoint("/entries/{tier}/{division}", page=int)
    grandmaster = LeagueEndpoint("/grandmaster")
    by_id = LeagueEndpoint("/leagues/{league_id}")
    master = LeagueEndpoint("/master")
    rated_ladders = LeagueEndpoint("/rated-ladders/{queue}/top")
