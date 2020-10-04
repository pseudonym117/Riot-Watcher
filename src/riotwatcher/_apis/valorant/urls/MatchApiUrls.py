from .ValEndpoint import ValEndpoint


class MatchEndpoint(ValEndpoint):
    def __init__(self, url: str, **kwargs):
        super().__init__(f"/match/v1{url}", **kwargs)


class MatchApiUrls:
    by_id = MatchEndpoint("/matches/{match_id}")
    matchlist_by_puuid = MatchEndpoint("/matchlists/by-puuid/{puuid}")
    recent_matches = MatchEndpoint("/recent-matches/by-queue/{queue}")
