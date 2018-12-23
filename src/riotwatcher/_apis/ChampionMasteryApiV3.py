from . import NamedEndpoint
from .urls import ChampionMasteryApiV3Urls


class ChampionMasteryApiV3(NamedEndpoint):
    """
    This class wraps the Champion-Mastery-v3 Api calls provided by the Riot API.

    See https://developer.riotgames.com/api-methods/#champion-mastery-v3/ for more detailed
    information
    """

    def __init__(self, http_client):
        """
        Initialize a new ChampionMasteryApiV3 which uses the provided http_client

        :param HTTPClient http_client: the root API object to use for making all requests.
        """
        super(ChampionMasteryApiV3, self).__init__(http_client, self.__class__.__name__)

    async def by_summoner(self, region, summoner_id):
        """
        Get all champion mastery entries sorted by number of champion points descending.

        :param string region: the region to execute this request on
        :param long summoner_id: Summoner ID associated with the player

        :returns: List[ChampionMasteryDTO]: This object contains a list of Champion Mastery
                                            information for player and champion combination.
        """
        url, query = ChampionMasteryApiV3Urls.by_summoner(
            region=region, summoner_id=summoner_id
        )
        return await self._raw_request(self.by_summoner.__name__, region, url, query)

    async def by_summoner_by_champion(self, region, summoner_id, champion_id):
        """
        Get a champion mastery by player ID and champion ID.

        :param string region: the region to execute this request on
        :param long summoner_id: Summoner ID associated with the player
        :param long champion_id: Champion ID to retrieve Champion Mastery for

        :returns: ChampionMasteryDTO: This object contains single Champion Mastery information for
                                      player and champion combination.
        """
        url, query = ChampionMasteryApiV3Urls.by_summoner_by_champion(
            region=region, summoner_id=summoner_id, champion_id=champion_id
        )
        return await self._raw_request(
            self.by_summoner_by_champion.__name__, region, url, query
        )

    async def scores_by_summoner(self, region, summoner_id):
        """
        Get a player's total champion mastery score, which is the sum of individual champion
        mastery levels

        :param string region: the region to execute this request on
        :param long summoner_id: Summoner ID associated with the player

        :returns: int
        """
        url, query = ChampionMasteryApiV3Urls.scored_by_summoner(
            region=region, summoner_id=summoner_id
        )
        return await self._raw_request(self.scores_by_summoner.__name__, region, url, query)
