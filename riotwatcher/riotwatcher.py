
from ._apis import *
from .Handlers import *


class RiotWatcher:
    """
    RiotWatcher class is intended to be the main interaction point with the RiotAPI.
    """

    def __init__(self, api_key, custom_handler_chain=None):
        """
        Initialize a new instance of the RiotWatcher class.

        :param string api_key: the API key to use for this instance
        :param List[RequestHandler] custom_handler_chain:
                    RequestHandler chain to pass to the created BaseApi object.
                    This chain is called in order before any calls to the API, and called in reverse order after any
                    calls to the API.
                    If preview_request returns data, the rest of the call short circuits, preventing any call to the
                    real API and calling any handlers that have already been run in reverse order.
                    This should allow for dynamic tiered caching of data.
                    If after_request returns data, that is the data that is fed to the next handler in the chain.
                    Default chain is:
                        [
                            JsonifyHandler,
                            ThrowOnErrorHandler,
                            WaitingRateLimitHandler
                        ]
        """
        if custom_handler_chain is None:
            custom_handler_chain = [
                JsonifyHandler(),
                ThrowOnErrorHandler(),
                WaitingRateLimitHandler(),
            ]

        self._base_api = BaseApi(api_key, custom_handler_chain)

        self._champion = ChampionApiV3(self._base_api)
        self._champion_mastery = ChampionMasteryApiV3(self._base_api)
        self._league = LeagueApiV3(self._base_api)
        self._lol_status = LolStatusApiV3(self._base_api)
        self._masteries = MasteriesApiV3(self._base_api)
        self._match = MatchApiV3(self._base_api)
        self._runes = RunesApiV3(self._base_api)
        self._spectator = SpectatorApiV3(self._base_api)
        self._static_data = StaticDataApiV3(self._base_api)
        self._summoner = SummonerApiV3(self._base_api)
        # todo: tournament-stub
        # todo: tournament

    @property
    def champion_mastery(self):
        """
        Interface to the ChampionMastery Endpoint

        :rtype: ChampionMasteryApiV3
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

        :rtype: LeagueApiV3
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
    def masteries(self):
        """Interface to the Masteries Endpoint

        :rtype: MasteriesApiV3
        """
        return self._masteries

    @property
    def match(self):
        """
        Interface to the Match Endpoint

        :rtype: MatchApiV3
        """
        return self._match

    @property
    def runes(self):
        """
        Interface to the Runes Endpoint

        :rtype: RunesApiV3
        """
        return self._runes

    @property
    def spectator(self):
        """
        Interface to the Spectator Endpoint

        :rtype: SpectatorApiV3
        """
        return self._spectator

    @property
    def static_data(self):
        """
        Interface to the LoL-Static-Data Endpoint

        :rtype: StaticDataApiV3
        """
        return self._static_data

    @property
    def summoner(self):
        """
        Interface to the Summoner Endpoint

        :rtype: SummonerApiV3
        """
        return self._summoner
