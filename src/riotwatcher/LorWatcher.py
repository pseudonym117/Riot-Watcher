from typing import List

from ._apis import BaseApi, LorRankedApi
from .Handlers import (
    DeprecationHandler,
    JsonifyHandler,
    RequestHandler,
    ThrowOnErrorHandler,
    TypeCorrectorHandler,
)

from .Handlers.RateLimit import RateLimitHandler


class LorWatcher:
    """
    LorWatcher class is intended to be the main interaction point with the API for Legends of Runterra.
    """

    def __init__(
        self,
        api_key: str = None,
        custom_handler_chain: List[RequestHandler] = None,
        timeout: int = None,
    ):
        """
        Initialize a new instance of the LorWatcher class.

        :param string api_key: the API key to use for this instance
        :param List[RequestHandler] custom_handler_chain:
                    RequestHandler chain to pass to the created BaseApi object.
                    This chain is called in order before any calls to the API, and called in
                    reverse order after any calls to the API.
                    If preview_request returns data, the rest of the call short circuits,
                    preventing any call to the real API and calling any handlers that have already
                    been run in reverse order.
                    This should allow for dynamic tiered caching of data.
                    If after_request returns data, that is the data that is fed to the next handler
                    in the chain.
                    Default chain is:
                        [
                            JsonifyHandler,
                            ThrowOnErrorHandler,
                            TypeCorrector,
                            RateLimitHandler,
                            DeprecationHandler
                        ]
        :param int timeout: Time to wait for a response before timing out a connection to
                            the Riot API
        """
        if not api_key:
            raise ValueError("api_key must be set!")

        if custom_handler_chain is None:
            custom_handler_chain = [
                JsonifyHandler(),
                ThrowOnErrorHandler(),
                TypeCorrectorHandler(),
                RateLimitHandler(),
                DeprecationHandler(),
            ]

        self._base_api = BaseApi(api_key, custom_handler_chain, timeout=timeout)

        self._ranked = LorRankedApi(self._base_api)

    @property
    def ranked(self) -> LorRankedApi:
        """
        Interface to the Ranked Endpoint

        :rtype: LorRankedApi
        """
        return self._ranked
