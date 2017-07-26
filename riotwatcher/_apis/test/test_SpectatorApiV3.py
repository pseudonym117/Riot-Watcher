
import unittest
import sys

if sys.version_info > (3, 0):
    from unittest.mock import MagicMock
else:
    from mock import MagicMock

from .. import SpectatorApiV3


class SpectatorApiV3TestCase(unittest.TestCase):
    def setUp(self):
        self._expected_return = object()

        self._base_api_mock = MagicMock(name='base_api')
        self._base_api_mock.request = MagicMock(name='request')
        self._base_api_mock.request.return_value = self._expected_return

    def test_by_summoner(self):
        spectator = SpectatorApiV3(self._base_api_mock)
        region = 'agagd'
        summoner_id = 98532

        ret = spectator.by_summoner(region, summoner_id)

        self._base_api_mock.request.assert_called_once_with(
            SpectatorApiV3.__name__,
            spectator.by_summoner.__name__,
            region,
            '/lol/spectator/v3/active-games/by-summoner/{summonerId}'.format(summonerId=summoner_id)
        )

        self.assertIs(self._expected_return, ret)

    def test_featured_games(self):
        spectator = SpectatorApiV3(self._base_api_mock)
        region = 'hfh42'

        ret = spectator.featured_games(region)

        self._base_api_mock.request.assert_called_once_with(
            SpectatorApiV3.__name__,
            spectator.featured_games.__name__,
            region,
            '/lol/spectator/v3/featured-games'
        )

        self.assertIs(self._expected_return, ret)
