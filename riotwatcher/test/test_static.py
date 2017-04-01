import unittest

from riotwatcher.main.riotwatcher import RiotWatcher
from riotwatcher import API_KEY


class TestStatic(unittest.TestCase):

    def setUp(self):
        self.__summoner_name = 'Taikki'
        self.__summoner_id = 73759302
        # if summoner doesnt have ranked teams, teams tests will fail
        # if summoner doesnt have ranked stats, stats tests will fail
        # these are not graceful failures, so try to use a summoner that has them

        self.__key = API_KEY
        self.__watcher = RiotWatcher(self.__key)

    def test_get_champion(self):
        temp = self.__watcher.static_get_champion_list()
        self.__watcher.static_get_champion(temp['data'][list(temp['data'])[0]]['id'])

    def test_get_item(self):
        temp = self.__watcher.static_get_item_list()
        self.__watcher.static_get_item(temp['data'][list(temp['data'])[0]]['id'])

    def test_get_mastery(self):
        temp = self.__watcher.static_get_mastery_list()
        self.__watcher.static_get_mastery(temp['data'][list(temp['data'])[0]]['id'])

    def test_get_realm(self):
        self.__watcher.static_get_realm()

    def test_get_rune(self):
        temp = self.__watcher.static_get_rune_list()
        self.__watcher.static_get_rune(temp['data'][list(temp['data'])[0]]['id'])

    def test_get_summoner_spell(self):
        temp = self.__watcher.static_get_summoner_spell_list()
        self.__watcher.static_get_summoner_spell(temp['data'][list(temp['data'])[0]]['id'])

    def test_get_versions(self):
        self.__watcher.static_get_versions()