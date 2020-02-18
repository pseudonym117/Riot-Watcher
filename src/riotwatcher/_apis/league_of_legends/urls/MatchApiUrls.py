from .LeagueEndpoint import LeagueEndpoint


class MatchV4Endpoint(LeagueEndpoint):
    def __init__(self, url, **kwargs):
        nurl = f"/match/v4{url}"
        super().__init__(nurl, **kwargs)


class MatchApiV4Urls:
    by_id = MatchV4Endpoint("/matches/{match_id}")
    matchlist_by_account = MatchV4Endpoint(
        "/matchlists/by-account/{encrypted_account_id}",
        queue=(int,),
        beginTime=int,
        endTime=int,
        beginIndex=int,
        endIndex=int,
        season=(int,),
        champion=(int,),
    )
    timeline_by_match = MatchV4Endpoint("/timelines/by-match/{match_id}")
