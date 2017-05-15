
from BaseApi import BaseApi

from ChampionMasteryApiV3 import ChampionMasteryApiV3
from ChampionApiV3 import ChampionApiV3
from LeagueStatusApiV3 import LeagueStatusApiV3
from LolStatusApiV3 import LolStatusApiV3
from MasteriesApiV3 import MasteriesApiV3
from MatchApiV3 import MatchApiV3
from RunesApiV3 import RunesApiV3
from SpectatorApiV3 import SpectatorApiV3
from StaticDataApiV3 import StaticDataApiV3
from SummonerApiV3 import SummonerApiV3


class RiotWatcher:
    def __init__(self, api_key):
        self._base_api = BaseApi(api_key)

        self._champion_mastery = ChampionMasteryApiV3(self._base_api)
        self._champion = ChampionApiV3(self._base_api)
        self._league = LeagueStatusApiV3(self._base_api)
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
