
from . import NamedEndpoint


class ChampionMasteryApiV3(NamedEndpoint):
    """
    This class wraps the Champion-Mastery-v3 Api calls provided by the Riot API.
    See https://developer.riotgames.com/api-methods/#champion-mastery-v3/ for more detailed information
    """
    def __init__(self, base_api):
        """
        Initialize a new ChampionMasteryApiV3 which uses the provided base_api

        :param BaseApi base_api: the root API object to use for making all requests.
        """
        super(ChampionMasteryApiV3, self).__init__(base_api, self.__class__.__name__)

    def by_summoner(self, region, summoner_id):
        """
        Get all champion mastery entries sorted by number of champion points descending.

        :param string region: the region to execute this request on
        :param long summoner_id: Summoner ID associated with the player

        :returns: List[ChampionMasteryDTO]: This object contains a list of Champion Mastery information for player
                                            and champion combination.
        """
        return self._request(
            self.by_summoner.__name__,
            region,
            '/lol/champion-mastery/v3/champion-masteries/by-summoner/{summonerId}'.format(summonerId=summoner_id)
        )

    def by_summoner_by_champion(self, region, summoner_id, champion_id):
        """
        Get a champion mastery by player ID and champion ID.

        :param string region: the region to execute this request on
        :param long summoner_id: Summoner ID associated with the player
        :param long champion_id: Champion ID to retrieve Champion Mastery for

        :returns: ChampionMasteryDTO: This object contains single Champion Mastery information for player
                                      and champion combination.
        """
        return self._request(
            self.by_summoner_by_champion.__name__,
            region,
            '/lol/champion-mastery/v3/champion-masteries/by-summoner/{summonerId}/by-champion/{championId}'.format(
                summonerId=summoner_id,
                championId=champion_id
            )
        )

    def scores_by_summoner(self, region, summoner_id):
        """
        Get a player's total champion mastery score, which is the sum of individual champion mastery levels

        :param string region: the region to execute this request on
        :param long summoner_id: Summoner ID associated with the player

        :returns: int
        """
        return self._request(
            self.scores_by_summoner.__name__,
            region,
            '/lol/champion-mastery/v3/scores/by-summoner/{summonerId}'.format(summonerId=summoner_id)
        )
