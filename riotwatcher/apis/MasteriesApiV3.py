
class MasteriesApiV3:
    def __init__(self, base_api):
        self._base_api = base_api

    def by_summoner(self, summoner_id, region='na1'):
        return self._base_api.request(
            region,
            '/lol/platform/v3/masteries/by-summoner/{summonerId}'.format(summonerId=summoner_id)
        )
