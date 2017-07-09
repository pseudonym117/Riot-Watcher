
class SpectatorApiV3:
    def __init__(self, base_api):
        self._base_api = base_api

    def featured_games(self, region='na1'):
        return self._base_api.request(region, '/lol/spectator/v3/featured-games')

    def by_summoner(self, summoner_id, region='na1'):
        return self._base_api.request(
            region,
            '/lol/spectator/v3/active-games/by-summoner/{summonerId}'.format(summonerId=summoner_id)
        )
