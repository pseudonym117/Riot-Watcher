from ._apis import BaseApi, DataDragonApi, ChampionApiV3, LolStatusApiV3
from ._apis import (
    ChampionMasteryApiV4,
    LeagueApiV4,
    MatchApiV4,
    SpectatorApiV4,
    SummonerApiV4,
    ThirdPartyCodeApiV4,
)
from .Handlers import (
    DeprecationHandler,
    JsonifyHandler,
    ThrowOnErrorHandler,
    TypeCorrectorHandler,
)

from .Handlers.RateLimit import RateLimitHandler

from ._apis.urls import UrlConfig


class RiotWatcher(object):
    """
    RiotWatcher class is intended to be the main interaction point with the RiotAPI.
    """

    def __init__(
        self, api_key=None, custom_handler_chain=None, timeout=None, kernel_url=None
    ):
        """
        Initialize a new instance of the RiotWatcher class.

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
        :param string kernel_url: URL for the kernel instance to connect to, instead of the API.
                                  See https://github.com/meraki-analytics/kernel for details.
        """
        if not kernel_url and not api_key:
            raise ValueError("Either api_key or kernel_url must be set!")

        if custom_handler_chain is None:
            if kernel_url:
                custom_handler_chain = [
                    JsonifyHandler(),
                    ThrowOnErrorHandler(),
                    TypeCorrectorHandler(),
                    DeprecationHandler(),
                ]
            else:
                custom_handler_chain = [
                    JsonifyHandler(),
                    ThrowOnErrorHandler(),
                    TypeCorrectorHandler(),
                    RateLimitHandler(),
                    DeprecationHandler(),
                ]

        if kernel_url:
            UrlConfig.root_url = kernel_url
        else:
            UrlConfig.root_url = "https://{platform}.api.riotgames.com"

        self._base_api = BaseApi(api_key, custom_handler_chain, timeout=timeout)

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
    def champion_mastery(self):
        """
        Interface to the ChampionMastery Endpoint

        :rtype: ChampionMasteryApiV4
        """
        return self._champion_mastery

    @property
    def champion(self):
        """
        Interface to the Champion Endpoint

        :rtype: ChampionApiV3
        """
        return self._champion

    @property
    def league(self):
        """
        Interface to the League Endpoint

        :rtype: LeagueApiV4
        """
        return self._league

    @property
    def lol_status(self):
        """
        Interface to the LoLStatus Endpoint

        :rtype: LolStatusApiV3
        """
        return self._lol_status

    @property
    def match(self):
        """
        Interface to the Match Endpoint

        :rtype: MatchApiV4
        """
        return self._match

    @property
    def spectator(self):
        """
        Interface to the Spectator Endpoint

        :rtype: SpectatorApiV4
        """
        return self._spectator

    @property
    def data_dragon(self):
        """
        Interface to the DataDragon Endpoint

        :rtype: DataDragonApi
        """
        return self._data_dragon

    @property
    def summoner(self):
        """
        Interface to the Summoner Endpoint

        :rtype: SummonerApiV4
        """
        return self._summoner

    @property
    def third_party_code(self):
        """
        Interface to the Third Party Code Endpoint

        :rtype: ThirdPartyCodeApiV4
        """
        return self._third_party_code
