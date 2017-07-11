
class ChampionMasteryApiV3:
    def __init__(self, base_api):
        self._base_api = base_api

    def by_summoner(self, region, summoner_id):
        return self._base_api.request(
            region,
            '/lol/champion-mastery/v3/champion-masteries/by-summoner/{summonerId}'.format(summonerId=summoner_id)
        )

    def by_summoner_by_champion(self, region, summoner_id, champion_id):
        return self._base_api.request(
            region,
            '/lol/champion-mastery/v3/champion-masteries/by-summoner/{summonerId}/by-champion/{championId}'.format(
                summonerId=summoner_id,
                championId=champion_id
            )
        )

    def scores_by_summoner(self, region, summoner_id):
        return self._base_api.request(
            region,
            '/lol/champion-mastery/v3/scores/by-summoner/{summonerId}'.format(summonerId=summoner_id)
        )
