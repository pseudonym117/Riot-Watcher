
class MasteriesApiV3:
    def __init__(self, base_api):
        self._base_api = base_api

    def by_summoner(self, region, summoner_id):
        return self._base_api.request(
            region,
            '/lol/platform/v3/masteries/by-summoner/{summonerId}'.format(summonerId=summoner_id)
        )
