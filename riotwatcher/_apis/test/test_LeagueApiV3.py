
import unittest
import sys

if sys.version_info > (3, 0):
    from unittest.mock import MagicMock
else:
    from mock import MagicMock

from .. import LeagueApiV3


class LeagueApiV3TestCase(unittest.TestCase):
    def setUp(self):
        self._expected_return = object()

        self._base_api_mock = MagicMock(name='base_api')
        self._base_api_mock.request = MagicMock(name='request')
        self._base_api_mock.request.return_value = self._expected_return

    def test_challenger_by_queue(self):
        league = LeagueApiV3(self._base_api_mock)
        region = 'afas'
        queue = 'yolo_q'

        ret = league.challenger_by_queue(region, queue)

        self._base_api_mock.request.assert_called_once_with(
            LeagueApiV3.__name__,
            league.challenger_by_queue.__name__,
            region,
            '/lol/league/v3/challengerleagues/by-queue/{queue}'.format(queue=queue)
        )

        self.assertIs(self._expected_return, ret)

    def test_masters_by_queue(self):
        league = LeagueApiV3(self._base_api_mock)
        region = 'afasf'
        queue = 'yolo_q'

        ret = league.masters_by_queue(region, queue)

        self._base_api_mock.request.assert_called_once_with(
            LeagueApiV3.__name__,
            league.masters_by_queue.__name__,
            region,
            '/lol/league/v3/masterleagues/by-queue/{queue}'.format(queue=queue)
        )

        self.assertIs(self._expected_return, ret)

    def test_by_summoner(self):
        league = LeagueApiV3(self._base_api_mock)
        region = 'afasf'
        summoner_id = 13542

        ret = league.by_summoner(region, summoner_id)

        self._base_api_mock.request.assert_called_once_with(
            LeagueApiV3.__name__,
            league.by_summoner.__name__,
            region,
            '/lol/league/v3/leagues/by-summoner/{summonerId}'.format(summonerId=summoner_id)
        )

        self.assertIs(self._expected_return, ret)

    def test_positions_by_summoner(self):
        league = LeagueApiV3(self._base_api_mock)
        region = 'afasf'
        summoner_id = 52343

        ret = league.positions_by_summoner(region, summoner_id)

        self._base_api_mock.request.assert_called_once_with(
            LeagueApiV3.__name__,
            league.positions_by_summoner.__name__,
            region,
            '/lol/league/v3/positions/by-summoner/{summonerId}'.format(summonerId=summoner_id)
        )

        self.assertIs(self._expected_return, ret)
