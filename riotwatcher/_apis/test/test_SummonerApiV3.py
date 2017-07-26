
import unittest
import sys

if sys.version_info > (3, 0):
    from unittest.mock import MagicMock
else:
    from mock import MagicMock

from .. import SummonerApiV3


class SummonerApiV3TestCase(unittest.TestCase):
    def setUp(self):
        self._expected_return = object()

        self._base_api_mock = MagicMock(name='base_api')
        self._base_api_mock.request = MagicMock(name='request')
        self._base_api_mock.request.return_value = self._expected_return

    def test_by_account(self):
        summoner = SummonerApiV3(self._base_api_mock)
        region = 'htr35ge'
        account_id = 98532

        ret = summoner.by_account(region, account_id)

        self._base_api_mock.request.assert_called_once_with(
            SummonerApiV3.__name__,
            summoner.by_account.__name__,
            region,
            '/lol/summoner/v3/summoners/by-account/{accountId}'.format(accountId=account_id)
        )

        self.assertIs(self._expected_return, ret)

    def test_by_name(self):
        summoner = SummonerApiV3(self._base_api_mock)
        region = 'htr35ge'
        summoner_name = 'psesn886'

        ret = summoner.by_name(region, summoner_name)

        self._base_api_mock.request.assert_called_once_with(
            SummonerApiV3.__name__,
            summoner.by_name.__name__,
            region,
            '/lol/summoner/v3/summoners/by-name/{summonerName}'.format(summonerName=summoner_name)
        )

        self.assertIs(self._expected_return, ret)

    def test_by_id(self):
        summoner = SummonerApiV3(self._base_api_mock)
        region = 'htr35ge'
        summoner_id = 25979

        ret = summoner.by_id(region, summoner_id)

        self._base_api_mock.request.assert_called_once_with(
            SummonerApiV3.__name__,
            summoner.by_id.__name__,
            region,
            '/lol/summoner/v3/summoners/{summonerId}'.format(summonerId=summoner_id)
        )

        self.assertIs(self._expected_return, ret)
