from .Endpoint import TftEndpoint


class TftSummonerEndpoint(TftEndpoint):
    def __init__(self, url, **kwargs):
        nurl = "/summoner/v1/summoners" + url
        super(TftSummonerEndpoint, self).__init__(nurl, **kwargs)


class TftSummonerApiUrls(object):
    by_account = TftSummonerEndpoint("/by-account/{encrypted_account_id}")
    by_name = TftSummonerEndpoint("/by-name/{summoner_name}")
    by_puuid = TftSummonerEndpoint("/by-puuid/{puuid}")
    by_id = TftSummonerEndpoint("/{encrypted_summoner_id}")
