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
from ._apis.riot import AccountApi


class RiotWatcher:
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
        self._account = AccountApi(self._base_api)

    @property
    def account(self) -> AccountApi:
        return self._account
