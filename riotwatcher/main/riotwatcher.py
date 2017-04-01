from collections import deque
import time
import requests
from pprint import pprint

# Constants
BRAZIL = 'br'
EUROPE_NORDIC_EAST = 'eune'
EUROPE_WEST = 'euw'
KOREA = 'kr'
LATIN_AMERICA_NORTH = 'lan'
LATIN_AMERICA_SOUTH = 'las'
NORTH_AMERICA = 'na'
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
    'stats': 1.3,
    'summoner': 1.4
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

d_error_code_msg_s = {
    400: "Bad request",
    401: "Unauthorized",
    403: "Blacklisted or invalid key",
    404: "Game data not found",
    429: "Too many requests",
    500: "Internal server error",
    503: "Service unavailable",
    504: 'Gateway timeout',
}


def raise_status(response):
    # Check if there exists an error message corresponding to the status code
    # If not the exception KeyError is raised then caught
    # and the response.raise_for_status method is called
    try:
        s_error_msg = d_error_code_msg_s[response.status_code]
        raise LoLException(s_error_msg, response)
    except KeyError:
        response.raise_for_status()

    # if response.status_code == 400:
    #     raise LoLException(error_400, response)
    #
    #
    #
    # elif response.status_code == 401:
    #     raise LoLException(error_401, response)
    # elif response.status_code == 403:
    #     raise LoLException(error_403, response)
    # elif response.status_code == 404:
    #     raise LoLException(error_404, response)
    # elif response.status_code == 429:
    #     raise LoLException(error_429, response)
    # elif response.status_code == 500:
    #     raise LoLException(error_500, response)
    # elif response.status_code == 503:
    #     raise LoLException(error_503, response)
    # elif response.status_code == 504:
    #     raise LoLException(error_504, response)
    # else:
    #     response.raise_for_status()


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
#
# class RiotAPIRequest:
#
#     def __init__(self, p_api_key, url, region, ):


class RiotWatcher:
    def __init__(self, key, default_region=EUROPE_WEST, limits=(RateLimit(10, 10), RateLimit(500, 600), )):
        self.key = key  #If you have a production key, use limits=(RateLimit(3000,10), RateLimit(180000,600),)
        self.default_region = default_region
        self.limits = limits

    def _wait(call):
        """
        Decorator that aims to check if the current RiotWatcher can do requests.

        :param func:
        :return:
        """
        def wrapper(*args, **kwargs):
            watcher = args[0]
            print(call, args)
            # loop until watcher's limit has been refreshed
            while not watcher.can_make_request():
                time.sleep(1)
            return call(*args, **kwargs)
        return wrapper

    def can_make_request(self):
        for lim in self.limits:
            if not lim.request_available():
                return False
        return True

    @staticmethod
    def sanitized_name(name):
        return name.replace(' ', '').lower()

    # lol-status-v1.0
    @staticmethod
    def get_server_status(region=None):
        if region is None:
            url = 'shards'
        else:
            url = 'shards/{region}'.format(region=region)
        r = requests.get('http://status.leagueoflegends.com/{url}'.format(url=url))
        raise_status(r)
        return r.json()

#################################################################################################"

    @_wait
    def _observer_mode_request(self, url, proxy=None, **kwargs):
        if proxy is None:
            proxy = self.default_region
        args = {'api_key': self.key}
        for k in kwargs:
            if kwargs[k] is not None:
                args[k] = kwargs[k]
        r = requests.get(
            'https://{proxy}.api.pvp.net/observer-mode/rest/{url}'.format(
                proxy=proxy,
                url=url
            ),
            params=args
        )
        for lim in self.limits:
            lim.add_request()
        raise_status(r)
        return r.json()

    @_wait
    def base_request(self, url, region, static=False, **kwargs):
        if region is None:
            region = self.default_region
        args = {'api_key': self.key}
        for k in kwargs:
            if kwargs[k] is not None:
                args[k] = kwargs[k]

        final_url ='https://{proxy}.api.pvp.net/api/lol/{static}{region}/{url}'.format(
                proxy='global' if static else region,
                static='static-data/' if static else '',
                region=region,
                url=url
            )
        r = requests.get(final_url,
            params=args
        )
        if not static:
            for lim in self.limits:
                lim.add_request()
        raise_status(r)
        return r.json()

    # Requests
    def _category_base_request(self, category, end_url, region, **kwargs):
        d_categories = {
            'lol-static-data': "/",
            "game": "/game/",
            "league": "/league/",
            "matchlist": "/matchlist/",
            "match": "/match/",
            "stats": "/stats/",
            "summoner": "/summoner/"
        }
        if category not in d_categories:
            raise Exception("Category %s not in l_categories" % category)

        return self.base_request(
            'v{version}{category}{end_url}'.format(
                version=api_versions[category],
                end_url=end_url,
                category=d_categories[category]
            ),
            region,
            **kwargs
        )

    # lol-static-data-v1.2
    def _static_request(self, end_url, region, **kwargs):
        return self._category_base_request(category='lol-static-data',
                                            end_url='{end_url}'.format(
                                                      end_url=end_url
                                            ),
                                            region=region,
                                            static=True,
                                            **kwargs
                                            )

######################################################################################################

    # summoner related
    # current-game-v1.0
    def get_current_game(self, summoner_id, platform_id=None, region=None):
        if platform_id is None:
            platform_id = platforms[self.default_region]
        return self._observer_mode_request(
            'consumer/getSpectatorGameInfo/{platform}/{summoner_id}'.format(
                platform=platform_id,
                summoner_id=summoner_id
            ),
            region
        )
    # todo

    def get_match_list(self, summoner_id, region=None, champion_ids=None, ranked_queues=None, season=None,
                       begin_time=None, end_time=None, begin_index=None, end_index=None):
        if ranked_queues is not None and not isinstance(ranked_queues, str) :
            ranked_queues = ','.join(ranked_queues)
        if season is not None and not isinstance(season, str):
            season = ','.join(season)

        return self._category_base_request(category='matchlist',
                                            end_url='by-summoner/{summoner_id}'.format(summoner_id=summoner_id),
                                            region=region,
                                            championIds=champion_ids,
                                            rankedQueues=ranked_queues,
                                            seasons=season,
                                            beginTime=begin_time,
                                            endTime=end_time,
                                            beginIndex=begin_index,
                                            endIndex=end_index
        )

    def get_stat_summary(self, summoner_id, region=None, season=None):
        return self._category_base_request(category='stats',
                                           end_url='by-summoner/{summoner_id}/summary'.format(summoner_id=summoner_id),
                                           region=region,
                                           season='SEASON{}'.format(season) if season is not None else None)

    def get_ranked_stats(self, summoner_id, region=None, season=None):
        return self._category_base_request(category='stats',
                                           end_url='by-summoner/{summoner_id}/ranked'.format(summoner_id=summoner_id),
                                           region=region,
                                           season='SEASON{}'.format(season) if season is not None else None
                                           )

    def get_mastery_pages(self, summoner_ids, region=None):
        return self._category_base_request(category='summoner',
                                           end_url='{summoner_ids}/masteries'.format(summoner_ids=','.join([str(s) for s in summoner_ids])),
                                           region=region
        )

    def get_rune_pages(self, summoner_ids, region=None):
        return self._category_base_request(category='summoner',
                                           end_url='{summoner_ids}/runes'.format(summoner_ids=','.join([str(s) for s in summoner_ids])),
                                           region=region
        )

    def get_league(self, summoner_ids=None, region=None):
        """summoner_ids and team_ids arguments must be iterable, only one should be specified, not both"""
        # todo wtf is this shit?

        if summoner_ids is None:
            return self._category_base_request(category="league",
                                               end_url='by-summoner/{summoner_ids}'.format(summoner_ids=','.join([str(s) for s in summoner_ids])),
                                               region=region)

    def get_league_entry(self, summoner_ids=None, region=None):
        """summoner_ids and team_ids arguments must be iterable, only one should be specified, not both"""
        if summoner_ids is None:
            return self._category_base_request(category="league",
                                               end_url='by-summoner/{summoner_ids}/entry'.format(summoner_ids=','.join([str(s) for s in summoner_ids])),
                                               region=region)

    def get_recent_games(self, summoner_id, region=None):
        return self._category_base_request(category='game',
                                           end_url='by-summoner/{summoner_id}/recent'.format(summoner_id=summoner_id),
                                           region=region)

    def get_summoner_name(self, summoner_ids, region=None):
        return self._category_base_request(category='summoner',
                                           end_url='{summoner_ids}/name'.format(summoner_ids=','.join([str(s) for s in summoner_ids])),
                                           region=region
                                           )

# League related

    def get_challenger(self, region=None, queue=solo_queue):
        return self._category_base_request(category='league',
                                           end_url='challenger',
                                           region=region,
                                           type=queue
                                           )

    def get_master(self, region=None, queue=solo_queue):
        return self._category_base_request(category='league',
                                           end_url='master',
                                           region=region,
                                           type=queue
                                           )

    def get_match(self, match_id, region=None, include_timeline=False):
        return self._category_base_request(category='match',
                                           end_url='{match_id}'.format(match_id=match_id),
                                           region=region,
                                           includeTimeline=include_timeline
                                           )

    def get_summoners(self, names=None, ids=None, region=None):
        # todo je pense qu'on peut mieux faire iici, avec un elif
        if (names is None) != (ids is None):
            if names is not None:
                end_url = 'by-name/{summoner_names}'.format(summoner_names=','.join([self.sanitized_name(n) for n in names]))
            else:
                end_url = '{summoner_ids}'.format(summoner_ids=','.join([str(i) for i in ids]))
            return self._category_base_request(category='summoner',
                                               end_url=end_url,
                                               region=region)
        else:
            return None


# todo complicado

    def get_summoner(self, name=None, _id=None, region=None):
        if (name is None) != (_id is None):
            if name is not None:
                name = self.sanitized_name(name)
                key, summoner = self.get_summoners(names=[name, ], region=region).popitem()
                return summoner
            else:
                return self.get_summoners(ids=[_id, ], region=region)[str(_id)]
        return None

    def get_featured_games(self, proxy=None):
        return self._observer_mode_request('featured', proxy)

    # todo static class for static functions
    def static_get_champion_list(self, region=None, locale=None, version=None, data_by_id=None, champ_data=None):
        return self._static_request(
            'champion',
            region,
            locale=locale,
            version=version,
            dataById=data_by_id,
            champData=champ_data
        )

    def static_get_champion(self, champ_id, region=None, locale=None, version=None, champ_data=None):
        return self._static_request(
            'champion/{id}'.format(id=champ_id),
            region,
            locale=locale,
            version=version,
            champData=champ_data
        )

    def static_get_item_list(self, region=None, locale=None, version=None, item_list_data=None):
        return self._static_request('item', region, locale=locale, version=version, itemListData=item_list_data)

    def static_get_item(self, item_id, region=None, locale=None, version=None, item_data=None):
        return self._static_request(
            'item/{id}'.format(id=item_id),
            region,
            locale=locale,
            version=version,
            itemData=item_data
        )

    def static_get_mastery_list(self, region=None, locale=None, version=None, mastery_list_data=None):
        return self._static_request(
            'mastery',
            region,
            locale=locale,
            version=version,
            masteryListData=mastery_list_data
        )

    def static_get_mastery(self, mastery_id, region=None, locale=None, version=None, mastery_data=None):
        return self._static_request(
            'mastery/{id}'.format(id=mastery_id),
            region,
            locale=locale,
            version=version,
            masteryData=mastery_data
        )

    def static_get_realm(self, region=None):
        return self._static_request('realm', region)

    def static_get_rune_list(self, region=None, locale=None, version=None, rune_list_data=None):
        return self._static_request('rune', region, locale=locale, version=version, runeListData=rune_list_data)

    def static_get_rune(self, rune_id, region=None, locale=None, version=None, rune_data=None):
        return self._static_request(
            'rune/{id}'.format(id=rune_id),
            region,
            locale=locale,
            version=version,
            runeData=rune_data
        )

    def static_get_summoner_spell_list(self, region=None, locale=None, version=None, data_by_id=None, spell_data=None):
        return self._static_request(
            'summoner-spell',
            region,
            locale=locale,
            version=version,
            dataById=data_by_id,
            spellData=spell_data
        )

    def static_get_summoner_spell(self, spell_id, region=None, locale=None, version=None, spell_data=None):
        return self._static_request(
            'summoner-spell/{id}'.format(id=spell_id),
            region,
            locale=locale,
            version=version,
            spellData=spell_data
        )

    def static_get_versions(self, region=None):
        return self._static_request('versions', region)
