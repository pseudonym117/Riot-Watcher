from . import RegionEndpoint


class MatchV3Endpoint(RegionEndpoint):
    def __init__(self, url, **kwargs):
        nurl = "/match/v3" + url
        super(MatchV3Endpoint, self).__init__(nurl, **kwargs)


class MatchApiV3Urls(object):
    by_id = MatchV3Endpoint("/matches/{match_id}")
    matchlist_by_account = MatchV3Endpoint(
        "/matchlists/by-account/{account_id}",
        queue=(int,),
        beginTime=int,
        endTime=int,
        beginIndex=int,
        endIndex=int,
        season=(int,),
        champion=(int,),
    )
    timeline_by_match = MatchV3Endpoint("/timelines/by-match/{match_id}")


class MatchV4Endpoint(RegionEndpoint):
    def __init__(self, url, **kwargs):
        nurl = "/match/v4" + url
        super(MatchV4Endpoint, self).__init__(nurl, **kwargs)


class MatchApiV4Urls(object):
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
