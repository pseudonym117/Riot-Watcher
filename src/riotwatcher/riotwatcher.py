import asyncio
import aiohttp

from ._apis import (
    BaseApi,
    DataDragonApi,
    ChampionApiV3,
    ChampionMasteryApiV3,
    LeagueApiV3,
    LolStatusApiV3,
)
from ._apis import MatchApiV3, SpectatorApiV3, SummonerApiV3, ThirdPartyCodeApiV3
from .Handlers import TypeCorrectorHandler, ThrowOnErrorHandler, JsonifyHandler
from .Handlers.RateLimit import RateLimitHandler


class RiotWatcher(object):
    def __init__(self, api_key, connector=None, loop=None,
                 early_handlers=None, late_handlers=None):
        self.api_key = api_key
        self.loop = asyncio.get_event_loop() if loop is None else loop

        self._rate_limiter = RateLimitHandler(loop=self.loop)
        early_handlers = self.default_early_handlers if not early_handlers else early_handlers
        late_handlers = self.default_late_handlers if not late_handlers else late_handlers

        self._base_api = BaseApi(
            api_key, connector=connector, loop=self.loop,
            early_handlers=early_handlers, late_handlers=late_handlers
        )
        self._champion = ChampionApiV3(self._base_api)
        self._champion_mastery = ChampionMasteryApiV3(self._base_api)
        self._league = LeagueApiV3(self._base_api)
        self._lol_status = LolStatusApiV3(self._base_api)
        self._match = MatchApiV3(self._base_api)
        self._spectator = SpectatorApiV3(self._base_api)
        self._data_dragon = DataDragonApi(self._base_api)
        self._summoner = SummonerApiV3(self._base_api)
        self._third_party_code = ThirdPartyCodeApiV3(self._base_api)
        # TODO: tournament-stub
        # TODO: tournament

    @property
    def default_early_handlers(self):
        return [
            TypeCorrectorHandler(loop=self.loop),
            self._rate_limiter
        ]
    
    @property
    def default_late_handlers(self):
        return [
            self._rate_limiter,
            ThrowOnErrorHandler(loop=self.loop),
            JsonifyHandler(loop=self.loop)
        ]

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
    def match(self):
        """
        Interface to the Match Endpoint
        :rtype: MatchApiV3
        """
        return self._match

    @property
    def spectator(self):
        """
        Interface to the Spectator Endpoint
        :rtype: SpectatorApiV3
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
        :rtype: SummonerApiV3
        """
        return self._summoner

    @property
    def third_party_code(self):
        """
        Interface to the Third Party Code Endpoint
        :rtype: ThirdPartyCodeApiV3
        """
        return self._third_party_code
