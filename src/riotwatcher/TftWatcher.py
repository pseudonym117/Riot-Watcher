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

from ._apis import BaseApi
from ._apis.team_fight_tactics import LeagueApi, MatchApi, SummonerApi


class TftWatcher:
    """
    TftWatcher class is intended to be the main interaction point with the APIs for
    Team Fight Tactics.
    """

    def __init__(
        self,
        api_key: str = None,
        timeout: int = None,
        rate_limiter: RateLimiter = BasicRateLimiter(),
        deserializer: Deserializer = DictionaryDeserializer(),
    ):
        """
        Initialize a new instance of the TftWatcher class.

        :param string api_key: the API key to use for this instance
        :param int timeout: Time to wait for a response before timing out a connection
                            to the Riot API
        :param RateLimiter rate_limiter: Instance to be used for rate limiting.
                                         This defaults to
                                         Handlers.RateLimit.BasicRateLimiter.
        :param Deserializer deserializer: Instance to be used to deserialize responses
                                          from the Riot Api. Default is
                                          Handlers.DictionaryDeserializer.
        """
        if not api_key:
            raise ValueError("api_key must be set!")

        handler_chain = [
            SanitationHandler(),
            DeserializerAdapter(deserializer),
            ThrowOnErrorHandler(),
            TypeCorrectorHandler(),
            RateLimiterAdapter(rate_limiter),
            DeprecationHandler(),
        ]

        self._base_api = BaseApi(api_key, handler_chain, timeout=timeout)

        self._league = LeagueApi(self._base_api)
        self._match = MatchApi(self._base_api)
        self._summoner = SummonerApi(self._base_api)

    @property
    def league(self) -> LeagueApi:
        """
        Interface to the League Endpoint

        :rtype: team_fight_tactics.LeagueApi
        """
        return self._league

    @property
    def match(self) -> MatchApi:
        """
        Interface to the Match Endpoint

        :rtype: team_fight_tactics.MatchApi
        """
        return self._match

    @property
    def summoner(self) -> SummonerApi:
        """
        Interface to the Summoner Endpoint

        :rtype: team_fight_tactics.SummonerApi
        """
        return self._summoner
