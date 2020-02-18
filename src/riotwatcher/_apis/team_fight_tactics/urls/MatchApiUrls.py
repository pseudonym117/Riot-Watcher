from .TftEndpoint import TftEndpoint


class MatchEndpoint(TftEndpoint):
    def __init__(self, url: str, **kwargs):
        nurl = "/match/v1/matches" + url
        super().__init__(nurl, **kwargs)


class MatchApiUrls:
    by_puuid = MatchEndpoint("/by-puuid/{puuid}/ids", count=int)
    by_id = MatchEndpoint("/{match_id}")
