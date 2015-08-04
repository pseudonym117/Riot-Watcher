
# these tests are pretty bad, mostly to make sure no exceptions are thrown

import time
from riotwatcher import RiotWatcher, NORTH_AMERICA
import os

key = os.environ['RIOT_API_KEY']
# if summoner doesnt have ranked teams, teams tests will fail
# if summoner doesnt have ranked stats, stats tests will fail
# these are not graceful failures, so try to use a summoner that has them
summoner_name = 'pseudonym117'

w = RiotWatcher(key)

import unittest

def wait():
    while not w.can_make_request():
        time.sleep(2)

class TestAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # only initialize some variables once
        cls.summoner = w.get_summoner(name=summoner_name)

    def setUp(self):
        wait()

    def test_can_get_champion(self):
        temp = w.get_all_champions()
        wait()
        self.assertIsNotNone(w.get_champion(temp['champions'][0]['id']))

    def test_can_get_featured_games(self):
        temp = w.get_featured_games()
        self.assertIsNotNone(temp)

    def test_can_get_current_game(self):
        player = w.get_featured_games()['gameList'][0]['participants'][0]['summonerName']
        wait()
        player_id = w.get_summoner(name=player)['id']
        wait()
        self.assertIsNotNone(w.get_current_game(player_id))

    def test_can_get_static(self):
        temp = w.static_get_champion_list()
        self.assertIsNotNone(w.static_get_champion(temp['data'][list(temp['data'])[0]]['id']))
        temp = w.static_get_item_list()
        self.assertIsNotNone(w.static_get_item(temp['data'][list(temp['data'])[0]]['id']))
        temp = w.static_get_mastery_list()
        self.assertIsNotNone(w.static_get_mastery(temp['data'][list(temp['data'])[0]]['id']))
        self.assertIsNotNone(w.static_get_realm())
        temp = w.static_get_rune_list()
        self.assertIsNotNone(w.static_get_rune(temp['data'][list(temp['data'])[0]]['id']))
        temp = w.static_get_summoner_spell_list()
        self.assertIsNotNone(w.static_get_summoner_spell(temp['data'][list(temp['data'])[0]]['id']))
        self.assertIsNotNone(w.static_get_versions())

    def test_can_get_status(self):
        self.assertIsNotNone(w.get_server_status())
        self.assertIsNotNone(w.get_server_status(region=NORTH_AMERICA))

    def test_can_get_summoner(self):
        summoner = w.get_summoner(name=summoner_name)
        self.assertIsNotNone(summoner)
        wait()
        self.assertIsNotNone(w.get_summoner(_id=summoner['id']))
        wait()
        self.assertIsNotNone(w.get_mastery_pages([summoner['id'], ]))
        wait()
        self.assertIsNotNone(w.get_rune_pages([summoner['id'], ]))
        wait()
        self.assertIsNotNone(w.get_summoner_name([summoner['id'], ]))

    def test_can_get_recent_games(self):
        temp = w.get_recent_games(self.summoner['id'])
        self.assertIsNotNone(temp)

    def test_can_get_league(self):
        self.assertIsNotNone(w.get_league(summoner_ids=[self.summoner['id'], ]))
        wait()
        self.assertIsNotNone(w.get_league_entry(summoner_ids=[self.summoner['id'], ]))
        wait()
        self.assertIsNotNone(w.get_challenger())
        wait()
        self.assertIsNotNone(w.get_master())

    def test_can_get_match(self):
        matches = w.get_match_history(self.summoner['id'])
        self.assertIsNotNone(matches)
        match = matches['matches'][0]
        self.assertIsNotNone(w.get_match(match['matchId']))

    def test_can_get_stats(self):
        self.assertIsNotNone(w.get_stat_summary(self.summoner['id']))
        wait()
        self.assertIsNotNone(w.get_ranked_stats(self.summoner['id']))

    def test_can_get_team(self):
        team = w.get_teams_for_summoner(self.summoner['id'])
        self.assertIsNotNone(team)
        wait()
        self.assertIsNotNone(w.get_team(team[0]['fullId']))

    def test_can_get_match_list(self):
        self.assertIsNotNone(w.get_match_list(self.summoner['id']))

if __name__ == '__main__':
    unittest.main()
