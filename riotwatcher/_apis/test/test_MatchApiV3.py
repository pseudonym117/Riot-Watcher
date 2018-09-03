
import sys

if sys.version_info > (3, 0):
    from unittest.mock import MagicMock
else:
    from mock import MagicMock

from .. import MatchApiV3


class TestMatchApiV3(object):
    def test_by_id(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.request.return_value = expected_return

        match = MatchApiV3(mock_base_api)
        region = 'afaaas'
        match_id = 54321

        ret = match.by_id(region, match_id)

        mock_base_api.request.assert_called_once_with(
            MatchApiV3.__name__,
            match.by_id.__name__,
            region,
            '/lol/match/v3/matches/{matchId}'.format(matchId=match_id)
        )

        assert ret is expected_return

    def test_ml_by_account_defaults(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.request.return_value = expected_return

        match = MatchApiV3(mock_base_api)
        region = 'sfsfa'
        account_id = 15357

        ret = match.matchlist_by_account(region, account_id)

        mock_base_api.request.assert_called_once_with(
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

        assert ret is expected_return

    def test_ml_by_account_takes_param(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.request.return_value = expected_return

        match = MatchApiV3(mock_base_api)
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

        mock_base_api.request.assert_called_once_with(
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

        assert ret is expected_return

    def test_timeline_by_match(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.request.return_value = expected_return

        match = MatchApiV3(mock_base_api)
        region = 'afaaas'
        match_id = 262464

        ret = match.timeline_by_match(region, match_id)

        mock_base_api.request.assert_called_once_with(
            MatchApiV3.__name__,
            match.timeline_by_match.__name__,
            region,
            '/lol/match/v3/timelines/by-match/{matchId}'.format(matchId=match_id)
        )

        assert ret is expected_return
