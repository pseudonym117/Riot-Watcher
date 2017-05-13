
class LeagueApiV3:
    def __init__(self, base_api):
        self._base_api = base_api

    def challenger_by_queue(self, queue, region='na1'):
        return self._base_api.request(region, '/lol/league/v3/challengerleagues/by-queue/{queue}'.format(queue=queue))

    def masters_by_queue(self, queue, region='na1'):
        return self._base_api.request(region, '/lol/league/v3/masterleagues/by-queue/{queue}'.format(queue=queue))

    def leagues_by_summoner(self, summoner_id, region='na1'):
        return self._base_api.request(
            region,
            '/lol/league/v3/leagues/by-summoner/{summonerId}'.format(summonerId=summoner_id)
        )

    def positions_by_summoner(self, summoner_id, region='na1'):
        return self._base_api.request(
            region,
            '/lol/league/v3/positions/by-summoner/{summonerId}'.format(summonerId=summoner_id)
        )
