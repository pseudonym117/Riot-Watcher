
import unittest
import sys

if sys.version_info > (3, 0):
    from unittest.mock import MagicMock
else:
    from mock import MagicMock

from .. import MasteriesApiV3


class MasteriesApiV3TestCase(unittest.TestCase):
    def setUp(self):
        self._expected_return = object()

        self._base_api_mock = MagicMock(name='base_api')
        self._base_api_mock.request = MagicMock(name='request')
        self._base_api_mock.request.return_value = self._expected_return

    def test_by_summoner(self):
        masteries = MasteriesApiV3(self._base_api_mock)
        region = 'afaaas'
        summoner_id = 14732

        ret = masteries.by_summoner(region, summoner_id)

        self._base_api_mock.request.assert_called_once_with(
            MasteriesApiV3.__name__,
            masteries.by_summoner.__name__,
            region,
            '/lol/platform/v3/masteries/by-summoner/{summonerId}'.format(summonerId=summoner_id)
        )

        self.assertIs(self._expected_return, ret)
