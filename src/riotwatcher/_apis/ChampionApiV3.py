
from . import NamedEndpoint
from .urls import ChampionApiV3Urls


class ChampionApiV3(NamedEndpoint):
    """
    This class wraps the Champion-v3 Api calls provided by the Riot API.

    See https://developer.riotgames.com/api-methods/#champion-v3 for more detailed information
    """
    def __init__(self, base_api):
        """
        Initialize a new ChampionApiV3 which uses the provided base_api

        :param BaseApi base_api: the root API object to use for making all requests.
        """
        super(ChampionApiV3, self).__init__(base_api, self.__class__.__name__)

    def all(self, region, free_to_play=False):
        """
        Retrieve all champions.

        :param string region: the region to execute this request on
        :param bool free_to_play: Optional filter param to retrieve only free to play champions.

        :returns: List[ChampionDto]: This object contains a collection of champion information.
        """
        url, query = ChampionApiV3Urls.all(region=region, freeToPlay=free_to_play)
        return self._raw_request(self.all.__name__, region, url, query)

    def by_id(self, region, champion_id):
        """
        Retrieve champion by ID

        :param string region: the region to execute this request on
        :param int champion_id: Champion ID

        :returns: ChampionDto: This object contains a collection of champion information.
        """
        url, query = ChampionApiV3Urls.by_id(region=region, champion_id=champion_id)
        return self._raw_request(self.by_id.__name__, region, url, query)

    def rotations(self, region):
        """
        Returns champion rotations, including free-to-play and low-level free-to-play rotations.

        :returns: ChampionInfo
        """
        url, query = ChampionApiV3Urls.rotations(region=region)
        return self._raw_request(self.rotations.__name__, region, url, query)
