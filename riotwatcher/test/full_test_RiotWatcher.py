
import os
import unittest

from requests import HTTPError

from .. import RiotWatcher


class RiotWatcherRealApiAccessTestCase(unittest.TestCase):
    def setUp(self):
        if not os.path.isfile('api_key'):
            raise FileNotFoundError('API Key not found (should be in file "api_key" in same directory tests run)')

        with open('api_key', 'r') as f:
            key = f.read()
            self._watcher = RiotWatcher(key.strip())

        self._region = 'na1'

        self._test_accounts = ['pseudonym117', 'fakename117']

    def test_champion_api(self):
        champion_list_dto = self._watcher.champion.all(self._region)

        for champ in champion_list_dto['champions']:
            c = self._watcher.champion.by_id(self._region, champ['id'])

        f2p_champs = self._watcher.champion.all(self._region, free_to_play=True)

    def test_champion_mastery_api(self):
        for account in self._test_accounts:
            s = self._watcher.summoner.by_name(self._region, account)

            s_id = s['id']

            mastery_list = self._watcher.champion_mastery.by_summoner(self._region, s_id)

            for mastery in mastery_list:
                champ_mastery = self._watcher.champion_mastery.by_summoner_by_champion(
                    self._region,
                    s_id,
                    mastery['championId']
                )

            scores = self._watcher.champion_mastery.scores_by_summoner(self._region, s_id)

    def test_league_api(self):
        queues = [
            'RANKED_SOLO_5x5',
            'RANKED_FLEX_SR',
            'RANKED_FLEX_TT',
        ]

        for queue in queues:
            redditors = self._watcher.league.challenger_by_queue(self._region, queue)

            plebs = self._watcher.league.masters_by_queue(self._region, queue)

        for account in self._test_accounts:
            s = self._watcher.summoner.by_name(self._region, account)

            s_id = s['id']

            my_leagues = self._watcher.league.by_summoner(self._region, s_id)

            my_positions = self._watcher.league.positions_by_summoner(self._region, s_id)

    def test_lol_status_api(self):
        self._watcher.lol_status.shard_data(self._region)

    def test_masteries_api(self):
        for account in self._test_accounts:
            s = self._watcher.summoner.by_name(self._region, account)

            masteries = self._watcher.masteries.by_summoner(self._region, s['id'])

    def test_match_api(self):
        for name in self._test_accounts:
            s = self._watcher.summoner.by_name(self._region, name)

            recent = self._watcher.match.matchlist_by_account_recent(self._region, s['accountId'])

            for match in recent['matches']:
                m = self._watcher.match.by_id(self._region, match['gameId'])

                try:
                    timeline = self._watcher.match.timeline_by_match(self._region, m['gameId'])
                except HTTPError as err:
                    # 404 means game doesnt have timeline data, which is allowed
                    if err.response.status_code != 404:
                        raise

            try:
                whatever_match_returns_default = self._watcher.match.matchlist_by_account(
                    self._region,
                    s['accountId']
                )
            except HTTPError as err:
                # 404 indicates account doesnt have recent enough matches.
                # FakeName117 is in this boat.
                if err.response.status_code != 404:
                    raise

    def test_runes_api(self):
        for account in self._test_accounts:
            s = self._watcher.summoner.by_name(self._region, account)

            runes = self._watcher.runes.by_summoner(self._region, s['id'])

    def test_spectator_api(self):
        for account in self._test_accounts:
            s = self._watcher.summoner.by_name(self._region, account)

            try:
                game = self._watcher.spectator.by_summoner(self._region, s['id'])
            except HTTPError as err:
                # one of these will 404, i dont think i am going to be playing
                # a game on 2 accounts at once.
                if err.response.status_code != 404:
                    raise

        featured = self._watcher.spectator.featured_games(self._region)

        for player in featured['gameList'][0]['participants']:
            if player['bot']:
                continue

            try:
                summoner = self._watcher.summoner.by_name(self._region, player['summonerName'])

                game = self._watcher.spectator.by_summoner(self._region, summoner['id'])
            except HTTPError as err:
                # maybe they got out of the game, or maybe the summonerName
                # was something like 'Summoner 1'
                if err.response.status_code != 404:
                    raise

    def test_static_data_api(self):
        champs = self._watcher.static_data.champions(self._region)

        for name, champ in champs['data'].items():
            api_champ = self._watcher.static_data.champion(self._region, champ['id'])

        items = self._watcher.static_data.items(self._region)

        for name, item in items['data'].items():
            api_item = self._watcher.static_data.item(self._region, item['id'])

        language_strings = self._watcher.static_data.language_strings(self._region)

        languages = self._watcher.static_data.languages(self._region)

        maps = self._watcher.static_data.maps(self._region)

        masteries = self._watcher.static_data.masteries(self._region)

        for name, mastery in masteries['data'].items():
            api_mastery = self._watcher.static_data.mastery(self._region, mastery['id'])

        profile_icons = self._watcher.static_data.profile_icons(self._region)

        realms = self._watcher.static_data.realms(self._region)

        runes = self._watcher.static_data.runes(self._region)

        for name, rune in runes['data'].items():
            api_run = self._watcher.static_data.rune(self._region, rune['id'])

        summoner_spells = self._watcher.static_data.summoner_spells(self._region)

        for name, summoner_spell in summoner_spells['data'].items():
            api_summoner_spell = self._watcher.static_data.summoner_spell(
                self._region,
                summoner_spell['id']
            )

        versions = self._watcher.static_data.versions(self._region)

    def test_summoner_api(self):
        for summoner_name in self._test_accounts:
            summoner = self._watcher.summoner.by_name(self._region, summoner_name)

            account = self._watcher.summoner.by_account(self._region, summoner['accountId'])

            summoner_again = self._watcher.summoner.by_id(self._region, summoner['id'])
