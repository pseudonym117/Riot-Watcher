
from .. import RiotWatcher as RW

from collections import deque
import logging
import time
from requests import HTTPError

# Constants
BRAZIL = 'br'
EUROPE_NORDIC_EAST = 'eune'
EUROPE_WEST = 'euw'
KOREA = 'kr'
LATIN_AMERICA_NORTH = 'lan'
LATIN_AMERICA_SOUTH = 'las'
NORTH_AMERICA = 'na1'
OCEANIA = 'oce'
RUSSIA = 'ru'
TURKEY = 'tr'
JAPAN = 'jp'

# Platforms
platforms = {
    BRAZIL: 'BR1',
    EUROPE_NORDIC_EAST: 'EUN1',
    EUROPE_WEST: 'EUW1',
    KOREA: 'KR',
    LATIN_AMERICA_NORTH: 'LA1',
    LATIN_AMERICA_SOUTH: 'LA2',
    NORTH_AMERICA: 'NA1',
    OCEANIA: 'OC1',
    RUSSIA: 'RU',
    TURKEY: 'TR1',
    JAPAN: 'JP1'
}

queue_types = [
    'CUSTOM',  # Custom games
    'NORMAL_5x5_BLIND',  # Normal 5v5 blind pick
    'BOT_5x5',  # Historical Summoners Rift coop vs AI games
    'BOT_5x5_INTRO',  # Summoners Rift Intro bots
    'BOT_5x5_BEGINNER',  # Summoner's Rift Coop vs AI Beginner Bot games
    'BOT_5x5_INTERMEDIATE',  # Historical Summoner's Rift Coop vs AI Intermediate Bot games
    'NORMAL_3x3',  # Normal 3v3 games
    'NORMAL_5x5_DRAFT',  # Normal 5v5 Draft Pick games
    'ODIN_5x5_BLIND',  # Dominion 5v5 Blind Pick games
    'ODIN_5x5_DRAFT',  # Dominion 5v5 Draft Pick games
    'BOT_ODIN_5x5',  # Dominion Coop vs AI games
    'RANKED_SOLO_5x5',  # Ranked Solo 5v5 games
    'RANKED_PREMADE_3x3',  # Ranked Premade 3v3 games
    'RANKED_PREMADE_5x5',  # Ranked Premade 5v5 games
    'RANKED_TEAM_3x3',  # Ranked Team 3v3 games
    'RANKED_TEAM_5x5',  # Ranked Team 5v5 games
    'BOT_TT_3x3',  # Twisted Treeline Coop vs AI games
    'GROUP_FINDER_5x5',  # Team Builder games
    'ARAM_5x5',  # ARAM games
    'ONEFORALL_5x5',  # One for All games
    'FIRSTBLOOD_1x1',  # Snowdown Showdown 1v1 games
    'FIRSTBLOOD_2x2',  # Snowdown Showdown 2v2 games
    'SR_6x6',  # Hexakill games
    'URF_5x5',  # Ultra Rapid Fire games
    'BOT_URF_5x5',  # Ultra Rapid Fire games played against AI games
    'NIGHTMARE_BOT_5x5_RANK1',  # Doom Bots Rank 1 games
    'NIGHTMARE_BOT_5x5_RANK2',  # Doom Bots Rank 2 games
    'NIGHTMARE_BOT_5x5_RANK5',  # Doom Bots Rank 5 games
    'ASCENSION_5x5',  # Ascension games
    'HEXAKILL',  # 6v6 games on twisted treeline
    'KING_PORO_5x5',  # King Poro game games
    'COUNTER_PICK',  # Nemesis games,
    'BILGEWATER_5x5',  # Black Market Brawlers games
]

game_maps = [
    {'map_id': 1, 'name': "Summoner's Rift", 'notes': "Summer Variant"},
    {'map_id': 2, 'name': "Summoner's Rift", 'notes': "Autumn Variant"},
    {'map_id': 3, 'name': "The Proving Grounds", 'notes': "Tutorial Map"},
    {'map_id': 4, 'name': "Twisted Treeline", 'notes': "Original Version"},
    {'map_id': 8, 'name': "The Crystal Scar", 'notes': "Dominion Map"},
    {'map_id': 10, 'name': "Twisted Treeline", 'notes': "Current Version"},
    {'map_id': 11, 'name': "Summoner's Rift", 'notes': "Current Version"},
    {'map_id': 12, 'name': "Howling Abyss", 'notes': "ARAM Map"},
    {'map_id': 14, 'name': "Butcher's Bridge", 'notes': "ARAM Map"},
]

game_modes = [
    'CLASSIC',  # Classic Summoner's Rift and Twisted Treeline games
    'ODIN',  # Dominion/Crystal Scar games
    'ARAM',  # ARAM games
    'TUTORIAL',  # Tutorial games
    'ONEFORALL',  # One for All games
    'ASCENSION',  # Ascension games
    'FIRSTBLOOD',  # Snowdown Showdown games
    'KINGPORO',  # King Poro games
]

game_types = [
    'CUSTOM_GAME',  # Custom games
    'TUTORIAL_GAME',  # Tutorial games
    'MATCHED_GAME',  # All other games
]

sub_types = [
    'NONE',  # Custom games
    'NORMAL',  # Summoner's Rift unranked games
    'NORMAL_3x3',  # Twisted Treeline unranked games
    'ODIN_UNRANKED',  # Dominion/Crystal Scar games
    'ARAM_UNRANKED_5v5',  # ARAM / Howling Abyss games
    'BOT',  # Summoner's Rift and Crystal Scar games played against AI
    'BOT_3x3',  # Twisted Treeline games played against AI
    'RANKED_SOLO_5x5',  # Summoner's Rift ranked solo queue games
    'RANKED_TEAM_3x3',  # Twisted Treeline ranked team games
    'RANKED_TEAM_5x5',  # Summoner's Rift ranked team games
    'ONEFORALL_5x5',  # One for All games
    'FIRSTBLOOD_1x1',  # Snowdown Showdown 1x1 games
    'FIRSTBLOOD_2x2',  # Snowdown Showdown 2x2 games
    'SR_6x6',  # Hexakill games
    'CAP_5x5',  # Team Builder games
    'URF',  # Ultra Rapid Fire games
    'URF_BOT',  # Ultra Rapid Fire games against AI
    'NIGHTMARE_BOT',  # Nightmare bots
    'ASCENSION',  # Ascension games
    'HEXAKILL',  # Twisted Treeline 6x6 Hexakill
    'KING_PORO',  # King Poro games
    'COUNTER_PICK',  # Nemesis games
    'BILGEWATER',  # Black Market Brawlers games
]

player_stat_summary_types = [
    'Unranked',  # Summoner's Rift unranked games
    'Unranked3x3',  # Twisted Treeline unranked games
    'OdinUnranked',  # Dominion/Crystal Scar games
    'AramUnranked5x5',  # ARAM / Howling Abyss games
    'CoopVsAI',  # Summoner's Rift and Crystal Scar games played against AI
    'CoopVsAI3x3',  # Twisted Treeline games played against AI
    'RankedSolo5x5',  # Summoner's Rift ranked solo queue games
    'RankedTeams3x3',  # Twisted Treeline ranked team games
    'RankedTeams5x5',  # Summoner's Rift ranked team games
    'OneForAll5x5',  # One for All games
    'FirstBlood1x1',  # Snowdown Showdown 1x1 games
    'FirstBlood2x2',  # Snowdown Showdown 2x2 games
    'SummonersRift6x6',  # Hexakill games
    'CAP5x5',  # Team Builder games
    'URF',  # Ultra Rapid Fire games
    'URFBots',  # Ultra Rapid Fire games played against AI
    'NightmareBot',  # Summoner's Rift games played against Nightmare AI
    'Hexakill',  # Twisted Treeline 6x6 Hexakill games
    'KingPoro',  # King Poro games
    'CounterPick',  # Nemesis games
    'Bilgewater',  # Black Market Brawlers games
]

solo_queue, ranked_5s, ranked_3s = 'RANKED_SOLO_5x5', 'RANKED_TEAM_5x5', 'RANKED_TEAM_3x3'

preseason_3, season_3, preseason_2014, season_2014, preseason_2015, season_2015, preseason_2016, season_2016 = [
    'PRESEASON3', 'SEASON3',
    'PRESEASON2014', 'SEASON2014',
    'PRESEASON2015', 'SEASON2015',
    'PRESEASON2016', 'SEASON2016',
]

api_versions = {
    'champion': 1.2,
    'current-game': 1.0,
    'featured-games': 1.0,
    'game': 1.3,
    'league': 2.5,
    'lol-static-data': 1.2,
    'lol-status': 1.0,
    'match': 2.2,
    'matchlist': 2.2,
    'summoner': 1.4,
}


class LoLException(Exception):
    def __init__(self, error, response):
        self.error = error
        self.headers = response.headers

    def __str__(self):
        return self.error

    def __eq__(self, other):
        if isinstance(other, "".__class__):
            return self.error == other
        elif isinstance(other, self.__class__):
            return self.error == other.error and self.headers == other.headers
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return super(LoLException).__hash__()


error_400 = "Bad request"
error_401 = "Unauthorized"
error_403 = "Blacklisted key"
error_404 = "Game data not found"
error_429 = "Too many requests"
error_500 = "Internal server error"
error_503 = "Service unavailable"
error_504 = 'Gateway timeout'


def raise_status(response):
    if response.status_code == 400:
        raise LoLException(error_400, response)
    elif response.status_code == 401:
        raise LoLException(error_401, response)
    elif response.status_code == 403:
        raise LoLException(error_403, response)
    elif response.status_code == 404:
        raise LoLException(error_404, response)
    elif response.status_code == 429:
        raise LoLException(error_429, response)
    elif response.status_code == 500:
        raise LoLException(error_500, response)
    elif response.status_code == 503:
        raise LoLException(error_503, response)
    elif response.status_code == 504:
        raise LoLException(error_504, response)
    else:
        response.raise_for_status()


class RateLimit:
    def __init__(self, allowed_requests, seconds):
        self.allowed_requests = allowed_requests
        self.seconds = seconds
        self.made_requests = deque()

    def __reload(self):
        t = time.time()
        while len(self.made_requests) > 0 and self.made_requests[0] < t:
            self.made_requests.popleft()

    def add_request(self):
        self.made_requests.append(time.time() + self.seconds)

    def request_available(self):
        self.__reload()
        return len(self.made_requests) < self.allowed_requests


class RiotWatcher:
    def __init__(self, key, default_region=NORTH_AMERICA, limits=None):
        logging.warn('legacy RiotWatcher class is not intended to be used long term')
        logging.warn('please update to RiotWatcher v2.0.0 APIs as soon as possible')
        self.key = key
        self._watcher = RW(key)
        self.default_region = default_region

    def can_make_request(self):
        return True

    def base_request(self, url, region, static=False, **kwargs):
        raise NotImplementedError()

    @staticmethod
    def sanitized_name(name):
        return name.replace(' ', '').lower()

    # champion-v1.2
    def get_all_champions(self, region=None, free_to_play=False):
        if region is None:
            region = self.default_region
        return self._watcher.champion.all(region, free_to_play=free_to_play)

    def get_champion(self, champion_id, region=None):
        if region is None:
            region = self.default_region
        return self._watcher.champion.by_id(region, champion_id)

    # current-game-v1.0
    def get_current_game(self, summoner_id, platform_id=None, region=None):
        if region is None:
            region = self.default_region
        return self._watcher.spectator.by_summoner(region, summoner_id)

    # featured-game-v1.0
    def get_featured_games(self, proxy=None):
        if proxy is None:
            proxy = self.default_region
        return self._watcher.spectator.featured_games(proxy)

    # game-v1.3
    def get_recent_games(self, summoner_id, region=None):
        if region is None:
            region = self.default_region
        summoner = self._watcher.summoner.by_id(region, summoner_id)
        return self._watcher.match.matchlist_by_account_recent(region, summoner['accountId'])

    # league-v2.5
    def get_league(self, summoner_ids=None, team_ids=None, region=None):
        """summoner_ids and team_ids arguments must be iterable, only one should be specified, not both"""
        if summoner_ids is not None:
            if region is None:
                region = self.default_region
            return [
                self._watcher.league.by_summoner(region, summoner_id)
                for summoner_id in summoner_ids
            ]
        raise NotImplementedError()

    def get_league_entry(self, summoner_ids=None, team_ids=None, region=None):
        """summoner_ids and team_ids arguments must be iterable, only one should be specified, not both"""
        return self.get_league(summoner_ids=summoner_ids, region=region)

    def get_challenger(self, region=None, queue=solo_queue):
        if region is None:
            region = self.default_region
        return self._watcher.league.challenger_by_queue(region, queue)

    def get_master(self, region=None, queue=solo_queue):
        if region is None:
            region = self.default_region
        return self._watcher.league.masters_by_queue(region, queue)

    # lol-static-data-v1.2
    def static_get_champion_list(self, region=None, locale=None, version=None, data_by_id=None, champ_data=None):
        if region is None:
            region = self.default_region
        return self._watcher.static_data.champions(
            region,
            locale=locale,
            version=version,
            data_by_id=data_by_id,
            tags=champ_data
        )

    def static_get_champion(self, champ_id, region=None, locale=None, version=None, champ_data=None):
        if region is None:
            region = self.default_region
        return self._watcher.static_data.champion(
            region,
            champ_id,
            locale=locale,
            version=version,
            tags=champ_data
        )

    def static_get_item_list(self, region=None, locale=None, version=None, item_list_data=None):
        if region is None:
            region = self.default_region
        return self._watcher.static_data.items(
            region,
            locale=locale,
            version=version,
            tags=item_list_data
        )

    def static_get_item(self, item_id, region=None, locale=None, version=None, item_data=None):
        if region is None:
            region = self.default_region
        return self._watcher.static_data.item(
            region,
            item_id,
            locale=locale,
            version=version,
            tags=item_data
        )

    def static_get_mastery_list(self, region=None, locale=None, version=None, mastery_list_data=None):
        if region is None:
            region = self.default_region
        return self._watcher.static_data.masteries(
            region,
            locale=locale,
            version=version,
            tags=mastery_list_data
        )

    def static_get_mastery(self, mastery_id, region=None, locale=None, version=None, mastery_data=None):
        if region is None:
            region = self.default_region
        return self._watcher.static_data.mastery(
            region,
            mastery_id,
            locale=locale,
            version=version,
            tags=mastery_data
        )

    def static_get_realm(self, region=None):
        if region is None:
            region = self.default_region
        return self._watcher.static_data.realms(region)

    def static_get_rune_list(self, region=None, locale=None, version=None, rune_list_data=None):
        if region is None:
            region = self.default_region
        return self._watcher.static_data.runes(
            region,
            locale=locale,
            version=version,
            tags=rune_list_data
        )

    def static_get_rune(self, rune_id, region=None, locale=None, version=None, rune_data=None):
        if region is None:
            region = self.default_region
        return self._watcher.static_data.rune(
            region,
            rune_id,
            locale=locale,
            version=version,
            tags=rune_data
        )

    def static_get_summoner_spell_list(self, region=None, locale=None, version=None, data_by_id=None, spell_data=None):
        if region is None:
            region = self.default_region
        return self._watcher.static_data.summoner_spells(
            region,
            locale=locale,
            version=version,
            data_by_id=data_by_id,
            tags=spell_data
        )

    def static_get_summoner_spell(self, spell_id, region=None, locale=None, version=None, spell_data=None):
        if region is None:
            region = self.default_region
        return self._watcher.static_data.summoner_spell(
            region,
            spell_id,
            locale=locale,
            version=version,
            tags=spell_data
        )

    def static_get_versions(self, region=None):
        if region is None:
            region = self.default_region
        return self._watcher.static_data.versions(region)

    # match-v2.2
    def get_match(self, match_id, region=None, include_timeline=False):
        if region is None:
            region = self.default_region
        match = self._watcher.match.by_id(region, match_id)

        if include_timeline:
            try:
                match['timeline'] = self._watcher.match.timeline_by_match(region, match_id)
            except HTTPError as err:
                if err.response.status_code != 404:
                    raise

        return match

    # lol-status-v1.0
    def get_server_status(self, region=None):
        if region is None:
            region = self.default_region
        return self._watcher.lol_status.shard_data(region)

    # match list-v2.2
    def get_match_list(
            self,
            summoner_id,
            region=None,
            champion_ids=None,
            ranked_queues=None,
            season=None,
            begin_time=None,
            end_time=None,
            begin_index=None,
            end_index=None):
        if region is None:
            region = self.default_region

        account = self._watcher.summoner.by_id(region, summoner_id)['accountId']

        return self._watcher.match.matchlist_by_account(
            region,
            account,
            queue=ranked_queues,
            begin_time=begin_time,
            end_time=end_time,
            begin_index=begin_index,
            end_index=end_index,
            season=season,
            champion=champion_ids
        )

    # summoner-v1.4
    def get_mastery_pages(self, summoner_ids, region=None):
        if region is None:
            region = self.default_region

        return [
            self._watcher.masteries.by_summoner(region, summoner_id)
            for summoner_id in summoner_ids
        ]

    def get_rune_pages(self, summoner_ids, region=None):
        if region is None:
            region = self.default_region

        return [
            self._watcher.runes.by_summoner(region, summoner_id)
            for summoner_id in summoner_ids
        ]

    def get_summoners(self, names=None, ids=None, region=None):
        if region is None:
            region = self.default_region

        if names is not None:
            return [
                self._watcher.summoner.by_name(region, name)
                for name in names
            ]
        if ids is not None:
            return [
                self._watcher.summoner.by_id(region, _id)
                for _id in ids
            ]
        raise NotImplementedError()

    def get_summoner(self, name=None, _id=None, region=None):
        if region is None:
            region = self.default_region
        if name is not None:
            return self._watcher.summoner.by_name(region, name)
        if _id is not None:
            return self._watcher.summoner.by_id(region, _id)
        raise NotImplementedError()

    def get_summoner_name(self, summoner_ids, region=None):
        if region is None:
            region = self.default_region

        return {
            sid: name
            for sid, name in zip(
                summoner_ids,
                [
                    self._watcher.summoner.by_id(region, _id)['name']
                    for _id in summoner_ids
                ]
            )
        }
