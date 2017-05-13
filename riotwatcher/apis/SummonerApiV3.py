
class SummonerApiV3:
    def __init__(self, base_api):
        self._base_api = base_api

    def by_account(self, account_id, region='na1'):
        return self._base_api.request(
            region,
            '/lol/summoner/v3/summoners/by-account/{accountId}'.format(accountId=account_id)
        )

    def by_name(self, summoner_name, region='na1'):
        return self._base_api.request(
            region,
            '/lol/summoner/v3/summoners/by-name/{summonerName}'.format(summonerName=summoner_name)
        )

    def __call__(self, summoner_id, region='na1'):
        return self._base_api.request(
            region,
            '/lol/summoner/v3/summoners/{summonerId}'.format(summonerId=summoner_id)
        )
