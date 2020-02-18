from .TftEndpoint import TftEndpoint


class SummonerEndpoint(TftEndpoint):
    def __init__(self, url: str, **kwargs):
        nurl = "/summoner/v1/summoners" + url
        super().__init__(nurl, **kwargs)


class SummonerApiUrls:
    by_account = SummonerEndpoint("/by-account/{encrypted_account_id}")
    by_name = SummonerEndpoint("/by-name/{summoner_name}")
    by_puuid = SummonerEndpoint("/by-puuid/{puuid}")
    by_id = SummonerEndpoint("/{encrypted_summoner_id}")
