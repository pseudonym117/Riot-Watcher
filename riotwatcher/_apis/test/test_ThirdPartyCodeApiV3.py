
import unittest
import sys

if sys.version_info > (3, 0):
    from unittest.mock import MagicMock
else:
    from mock import MagicMock

from .. import ThirdPartyCodeApiV3


class ThirdPartyCodeApiV3TestCase(unittest.TestCase):
    def setUp(self):
        self._expected_return = object()

        self._base_api_mock = MagicMock(name='base_api')
        self._base_api_mock.request = MagicMock(name='request')
        self._base_api_mock.request.return_value = self._expected_return

    def test_by_summoner(self):
        third_party_code = ThirdPartyCodeApiV3(self._base_api_mock)
        region = 'afaaas'
        summoner_id = 82357

        ret = third_party_code.by_summoner(region, summoner_id)

        self._base_api_mock.request.assert_called_once_with(
            ThirdPartyCodeApiV3.__name__,
            third_party_code.by_summoner.__name__,
            region,
            '/lol/platform/v3/third-party-code/by-summoner/82357'
        )

        self.assertIs(self._expected_return, ret)
