
class ChampionMasteryApiV3:
    def __init__(self, base_api):
        self._base_api = base_api

    def by_summoner(self, summoner_id, region='na1'):
        return self._base_api.request(
            region,
            '/lol/champion-mastery/v3/champion-masteries/by-summoner/{summonerId}'.format(summonerId=summoner_id)
        )

    def by_summoner_by_champion(self, summoner_id, champion_id, region='na1'):
        return self._base_api.request(
            region,
            '/lol/champion-mastery/v3/champion-masteries/by-summoner/{summonerId}/by-champion/{championId}'.format(
                summonerId=summoner_id,
                championId=champion_id
            )
        )

    def scores_by_summoner(self, summoner_id, region='na1'):
        return self._base_api.request(
            region,
            '/lol/champion-mastery/v3/scores/by-summoner/{summonerId}'.format(summonerId=summoner_id)
        )
