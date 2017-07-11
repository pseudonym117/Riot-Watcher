
class ChampionApiV3:
    def __init__(self, base_api):
        self._base_api = base_api

    def champions(self, region, free_to_play=False):
        """
        Retrieve all champions.

        :param bool free_to_play: Optional filter param to retrieve only free to play champions.
        """
        return self._base_api.request(region, '/lol/platform/v3/champions', freeToPlay=free_to_play)

    def champions_by_id(self, region, champion_id):
        return self._base_api.request(region, '/lol/platform/v3/champions/{id}'.format(id=champion_id))
