from . import RegionEndpoint


class SummonerEndpoint(RegionEndpoint):
    def __init__(self, url, **kwargs):
        nurl = "/summoner/v3/summoners" + url
        super(SummonerEndpoint, self).__init__(nurl, **kwargs)


class SummonerApiV3Urls(object):
    by_account = SummonerEndpoint("/by-account/{account_id}")
    by_name = SummonerEndpoint("/by-name/{summoner_name}")
    by_id = SummonerEndpoint("/{summoner_id}")
