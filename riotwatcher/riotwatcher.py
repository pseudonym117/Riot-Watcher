
from ._apis import *
from .Handlers import *

class RiotWatcher:
    def __init__(self, api_key, custom_handler_chain=None):
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
        return self._champion_mastery

    @property
    def champion(self):
        return self._champion

    @property
    def league(self):
        return self._league

    @property
    def lol_status(self):
        return self._lol_status

    @property
    def masteries(self):
        return self._masteries

    @property
    def match(self):
        return self._match

    @property
    def runes(self):
        return self._runes

    @property
    def spectator(self):
        return self._spectator

    @property
    def static_data(self):
        return self._static_data

    @property
    def summoner(self):
        return self._summoner
