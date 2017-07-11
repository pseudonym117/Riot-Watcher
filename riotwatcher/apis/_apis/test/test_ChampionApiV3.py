
import unittest
from unittest.mock import MagicMock

from .. import ChampionApiV3

class ChampionApiV3TestCase(unittest.TestCase):
    def setUp(self):
        self._expected_return = object()

        self._base_api_mock = MagicMock(name='base_api')
        self._base_api_mock.request = MagicMock(name='request')
        self._base_api_mock.request.return_value = self._expected_return

    def test_champions_default(self):
        champ = ChampionApiV3(self._base_api_mock)
        region = 'na1'

        ret = champ.champions(region)

        self._base_api_mock.request.assert_called_once_with(
            region,
            '/lol/platform/v3/champions',
            freeToPlay=False
        )

        self.assertIs(self._expected_return, ret)

    def test_champions_free_to_play(self):
        champ = ChampionApiV3(self._base_api_mock)
        test_region = 'fsfsf'

        ret = champ.champions(test_region, free_to_play=True)

        self._base_api_mock.request.assert_called_once_with(
            test_region,
            '/lol/platform/v3/champions',
            freeToPlay=True
        )

        self.assertIs(self._expected_return, ret)

    def test_champ_by_id(self):
        champ = ChampionApiV3(self._base_api_mock)
        test_region = 'fsfsf'
        champ_id = 75

        ret = champ.champions_by_id(test_region, champ_id)

        self._base_api_mock.request.assert_called_once_with(
            test_region,
            '/lol/platform/v3/champions/75'
        )

        self.assertIs(self._expected_return, ret)
