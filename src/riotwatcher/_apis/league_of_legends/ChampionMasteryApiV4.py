from .. import BaseApi, NamedEndpoint
from .urls import ChampionMasteryApiV4Urls


class ChampionMasteryApiV4(NamedEndpoint):
    """
    This class wraps the Champion-Mastery-v4 Api calls provided by the Riot API.

    See https://developer.riotgames.com/api-methods/#champion-mastery-v4/ for more
    detailed information
    """

    def __init__(self, base_api: BaseApi):
        """
        Initialize a new ChampionMasteryApiV4 which uses the provided base_api

        :param BaseApi base_api: the root API object to use for making all requests.
        """
        super().__init__(base_api, self.__class__.__name__)

    def by_puuid(self, region: str, puuid: str):
        """
        Get all champion mastery entries.

        :param string region:               the region to execute this request on
        :param string puuid:                PUUID associated with the player

        :returns: List[ChampionMasteryDTO]: This object contains a list of Champion
                                            Mastery information for player and champion
                                            combination.
        """
        return self._request_endpoint(
            self.by_puuid.__name__,
            region,
            ChampionMasteryApiV4Urls.by_puuid,
            puuid=puuid,
        )

    def by_puuid_by_champion(self, region: str, puuid: str, champion_id: int):
        """
        Get a champion mastery by player ID and champion ID.

        :param string region:         the region to execute this request on
        :param string puuid:          PUUID associated with the player
        :param long champion_id:      Champion ID to retrieve Champion Mastery for

        :returns: ChampionMasteryDTO: This object contains single Champion Mastery
                                      information for player and champion combination.
        """
        return self._request_endpoint(
            self.by_puuid_by_champion.__name__,
            region,
            ChampionMasteryApiV4Urls.by_puuid_by_champion,
            puuid=puuid,
            champion_id=champion_id,
        )

    def top_by_puuid(self, region: str, puuid: str, count: int = None):
        """
        Get specified number of top champion mastery entries sorted by number of champion
        points descending.

        :param string region:   the region to execute this request on
        :param string puuid:    PUUID associated with the player
        :param int count:       Number of entries to retrieve, defaults to 3.

        :returns: List[ChampionMasteryDto]
        """
        return self._request_endpoint(
            self.top_by_puuid.__name__,
            region,
            ChampionMasteryApiV4Urls.top_by_puuid,
            puuid=puuid,
            count=count,
        )

    def scores_by_puuid(self, region: str, puuid: str):
        """
        Get a player's total champion mastery score, which is the sum of individual
        champion mastery levels

        :param string region:   the region to execute this request on
        :param string puuid:    PUUID of the player

        :returns: int
        """
        return self._request_endpoint(
            self.scores_by_puuid.__name__,
            region,
            ChampionMasteryApiV4Urls.scores_by_puuid,
            puuid=puuid,
        )
