import logging
from typing import Union

from .Deserializer import Deserializer
from .RateLimiter import RateLimiter

from .Handlers import (
    DeprecationHandler,
    DeserializerAdapter,
    DictionaryDeserializer,
    RateLimiterAdapter,
    SanitationHandler,
    ThrowOnErrorHandler,
    TypeCorrectorHandler,
)

from .Handlers.RateLimit import BasicRateLimiter

from ._apis import BaseApi, UrlConfig
from ._apis.league_of_legends import (
    ChampionApiV3,
    ChampionMasteryApiV4,
    ClashApiV1,
    DataDragonApi,
    LeagueApiV4,
    LolStatusApiV3,
    LolStatusApiV4,
    SpectatorApiV4,
    SummonerApiV4,
    MatchApiV5,
    ChallengesApiV1,
)

LOG = logging.getLogger(__name__)


class LolWatcher:
    """
    LolWatcher class is intended to be the main interaction point with the APIs for
    League of Legends.
    """

    def __init__(
        self,
        api_key: str = None,
        timeout: int = None,
        kernel_url: str = None,
        rate_limiter: RateLimiter = BasicRateLimiter(),
        deserializer: Deserializer = DictionaryDeserializer(),
        default_status_v4: bool = False,
        **kwargs,
    ):
        """
        Initialize a new instance of the RiotWatcher class.

        :param string api_key: the API key to use for this instance
        :param int timeout: Time to wait for a response before timing out a connection
                            to the Riot API
        :param string kernel_url: URL for the kernel instance to connect to, instead of
                                  the API. See
                                  https://github.com/meraki-analytics/kernel for
                                  details.
        :param RateLimiter rate_limiter: Instance to be used for rate limiting.
                                         This defaults to
                                         Handlers.RateLimit.BasicRateLimiter.
                                         This parameter is not used when connecting to
                                         a kernel instance.
        :param Deserializer deserializer: Instance to be used to deserialize responses
                                          from the Riot Api. Default is
                                          Handlers.DictionaryDeserializer.
        """
        if not kernel_url and not api_key:
            raise ValueError("Either api_key or kernel_url must be set!")

        if kernel_url:
            handler_chain = [
                SanitationHandler(),
                DeserializerAdapter(deserializer),
                ThrowOnErrorHandler(),
                TypeCorrectorHandler(),
                DeprecationHandler(),
            ]
        else:
            handler_chain = [
                SanitationHandler(),
                DeserializerAdapter(deserializer),
                ThrowOnErrorHandler(),
                TypeCorrectorHandler(),
                RateLimiterAdapter(rate_limiter),
                DeprecationHandler(),
            ]

        if kernel_url:
            UrlConfig.root_url = kernel_url
        else:
            UrlConfig.root_url = "https://{platform}.api.riotgames.com"

        self._base_api = BaseApi(api_key, handler_chain, timeout=timeout)

        self._champion = ChampionApiV3(self._base_api)
        self._lol_status_v3 = LolStatusApiV3(self._base_api)
        self._lol_status_v4 = LolStatusApiV4(self._base_api)
        self._data_dragon = DataDragonApi(self._base_api)
        self._clash = ClashApiV1(self._base_api)
        self._champion_mastery = ChampionMasteryApiV4(self._base_api)
        self._league = LeagueApiV4(self._base_api)
        self._match = MatchApiV5(self._base_api)
        self._spectator = SpectatorApiV4(self._base_api)
        self._challenges = ChallengesApiV1(self._base_api)
        self._summoner = SummonerApiV4(self._base_api)

        self._lol_status = (
            self._lol_status_v4 if default_status_v4 else self._lol_status_v3
        )
        # todo: tournament-stub
        # todo: tournament

        if "default_match_v5" in kwargs:
            LOG.warning(
                "property 'default_match_v5' has been deprecated and can be removed"
            )

    @property
    def champion_mastery(self) -> ChampionMasteryApiV4:
        """
        Interface to the ChampionMastery Endpoint

        :rtype: league_of_legends.ChampionMasteryApiV4
        """
        return self._champion_mastery

    @property
    def champion(self) -> ChampionApiV3:
        """
        Interface to the Champion Endpoint

        :rtype: league_of_legends.ChampionApiV3
        """
        return self._champion

    @property
    def clash(self) -> ClashApiV1:
        """
        Interface to the Clash Endpoint

        :rtype: league_of_legends.ClashApiV1
        """
        return self._clash

    @property
    def league(self) -> LeagueApiV4:
        """
        Interface to the League Endpoint

        :rtype: league_of_legends.LeagueApiV4
        """
        return self._league

    @property
    def lol_status(self) -> Union[LolStatusApiV3, LolStatusApiV4]:
        """
        Interface to the LoLStatus Endpoint

        :rtype: league_of_legends.LolStatusApiV3
        """
        return self._lol_status

    @property
    def lol_status_v3(self) -> LolStatusApiV3:
        """
        Interface to the LoLStatus Endpoint

        :rtype: league_of_legends.LolStatusApiV3
        """
        return self._lol_status_v3

    @property
    def lol_status_v4(self) -> LolStatusApiV4:
        """
        Interface to the LoLStatus Endpoint

        :rtype: league_of_legends.LolStatusApiV4
        """
        return self._lol_status_v4

    @property
    def match(self) -> MatchApiV5:
        """
        Interface to the Match Endpoint

        :rtype: league_of_legends.MatchApiV5
        """
        return self._match

    @property
    def match_v4(self):
        """
        This property has been deprecated. Use 'match' property instead.
        Note that v4 is now permanently removed by Riot
        """
        raise NotImplementedError(
            "this property has been deprecated. Use 'match' property instead. Note "
            + "that v4 is now permanently removed by Riot"
        )

    @property
    def match_v5(self):
        """this property has been deprecated. Use 'match' property instead."""
        raise NotImplementedError(
            "this property has been deprecated. Use 'match' property instead."
        )

    @property
    def spectator(self) -> SpectatorApiV4:
        """
        Interface to the Spectator Endpoint

        :rtype: league_of_legends.SpectatorApiV4
        """
        return self._spectator

    @property
    def data_dragon(self) -> DataDragonApi:
        """
        Interface to the DataDragon Endpoint

        :rtype: league_of_legends.DataDragonApi
        """
        return self._data_dragon

    @property
    def summoner(self) -> SummonerApiV4:
        """
        Interface to the Summoner Endpoint

        :rtype: league_of_legends.SummonerApiV4
        """
        return self._summoner

    @property
    def third_party_code(self) -> None:
        """
        DEPRECATED: API has been removed by Riot
        """
        raise NotImplementedError(
            "API has been removed by Riot and no longer functions"
        )

    @property
    def challenges(self) -> ChallengesApiV1:
        """
        Interface to the Challenges Endpoint

        :rtype: league_of_legends.ChallengesApiV1
        """
        return self._challenges
