
import os
import unittest

from requests import HTTPError

from .. import RiotWatcher


class RiotWatcherRealApiAccessTestCase(unittest.TestCase):
    def setUp(self):
        if not os.path.isfile('api_key'):
            raise FileNotFoundError(
                'API Key not found (should be in file "api_key" in same directory tests run)'
            )

        with open('api_key', 'r') as key_file:
            key = key_file.read()
            self._watcher = RiotWatcher(key.strip())

        self._region = 'na1'

        self._test_accounts = ['pseudonym117', 'fakename117']

    def test_champion_api(self):
        champion_list_dto = self._watcher.champion.all(self._region)

        for champ in champion_list_dto['champions']:
            self._watcher.champion.by_id(self._region, champ['id'])

        self._watcher.champion.all(self._region, free_to_play=True)

    def test_champion_mastery_api(self):
        for account in self._test_accounts:
            summ = self._watcher.summoner.by_name(self._region, account)

            s_id = summ['id']

            mastery_list = self._watcher.champion_mastery.by_summoner(self._region, s_id)

            for mastery in mastery_list:
                self._watcher.champion_mastery.by_summoner_by_champion(
                    self._region,
                    s_id,
                    mastery['championId']
                )

            self._watcher.champion_mastery.scores_by_summoner(self._region, s_id)

    def test_league_api(self):
        queues = [
            'RANKED_SOLO_5x5',
            'RANKED_FLEX_SR',
            'RANKED_FLEX_TT',
        ]

        league_ids = [
            '091e46a0-fdb0-11e7-9e8c-c81f66cf135e',
            '24c70240-fff2-11e7-919f-c81f66cf2333'
        ]

        for queue in queues:
            self._watcher.league.challenger_by_queue(self._region, queue)

            self._watcher.league.masters_by_queue(self._region, queue)

        for league_id in league_ids:
            self._watcher.league.by_id(self._region, league_id)

        for account in self._test_accounts:
            summ = self._watcher.summoner.by_name(self._region, account)

            s_id = summ['id']

            self._watcher.league.positions_by_summoner(self._region, s_id)

    def test_lol_status_api(self):
        self._watcher.lol_status.shard_data(self._region)

    def test_match_api(self):
        for name in self._test_accounts:
            summ = self._watcher.summoner.by_name(self._region, name)

            recent = self._watcher.match.matchlist_by_account(
                self._region,
                summ['accountId'],
                begin_index=0,
                end_index=20
            )

            for match in recent['matches']:
                mtch = self._watcher.match.by_id(self._region, match['gameId'])

                try:
                    self._watcher.match.timeline_by_match(self._region, mtch['gameId'])
                except HTTPError as err:
                    # 404 means game doesnt have timeline data, which is allowed
                    if err.response.status_code != 404:
                        raise

            try:
                self._watcher.match.matchlist_by_account(
                    self._region,
                    summ['accountId']
                )
            except HTTPError as err:
                # 404 indicates account doesnt have recent enough matches.
                # FakeName117 is in this boat.
                if err.response.status_code != 404:
                    raise

    def test_spectator_api(self):
        for account in self._test_accounts:
            summ = self._watcher.summoner.by_name(self._region, account)

            try:
                self._watcher.spectator.by_summoner(self._region, summ['id'])
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

                self._watcher.spectator.by_summoner(self._region, summoner['id'])
            except HTTPError as err:
                # maybe they got out of the game, or maybe the summonerName
                # was something like 'Summoner 1'
                if err.response.status_code != 404:
                    raise

    def test_static_data_api(self):
        champs = self._watcher.static_data.champions(self._region)

        for _, champ in champs['data'].items():
            self._watcher.static_data.champion(self._region, champ['id'])

        items = self._watcher.static_data.items(self._region)

        for _, item in items['data'].items():
            self._watcher.static_data.item(self._region, item['id'])

        self._watcher.static_data.language_strings(self._region)

        self._watcher.static_data.languages(self._region)

        self._watcher.static_data.maps(self._region)

        masteries = self._watcher.static_data.masteries(self._region)

        for _, mastery in masteries['data'].items():
            self._watcher.static_data.mastery(self._region, mastery['id'])

        self._watcher.static_data.profile_icons(self._region)

        self._watcher.static_data.realms(self._region)

        runes = self._watcher.static_data.runes(self._region)

        for _, rune in runes['data'].items():
            self._watcher.static_data.rune(self._region, rune['id'])

        summoner_spells = self._watcher.static_data.summoner_spells(self._region)

        for _, summoner_spell in summoner_spells['data'].items():
            self._watcher.static_data.summoner_spell(
                self._region,
                summoner_spell['id']
            )

        self._watcher.static_data.versions(self._region)

    def test_summoner_api(self):
        for summoner_name in self._test_accounts:
            summoner = self._watcher.summoner.by_name(self._region, summoner_name)

            self._watcher.summoner.by_account(self._region, summoner['accountId'])

            self._watcher.summoner.by_id(self._region, summoner['id'])
