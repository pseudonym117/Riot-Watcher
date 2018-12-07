from . import RegionEndpoint


class MatchEndpoint(RegionEndpoint):
    def __init__(self, url, **kwargs):
        nurl = "/match/v3" + url
        super(MatchEndpoint, self).__init__(nurl, **kwargs)


class MatchApiV3Urls(object):
    by_id = MatchEndpoint("/matches/{match_id}")
    matchlist_by_account = MatchEndpoint(
        "/matchlists/by-account/{account_id}",
        queue=(int,),
        beginTime=int,
        endTime=int,
        beginIndex=int,
        endIndex=int,
        season=(int,),
        champion=(int,),
    )
    timeline_by_match = MatchEndpoint("/timelines/by-match/{match_id}")
