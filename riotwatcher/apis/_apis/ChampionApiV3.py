
class ChampionApiV3:
    """
    This class wraps the Champion Api v3 calls provided by the Riot API.
    See https://developer.riotgames.com/api-methods/#champion-v3 for more detailed information
    """
    def __init__(self, base_api):
        """
        Initialize a new ChampionApiV3 which uses the provided base_api

        :param base_api BaseApi: the root API object to use for making all requests.
        """
        self._base_api = base_api

    def champions(self, region, free_to_play=False):
        """
        Retrieve all champions.

        :param string region: the region to execute this request on
        :param bool free_to_play: Optional filter param to retrieve only free to play champions.
        :returns: List[ChampionDto] - This object contains a collection of champion information.
        """
        return self._base_api.request(region, '/lol/platform/v3/champions', freeToPlay=free_to_play)

    def champions_by_id(self, region, champion_id):
        """
        Retrieve champion by ID

        :param string region: the region to execute this request on
        :param int champion_id: Champion ID
        :returns: ChampionDto - This object contains a collection of champion information.
        """
        return self._base_api.request(region, '/lol/platform/v3/champions/{id}'.format(id=champion_id))
