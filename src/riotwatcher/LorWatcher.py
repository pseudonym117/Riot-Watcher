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
from ._apis.legends_of_runeterra import MatchApi, RankedApi


class LorWatcher:
    """
    LorWatcher class is intended to be the main interaction point with the API for
    Legends of Runterra.
    """

    def __init__(
        self,
        api_key: str = None,
        timeout: int = None,
        rate_limiter: RateLimiter = BasicRateLimiter(),
        deserializer: Deserializer = DictionaryDeserializer(),
    ):
        """
        Initialize a new instance of the LorWatcher class.

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

        self._match = MatchApi(self._base_api)
        self._ranked = RankedApi(self._base_api)

    @property
    def match(self) -> MatchApi:
        """
        Interface to the Match Endpoint

        :rtype: legends_of_runeterra.MatchApi
        """
        return self._match

    @property
    def ranked(self) -> RankedApi:
        """
        Interface to the Ranked Endpoint

        :rtype: legends_of_runeterra.RankedApi
        """
        return self._ranked
