from typing import Union
from .Deserializer import Deserializer
from .RateLimiter import RateLimiter

from .Handlers import (
    DeprecationHandler,
    DeserializerAdapter,
    DictionaryDeserializer,
    RateLimiterAdapter,
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
    MatchApiV4,
    SpectatorApiV4,
    SummonerApiV4,
    MatchApiV5,
    ThirdPartyCodeApiV4,
)


class LolWatcher:
    """
    LolWatcher class is intended to be the main interaction point with the APIs for League of Legends.
    """

    def __init__(
        self,
        api_key: str = None,
        timeout: int = None,
        kernel_url: str = None,
        rate_limiter: RateLimiter = BasicRateLimiter(),
        deserializer: Deserializer = DictionaryDeserializer(),
        default_match_v5: bool = False,
        default_status_v4: bool = False,
    ):
        """
        Initialize a new instance of the RiotWatcher class.

        :param string api_key: the API key to use for this instance
        :param int timeout: Time to wait for a response before timing out a connection to
                            the Riot API
        :param string kernel_url: URL for the kernel instance to connect to, instead of the API.
                                  See https://github.com/meraki-analytics/kernel for details.
        :param RateLimiter rate_limiter: Instance to be used for rate limiting.
                                         This defaults to Handlers.RateLimit.BasicRateLimiter.
                                         This parameter is not used when connecting to a
                                         kernel instance.
        :param Deserializer deserializer: Instance to be used to deserialize responses
                                          from the Riot Api. Default is Handlers.DictionaryDeserializer.
        """
        if not kernel_url and not api_key:
            raise ValueError("Either api_key or kernel_url must be set!")

        if kernel_url:
            handler_chain = [
                DeserializerAdapter(deserializer),
                ThrowOnErrorHandler(),
                TypeCorrectorHandler(),
                DeprecationHandler(),
            ]
        else:
            handler_chain = [
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
        self._match_v4 = MatchApiV4(self._base_api)
        self._match_v5 = MatchApiV5(self._base_api)
        self._spectator = SpectatorApiV4(self._base_api)
        self._summoner = SummonerApiV4(self._base_api)
        self._third_party_code = ThirdPartyCodeApiV4(self._base_api)

        self._match = self._match_v5 if default_match_v5 else self._match_v4
        self._lol_status = (
            self._lol_status_v4 if default_status_v4 else self._lol_status_v3
        )
        # todo: tournament-stub
        # todo: tournament

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
    def match(self) -> Union[MatchApiV4, MatchApiV5]:
        """
        Interface to the Match Endpoint

        :rtype: league_of_legends.MatchApiV5
        """
        return self._match

    @property
    def match_v4(self) -> MatchApiV4:
        """
        Temporary explicit interface to match-v4 endpoint.
        Will be removed when matchv4 is deprecated.

        :rtype: league_of_legends.MatchApiV4
        """
        return self._match

    @property
    def match_v5(self) -> MatchApiV5:
        """
        Temporary explicit interface to match-v5 endpoint.
        Will be removed when matchv4 is deprecated.

        :rtype: league_of_legends.MatchApiV5
        """
        return self._match_v5

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
    def third_party_code(self) -> ThirdPartyCodeApiV4:
        """
        Interface to the Third Party Code Endpoint

        :rtype: league_of_legends.ThirdPartyCodeApiV4
        """
        return self._third_party_code
