from typing import List

from .Handlers import (
    DeprecationHandler,
    JsonifyHandler,
    RequestHandler,
    ThrowOnErrorHandler,
    TypeCorrectorHandler,
)

from .Handlers.RateLimit import RateLimitHandler

from ._apis import BaseApi
from ._apis.team_fight_tactics import TftLeagueApi, TftMatchApi, TftSummonerApi


class TftWatcher:
    """
    TftWatcher class is intended to be the main interaction point with the APIs for Team Fight Tactics.
    """

    def __init__(
        self,
        api_key: str = None,
        custom_handler_chain: List[RequestHandler] = None,
        timeout: int = None,
    ):
        """
        Initialize a new instance of the TftWatcher class.

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

        self._league = TftLeagueApi(self._base_api)
        self._match = TftMatchApi(self._base_api)
        self._summoner = TftSummonerApi(self._base_api)

    @property
    def league(self) -> TftLeagueApi:
        """
        Interface to the League Endpoint

        :rtype: TftLeagueApi
        """
        return self._league

    @property
    def match(self) -> TftMatchApi:
        """
        Interface to the Match Endpoint

        :rtype: TftMatchApi
        """
        return self._match

    @property
    def summoner(self) -> TftSummonerApi:
        """
        Interface to the Summoner Endpoint

        :rtype: TftSummonerApi
        """
        return self._summoner
