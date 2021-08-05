from .LeagueEndpoint import LeagueEndpoint


class MatchV5Endpoint(LeagueEndpoint):
    def __init__(self, url, **kwargs):
        nurl = f"/match/v5{url}"
        super().__init__(nurl, **kwargs)


class MatchApiV5Urls:
    by_id = MatchV5Endpoint("/matches/{match_id}")
    matchlist_by_puuid = MatchV5Endpoint(
        "/matches/by-puuid/{puuid}/ids", start=int, count=int, queue=int, type=str
    )
    timeline_by_match = MatchV5Endpoint("/matches/{match_id}/timeline")
