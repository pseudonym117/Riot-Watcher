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

from ._apis import BaseApi
from ._apis.valorant import ContentApi, MatchApi


class ValWatcher:
    def __init__(
        self,
        api_key: str,
        timeout: int = None,
        rate_limiter: RateLimiter = BasicRateLimiter(),
        deserializer: Deserializer = DictionaryDeserializer(),
    ):
        if not api_key:
            raise ValueError("api_key must be set!")

        handler_chain = [
            DeserializerAdapter(deserializer),
            ThrowOnErrorHandler(),
            TypeCorrectorHandler(),
            RateLimiterAdapter(rate_limiter),
            DeprecationHandler(),
        ]

        self._base_api = BaseApi(api_key, handler_chain, timeout=timeout)

        self._content = ContentApi(self._base_api)
        self._match = MatchApi(self._base_api)

    @property
    def content(self) -> ContentApi:
        return self._content

    @property
    def match(self) -> MatchApi:
        return self._match
