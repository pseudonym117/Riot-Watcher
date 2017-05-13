
class ChampionApiV3:
    def __init__(self, base_api):
        self._base_api = base_api

    def champions(self, region='na1'):
        return self._base_api.request(region, '/lol/platform/v3/champions')

    def champions_by_id(self, champion_id, region='na1'):
        return self._base_api.request(region, '/lol/platform/v3/champions/{id}'.format(id=champion_id))
