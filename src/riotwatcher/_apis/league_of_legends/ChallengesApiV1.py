from .. import BaseApi, NamedEndpoint
from .urls import ChallengesApiV1Urls


class ChallengesApiV1(NamedEndpoint):
    """
    This class wraps the Challenges-v1 endpoint calls provided by the Riot API.

    See https://developer.riotgames.com/api-methods/#lol-challenges-v1 for more detailed
    information
    """

    def __init__(self, base_api: BaseApi):
        """
        Initialize a new ChallengesApiV1 which uses the provided base_api.

        :param BaseApi base_api: the root API object to use for making all requests.
        """
        super().__init__(base_api, self.__class__.__name__)

    def config(self, region: str):
        """
        List of all basic challenge configuration information.

        :param string region: The region to execute this request on

        :returns: ChallengeConfigInfoDto
        """
        return self._request_endpoint(
            self.config.__name__, region, ChallengesApiV1Urls.config
        )

    def percentiles(self, region: str):
        """
        Map of level to percentile of players who have achieved it.

        :param string region: The region to execute this request on

        :returns: Map[Long, Map[Integer, Map[Level, Double]]]
        """
        return self._request_endpoint(
            self.percentiles.__name__, region, ChallengesApiV1Urls.percentiles
        )

    def challenge_config(self, region: str, challenge_id: int):
        """
        Get challenge configuration.

        :param string region:                   The region to execute this request on
        
        :param long challenge_id:               The ID of the challenge.

        :returns: ChallengeConfigInfoDto
        """
        return self._request_endpoint(
            self.challenge_config.__name__,
            region,
            ChallengesApiV1Urls.challenge_config,
            challengeId=challenge_id,
        )

    def leaderboards(self, region: str, challenge_id: int, level: str):
        """
        Return top players for each level. Level must be MASTER, GRANDMASTER or CHALLENGER.

        :param string region:                   The region to execute this request on

        :param long challenge_id:               The ID of the challenge.

        :param string level:                    The level to get the leaderboard for.

        :returns: List[ApexPlayerInfoDto]
        """
        return self._request_endpoint(
            self.leaderboards.__name__,
            region,
            ChallengesApiV1Urls.leaderboards,
            challengeId=challenge_id,
            level=level,
        )

    def percentiles_by_challenge_id(self, region: str, challenge_id: int):
        """
        Map of level to percentile of players who have achieved it.

        :param string region:                   The region to execute this request on

        :param long challenge_id:                The ID of the challenge.

        :returns: Map[Level, double]
        """
        return self._request_endpoint(
            self.percentiles_by_challenge_id.__name__,
            region,
            ChallengesApiV1Urls.percentiles_by_challenge_id,
            challengeId=challenge_id,
        )

    def by_puuid(self, region: str, puuid: str):
        """
        Returns player information with list of all progressed challenges.

        :param string region:                   The region to execute this request on

        :param string puuid:                    The puuid.

        :returns: PlayerInfoDto
        """
        return self._request_endpoint(
            self.by_puuid.__name__,
            region,
            ChallengesApiV1Urls.by_puuid,
            puuid=puuid,
        )
