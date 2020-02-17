from .Endpoint import TftEndpoint


class TftMatchEndpoint(TftEndpoint):
    def __init__(self, url: str, **kwargs):
        nurl = "/match/v1/matches" + url
        super().__init__(nurl, **kwargs)


class TftMatchApiUrls:
    by_puuid = TftMatchEndpoint("/by-puuid/{puuid}/ids")
    by_id = TftMatchEndpoint("/{match_id}")
