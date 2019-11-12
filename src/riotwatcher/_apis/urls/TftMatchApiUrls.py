from .Endpoint import TftEndpoint


class TftMatchEndpoint(TftEndpoint):
    def __init__(self, url, **kwargs):
        nurl = "/match/v1/matches" + url
        super(TftMatchEndpoint, self).__init__(nurl, **kwargs)


class TftMatchApiUrls(object):
    by_puuid = TftMatchEndpoint("/by-puuid/{encrypted_puuid}/ids")
    by_id = TftMatchEndpoint("/{match_id}")
