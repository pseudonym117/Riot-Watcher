
class LolStatusApiV3:
    def __init__(self, base_api):
        self._base_api = base_api

    def shard_data(self, region):
        return self._base_api.request(region, '/lol/status/v3/shard-data')
