
import unittest
import sys

if sys.version_info > (3, 0):
    from unittest.mock import MagicMock
else:
    from mock import MagicMock


from .. import ChampionApiV3


class ChampionApiV3TestCase(unittest.TestCase):
    def setUp(self):
        self._expected_return = object()

        self._base_api_mock = MagicMock(name='base_api')
        self._base_api_mock.request = MagicMock(name='request')
        self._base_api_mock.request.return_value = self._expected_return

    def test_all_default(self):
        champ = ChampionApiV3(self._base_api_mock)
        region = 'na1'

        ret = champ.all(region)

        self._base_api_mock.request.assert_called_once_with(
            ChampionApiV3.__name__,
            champ.all.__name__,
            region,
            '/lol/platform/v3/champions',
            freeToPlay="false"
        )

        self.assertIs(self._expected_return, ret)

    def test_champions_free_to_play(self):
        champ = ChampionApiV3(self._base_api_mock)
        test_region = 'fsfsf'

        ret = champ.all(test_region, free_to_play=True)

        self._base_api_mock.request.assert_called_once_with(
            ChampionApiV3.__name__,
            champ.all.__name__,
            test_region,
            '/lol/platform/v3/champions',
            freeToPlay="true"
        )

        self.assertIs(self._expected_return, ret)

    def test_champ_by_id(self):
        champ = ChampionApiV3(self._base_api_mock)
        test_region = 'fsfsf'
        champ_id = 75

        ret = champ.by_id(test_region, champ_id)

        self._base_api_mock.request.assert_called_once_with(
            ChampionApiV3.__name__,
            champ.by_id.__name__,
            test_region,
            '/lol/platform/v3/champions/75'
        )

        self.assertIs(self._expected_return, ret)
