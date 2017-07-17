import unittest

from riotwatcher.main.riotwatcher import RiotWatcher
from riotwatcher import API_KEY


class TestDynamic(unittest.TestCase):

    def setUp(self):
        self.__summoner_name = 'zedt'
        self.__summoner_id = 19180446
        # if summoner doesnt have ranked teams, teams tests will fail
        # if summoner doesnt have ranked stats, stats tests will fail
        # these are not graceful failures, so try to use a summoner that has them

        self.__key = API_KEY
        self.__watcher = RiotWatcher(self.__key)

    def test_get_summoner_by_name(self):
        self.__watcher.get_summoner(name=self.__summoner_name)

    def test_get_summoner_by_id(self):
        self.__watcher.get_summoner(_id=self.__summoner_id)

    def test_get_mastery_page(self):
        self.__watcher.get_mastery_pages([self.__summoner_id, ])

    def test_get_runes_pages(self):
        self.__watcher.get_rune_pages([self.__summoner_id, ])

    def test_get_summoner_name(self):
        self.__watcher.get_summoner_name([self.__summoner_id, ])

    def test_get_game(self):
        self.__watcher.get_recent_games(self.__summoner_id)

    def test_get_league(self):
        self.__watcher.get_league(summoner_ids=[self.__summoner_id, ])
        self.__watcher.get_league_entry(summoner_ids=[self.__summoner_id, ])
        self.__watcher.get_challenger()
        self.__watcher.get_master()

    def test_get_stats(self):
        self.__watcher.get_stat_summary(self.__summoner_id)
        self.__watcher.get_ranked_stats(self.__summoner_id)

    def test_get_match_list(self):
        match_list = self.__watcher.get_match_list(self.__summoner_id)['matches'][0]
        self.__watcher.get_match(match_list['matchId'])

    def test_get_featured_games(self):
        self.__watcher.get_featured_games()

    def test_get_current_game_tests(self):
        player = self.__watcher.get_featured_games()['gameList'][0]['participants'][0]['summonerName']
        player_id = self.__watcher.get_summoner(name=player)['id']
        self.__watcher.get_current_game(player_id)
