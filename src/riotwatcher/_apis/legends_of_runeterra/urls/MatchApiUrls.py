from .LorEndpoint import LorEndpoint


class MatchEndpoint(LorEndpoint):
    def __init__(self, url: str, **kwargs):
        super().__init__(f"/match/v1{url}", **kwargs)


class MatchApiUrls:
    by_puuid = MatchEndpoint("/matches/by-puuid/{puuid}/ids")
    by_id = MatchEndpoint("/matches/{match_id}")
