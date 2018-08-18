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

    def test_version_api(self):
        versions = self._watcher.version.for_region(self._region)
        self.assertIsInstance(versions, dict)

    def test_dd_champion(self):
        versions = self._watcher.version.for_region(self._region)
        champions = self._watcher.data_dragon.champions(versions['n']['champion'])
        self.assertIsInstance(champions, dict)
