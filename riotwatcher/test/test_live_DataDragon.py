import os
import unittest

from riotwatcher import RiotWatcher


class RiotWatcherRealApiAccessTestCase(unittest.TestCase):
    def setUp(self):
        if not os.path.isfile('api_key'):
            raise FileNotFoundError(
                'API Key not found (should be in file "api_key" in same directory tests run)'
            )

        with open('api_key', 'r') as key_file:
            key = key_file.read()
            self._watcher = RiotWatcher(key.strip())

        self._region = 'euw1'
        self._versions = {"item": "8.16.1", "rune": "7.23.1", "mastery": "7.23.1", "summoner": "8.16.1",
                          "champion": "8.16.1", "profileicon": "8.16.1", "map": "8.16.1", "language": "8.16.1",
                          "sticker": "8.16.1"}

    def test_version_api(self):
        versions = self._watcher.version.for_region(self._region)
        self.assertIsInstance(versions, dict)

    def test_dd_champion(self):
        champions = self._watcher.data_dragon.champions(self._versions['champion'])
        self.assertIsInstance(champions, dict)

    def test_dd_items(self):
        ret = self._watcher.data_dragon.items(self._versions['item'])
        self.assertIsInstance(ret, dict)

    def test_dd_languages(self):
        ret = self._watcher.data_dragon.languages(self._versions['language'])
        self.assertIsInstance(ret, dict)

    def test_dd_maps(self):
        ret = self._watcher.data_dragon.maps(self._versions['map'])
        self.assertIsInstance(ret, dict)

    def test_dd_masteries(self):
        ret = self._watcher.data_dragon.masteries(self._versions['mastery'])
        self.assertIsInstance(ret, dict)

    def test_dd_icons(self):
        ret = self._watcher.data_dragon.profileIcons(self._versions['profileicon'])
        self.assertIsInstance(ret, dict)

    def test_dd_summoners(self):
        ret = self._watcher.data_dragon.summonerSpells(self._versions['summoner'])
        self.assertIsInstance(ret, dict)
