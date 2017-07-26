
import unittest
import sys

if sys.version_info > (3, 0):
    from unittest.mock import MagicMock
else:
    from mock import MagicMock

from .. import MatchApiV3


class MatchApiV3TestCase(unittest.TestCase):
    def setUp(self):
        self._expected_return = object()

        self._base_api_mock = MagicMock(name='base_api')
        self._base_api_mock.request = MagicMock(name='request')
        self._base_api_mock.request.return_value = self._expected_return

    def test_by_id(self):
        match = MatchApiV3(self._base_api_mock)
        region = 'afaaas'
        match_id = 54321

        ret = match.by_id(region, match_id)

        self._base_api_mock.request.assert_called_once_with(
            MatchApiV3.__name__,
            match.by_id.__name__,
            region,
            '/lol/match/v3/matches/{matchId}'.format(matchId=match_id)
        )

        self.assertIs(self._expected_return, ret)

    def test_matchlist_by_account_defaults(self):
        match = MatchApiV3(self._base_api_mock)
        region = 'sfsfa'
        account_id = 15357

        ret = match.matchlist_by_account(region, account_id)

        self._base_api_mock.request.assert_called_once_with(
            MatchApiV3.__name__,
            match.matchlist_by_account.__name__,
            region,
            '/lol/match/v3/matchlists/by-account/{accountId}'.format(accountId=account_id),
            queue=None,
            beginTime=None,
            endTime=None,
            beginIndex=None,
            endIndex=None,
            season=None,
            champion=None
        )

        self.assertIs(self._expected_return, ret)

    def test_matchlist_by_account_takes_params(self):
        match = MatchApiV3(self._base_api_mock)
        region = 'sfsfa'
        account_id = 15357

        queue = 'dfdfdaaa'
        begin_time, end_time = 'sgshrhr', 'sfsfsjjrj'
        begin_index, end_index = 'jtj3d', '3tn3ti'
        season = 'hg4reg422'
        champion = 'cancer'

        ret = match.matchlist_by_account(
            region,
            account_id,
            queue=queue,
            begin_time=begin_time,
            end_time=end_time,
            begin_index=begin_index,
            end_index=end_index,
            season=season,
            champion=champion
        )

        self._base_api_mock.request.assert_called_once_with(
            MatchApiV3.__name__,
            match.matchlist_by_account.__name__,
            region,
            '/lol/match/v3/matchlists/by-account/{accountId}'.format(accountId=account_id),
            queue=queue,
            beginTime=begin_time,
            endTime=end_time,
            beginIndex=begin_index,
            endIndex=end_index,
            season=season,
            champion=champion
        )

        self.assertIs(self._expected_return, ret)

    def test_matchlist_by_account_recent(self):
        match = MatchApiV3(self._base_api_mock)
        region = 'afaaas'
        account_id = 2624

        ret = match.matchlist_by_account_recent(region, account_id)

        self._base_api_mock.request.assert_called_once_with(
            MatchApiV3.__name__,
            match.matchlist_by_account_recent.__name__,
            region,
            '/lol/match/v3/matchlists/by-account/{accountId}/recent'.format(accountId=account_id)
        )

        self.assertIs(self._expected_return, ret)

    def test_timeline_by_match(self):
        match = MatchApiV3(self._base_api_mock)
        region = 'afaaas'
        match_id = 262464

        ret = match.timeline_by_match(region, match_id)

        self._base_api_mock.request.assert_called_once_with(
            MatchApiV3.__name__,
            match.timeline_by_match.__name__,
            region,
            '/lol/match/v3/timelines/by-match/{matchId}'.format(matchId=match_id)
        )

        self.assertIs(self._expected_return, ret)
