from typing import List

from .Deserializer import Deserializer
from .RateLimiter import RateLimiter

from .Handlers import (
    DeprecationHandler,
    DeserializerAdapter,
    DictionaryDeserializer,
    RateLimiterAdapter,
    RequestHandler,
    ThrowOnErrorHandler,
    TypeCorrectorHandler,
)

from .Handlers.RateLimit import BasicRateLimiter

from ._apis import BaseApi, UrlConfig
from ._apis.league_of_legends import (
    ChampionApiV3,
    ChampionMasteryApiV4,
    DataDragonApi,
    LeagueApiV4,
    LolStatusApiV3,
    MatchApiV4,
    SpectatorApiV4,
    SummonerApiV4,
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
        self._lol_status = LolStatusApiV3(self._base_api)
        self._data_dragon = DataDragonApi(self._base_api)
        self._champion_mastery = ChampionMasteryApiV4(self._base_api)
        self._league = LeagueApiV4(self._base_api)
        self._match = MatchApiV4(self._base_api)
        self._spectator = SpectatorApiV4(self._base_api)
        self._summoner = SummonerApiV4(self._base_api)
        self._third_party_code = ThirdPartyCodeApiV4(self._base_api)
        # todo: tournament-stub
        # todo: tournament

    @property
    def champion_mastery(self) -> ChampionMasteryApiV4:
        """
        Interface to the ChampionMastery Endpoint

        :rtype: ChampionMasteryApiV4
        """
        return self._champion_mastery

    @property
    def champion(self) -> ChampionApiV3:
        """
        Interface to the Champion Endpoint

        :rtype: ChampionApiV3
        """
        return self._champion

    @property
    def league(self) -> LeagueApiV4:
        """
        Interface to the League Endpoint

        :rtype: LeagueApiV4
        """
        return self._league

    @property
    def lol_status(self) -> LolStatusApiV3:
        """
        Interface to the LoLStatus Endpoint

        :rtype: LolStatusApiV3
        """
        return self._lol_status

    @property
    def match(self) -> MatchApiV4:
        """
        Interface to the Match Endpoint

        :rtype: MatchApiV4
        """
        return self._match

    @property
    def spectator(self) -> SpectatorApiV4:
        """
        Interface to the Spectator Endpoint

        :rtype: SpectatorApiV4
        """
        return self._spectator

    @property
    def data_dragon(self) -> DataDragonApi:
        """
        Interface to the DataDragon Endpoint

        :rtype: DataDragonApi
        """
        return self._data_dragon

    @property
    def summoner(self) -> SummonerApiV4:
        """
        Interface to the Summoner Endpoint

        :rtype: SummonerApiV4
        """
        return self._summoner

    @property
    def third_party_code(self) -> ThirdPartyCodeApiV4:
        """
        Interface to the Third Party Code Endpoint

        :rtype: ThirdPartyCodeApiV4
        """
        return self._third_party_code
