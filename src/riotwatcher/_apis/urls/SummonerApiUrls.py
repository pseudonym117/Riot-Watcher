from . import RegionEndpoint


class SummonerV3Endpoint(RegionEndpoint):
    def __init__(self, url, **kwargs):
        nurl = "/summoner/v3/summoners" + url
        super(SummonerV3Endpoint, self).__init__(nurl, **kwargs)


class SummonerApiV3Urls(object):
    by_account = SummonerV3Endpoint("/by-account/{account_id}")
    by_name = SummonerV3Endpoint("/by-name/{summoner_name}")
    by_id = SummonerV3Endpoint("/{summoner_id}")


class SummonerV4Endpoint(RegionEndpoint):
    def __init__(self, url, **kwargs):
        nurl = "/summoner/v4/summoners" + url
        super(SummonerV4Endpoint, self).__init__(nurl, **kwargs)


class SummonerApiV4Urls(object):
    by_account = SummonerV4Endpoint("/by-account/{encrypted_account_id}")
    by_name = SummonerV4Endpoint("/by-name/{summoner_name}")
    by_puuid = SummonerV4Endpoint("/by-puuid/{encrypted_puuid}")
    by_id = SummonerV4Endpoint("/{encrypted_summoner_id}")
