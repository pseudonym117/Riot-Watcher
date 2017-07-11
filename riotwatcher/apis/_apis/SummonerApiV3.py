
class SummonerApiV3:
    def __init__(self, base_api):
        self._base_api = base_api

    def by_account(self, region, account_id):
        return self._base_api.request(
            region,
            '/lol/summoner/v3/summoners/by-account/{accountId}'.format(accountId=account_id)
        )

    def by_name(self, region, summoner_name):
        return self._base_api.request(
            region,
            '/lol/summoner/v3/summoners/by-name/{summonerName}'.format(summonerName=summoner_name)
        )

    def __call__(self, region, summoner_id):
        return self._base_api.request(
            region,
            '/lol/summoner/v3/summoners/{summonerId}'.format(summonerId=summoner_id)
        )
