from threading import Timer
import requests

# Constants
NORTH_AMERICA = 'na'
EUROPE_WEST = 'euw'
EUROPE_NORDIC_EAST = 'eune'
BRAZIL = 'br'
LATIN_AMERICA_NORTH = 'lan'
LATIN_AMERICA_SOUTH = 'las'
KOREA = 'kr'

game_maps = [
	{'map_id': 1, 'name': "Summoner's Rift", 'notes': "Summer Variant"},
	{'map_id': 2, 'name': "Summoner's Rift", 'notes': "Autumn Variant"},
	{'map_id': 3, 'name': "The Proving Grounds", 'notes': "Tutorial Map"},
	{'map_id': 4, 'name': "Twisted Treeline", 'notes': "Original Version"},
	{'map_id': 8, 'name': "The Crystal Scar", 'notes': "Dominion Map"},
	{'map_id': 10, 'name': "Twisted Treeline", 'notes': "Current Version"},
	{'map_id': 12, 'name': "Howling Abyss", 'notes': "ARAM Map"},
]

game_modes = [
	'CLASSIC',				# Classic Summoner's Rift and Twisted Treeline games
	'ODIN',					# Dominion/Crystal Scar games
	'ARAM',					# ARAM games
	'TUTORIAL',				# Tutorial games
	'ONEFORALL',			# One for All games
	'FIRSTBLOOD',			# Snowdown Showdown games
]

game_types = [
	'CUSTOM_GAME',				# Custom games
	'TUTORIAL_GAME',			# Tutorial games
	'MATCHED_GAME',				# All other games
]

sub_types = [
	'NONE',						# Custom games
	'NORMAL',					# Summoner's Rift unranked games
	'NORMAL_3x3',				# Twisted Treeline unranked games
	'ODIN_UNRANKED',			# Dominion/Crystal Scar games
	'ARAM_UNRANKED_5v5',		# ARAM / Howling Abyss games
	'BOT',						# Summoner's Rift and Crystal Scar games played against AI
	'BOT_3x3',					# Twisted Treeline games played against AI
	'RANKED_SOLO_5x5',			# Summoner's Rift ranked solo queue games
	'RANKED_TEAM_3x3',			# Twisted Treeline ranked team games
	'RANKED_TEAM_5x5',			# Summoner's Rift ranked team games
	'ONEFORALL_5x5',			# One for All games
	'FIRSTBLOOD_1x1',			# Snowdown Showdown 1x1 games
	'FIRSTBLOOD_2x2',			# Snowdown Showdown 2x2 games
]

solo_queue, ranked_5s, ranked_3s = 'RANKED_SOLO_5x5', 'RANKED_TEAM_5x5', 'RANKED_TEAM_3x3'


class LoLException(Exception):
	def __init__(self, error):
		self.error = error

	def __str__(self):
		return self.error


error_400 = LoLException("Bad request")
error_401 = LoLException("Unauthorized")
error_404 = LoLException("Game data not found")
error_429 = LoLException("Too many requests")
error_500 = LoLException("Internal server error")
error_503 = LoLException("Service unavailable")


def raise_status(response):
	if response.status_code == 400:
		raise error_400
	elif response.status_code == 401:
		raise error_401
	elif response.status_code == 404:
		raise error_404
	elif response.status_code == 429:
		raise error_429
	elif response.status_code == 500:
		raise error_500
	elif response.status_code == 503:
		raise error_503
	else:
		response.raise_for_status()


class RiotWatcher:
	def __init__(self, key, default_region=NORTH_AMERICA, requests_per_10s=10, requests_per_10m=500):
		self.key = key
		self.default_region = default_region
		self.requests_per_10s, self.requests_per_10m = requests_per_10s, requests_per_10m
		self.requests_in_last_10s, self.requests_in_last_10m = 0, 0

	def __remove_request_10s(self):
		self.requests_in_last_10s -= 1

	def __remove_request_10m(self):
		self.requests_in_last_10m -= 1

	def __add_requests(self):
		self.requests_in_last_10s += 1
		self.requests_in_last_10m += 1
		ts = Timer(10, self.__remove_request_10s)
		tm = Timer(600, self.__remove_request_10m)
		ts.start()
		tm.start()

	def can_make_request(self):
		return self.requests_in_last_10s < self.requests_per_10s and self.requests_in_last_10m < self.requests_per_10m

	def base_request(self, url, region, static=False, **kwargs):
		if region is None:
			region = self.default_region
		args = {'api_key': self.key}
		for k in kwargs:
			if kwargs[k] is not None:
				args[k] = kwargs[k]
		r = requests.get('https://prod.api.pvp.net/api/lol/{static}{region}/{url}'
							.format(
								static='static/' if static else '',
								region=region,
								url=url
							),
							params=args
		)
		if not static:
			self.__add_requests()
		raise_status(r)
		return r.json()

	# champion-v1.1
	def get_all_champions(self, region=None, free_to_play=False):
		return self.base_request('v1.1/champion', region, freeToPlay=free_to_play)

	# game-v1.3
	def get_recent_games(self, summoner_id, region=None):
		return self.base_request('v1.3/game/by-summoner/{summoner_id}/recent'.format(summoner_id=summoner_id), region)

	# league-v2.3, update 1
	def get_league(self, summoner_id, region=None):
		return self.base_request('v2.3/league/by-summoner/{summoner_id}'.format(summoner_id=summoner_id), region)

	def get_league_for_summoner(self, summoner_id, region=None):
		return self.base_request('v2.3/league/by-summoner/{summoner_id}/entry'.format(summoner_id=summoner_id), region)

	def get_challenger(self, region=None, queue=solo_queue):
		return self.base_request('v2.3/league/challenger', region, type=queue)

	# lol-static-data-v1
	def static_get_champion_list(self, region=None, locale=None, version=None, champ_data=None):
		return self.base_request('v1/champion', region, static=True, locale=locale, version=version, champData=champ_data)

	def static_get_champion(self, champ_id, region=None, locale=None, version=None, champ_data=None):
		return self.base_request(
				'v1/champion/{id}'.format(id=champ_id),
				region,
				static=True,
				locale=locale,
				version=version,
				champData=champ_data
		)

	def static_get_item_list(self, region=None, locale=None, version=None, item_list_data=None):
		return self.base_request('v1/item', region, static=True, locale=locale, version=version, itemListData=item_list_data)

	def static_get_item(self, item_id, region=None, locale=None, version=None, item_data=None):
		return self.base_request(
				'v1/item/{id}'.format(id=item_id),
				region,
				static=True,
				locale=locale,
				version=version,
				itemData=item_data
		)

	def static_get_mastery_list(self, region=None, locale=None, version=None, mastery_list_data=None):
		return self.base_request(
				'v1/mastery',
				region,
				static=True,
				locale=locale,
				version=version,
				masteryListData=mastery_list_data
		)

	def static_get_mastery(self, mastery_id, region=None, locale=None, version=None, mastery_data=None):
		return self.base_request(
				'v1/mastery/{id}'.format(id=mastery_id),
				region,
				static=True,
				locale=locale,
				version=version,
				masteryData=mastery_data
		)

	def static_get_realm(self, region=None):
		return self.base_request('v1/realm', region, static=True)

	def static_get_rune_list(self, region=None, locale=None, version=None, rune_list_data=None):
		return self.base_request('v1/rune', region, static=True, locale=locale, version=version, runeListData=rune_list_data)

	def static_get_rune(self, rune_id, region=None, locale=None, version=None, rune_data=None):
		return self.base_request(
				'v1/rune/{id}'.format(id=rune_id),
				region,
				static=True,
				locale=locale,
				version=version,
				runeData=rune_data
		)

	def static_get_summoner_spell_list(self, region=None, locale=None, version=None, spell_data=None):
		return self.base_request(
				'v1/summoner-spell',
				region,
				static=True,
				locale=locale,
				version=version,
				spellData=spell_data
		)

	def static_get_summoner_spell(self, spell_id, region=None, locale=None, version=None, spell_data=None):
		return self.base_request(
				'v1/summoner-spell/{id}'.format(id=spell_id),
				region,
				static=True,
				locale=locale,
				version=version,
				spellData=spell_data
		)

	# stats-v1.2
	def get_stat_summary(self, summoner_id, region=None, season=None):
		return self.base_request(
				'v1.2/stats/by-summoner/{summoner_id}/summary'.format(summoner_id=summoner_id),
				region,
				season='SEASON{}'.format(season) if season is not None else None)

	def get_ranked_stats(self, summoner_id, region=None, season=None):
		return self.base_request(
				'v1.2/stats/by-summoner/{summoner_id}/ranked'.format(summoner_id=summoner_id),
				region,
				season='SEASON{}'.format(season) if season is not None else None
		)

	# summoner-v1.3
	def get_mastery_pages(self, summoner_ids, region=None):
		return self.base_request(
				'v1.3/summoner/{summoner_ids}/masteries'.format(summoner_ids=','.join([str(s) for s in summoner_ids])),
				region
		)

	def get_rune_pages(self, summoner_ids, region=None):
		return self.base_request(
				'v1.3/summoner/{summoner_ids}/runes'.format(summoner_ids=','.join([str(s) for s in summoner_ids])),
				region
		)

	def get_summoners(self, names=None, ids=None, region=None):
		if (names is None) != (ids is None):
			return self.base_request(
				'v1.3/summoner/by-name/{summoner_names}'.format(summoner_names=','.join(names)) if names is not None
				else 'v1.3/summoner/{summoner_ids}'.format(summoner_ids=','.join([str(i) for i in ids])),
				region
			)
		else:
			return None

	def get_summoner(self, name=None, id=None, region=None):
		if (name is None) != (id is None):
			if name is not None:
				return self.get_summoners(names=[name, ], region=region)[name]
			else:
				return self.get_summoners(ids=[id, ], region=region)[str(id)]
		return None

	def get_summoner_name(self, summoner_ids, region=None):
		return self.base_request(
				'v1.3/summoner/{summoner_ids}/name'.format(summoner_ids=','.join([str(s) for s in summoner_ids])),
				region
		)

	# team-v2.2
	def get_teams(self, summoner_id, region=None):
		return self.base_request('v2.2/team/by-summoner/{summoner_id}'.format(summoner_id=summoner_id), region)
