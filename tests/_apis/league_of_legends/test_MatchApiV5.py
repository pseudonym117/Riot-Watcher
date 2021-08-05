from unittest.mock import MagicMock

import pytest

from riotwatcher._apis.league_of_legends import MatchApiV5


@pytest.mark.lol
@pytest.mark.unit
class TestMatchApiV5:
    def test_by_id(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        matchv5 = MatchApiV5(mock_base_api)
        region = "afaaas"
        match_id = 54321

        ret = matchv5.by_id(region, match_id)

        mock_base_api.raw_request.assert_called_once_with(
            MatchApiV5.__name__,
            matchv5.by_id.__name__,
            region,
            f"https://{region}.api.riotgames.com/lol/match/v5/matches/{match_id}",
            {},
        )

        assert ret is expected_return

    def test_ml_by_puuid_defaults(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        matchv5 = MatchApiV5(mock_base_api)
        region = "sfsfa"
        puuid = "15357"

        ret = matchv5.matchlist_by_puuid(region, puuid)

        mock_base_api.raw_request.assert_called_once_with(
            MatchApiV5.__name__,
            matchv5.matchlist_by_puuid.__name__,
            region,
            f"https://{region}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids",
            {"start": None, "count": None, "queue": None, "type": None,},
        )

        assert ret is expected_return

    def test_ml_by_account_takes_param(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        matchv5 = MatchApiV5(mock_base_api)
        region = "sfsfa"
        puuid = "15357"

        start = "asfaf"
        count = "afasf"
        queue = 420
        type = "norms"

        ret = matchv5.matchlist_by_puuid(
            region, puuid, start=start, count=count, queue=queue, type=type,
        )

        mock_base_api.raw_request.assert_called_once_with(
            MatchApiV5.__name__,
            matchv5.matchlist_by_puuid.__name__,
            region,
            f"https://{region}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids",
            {"start": start, "count": count, "queue": queue, "type": type},
        )

        assert ret is expected_return

    def test_timeline_by_match(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        matchv5 = MatchApiV5(mock_base_api)
        region = "afaaas"
        match_id = 262464

        ret = matchv5.timeline_by_match(region, match_id)

        mock_base_api.raw_request.assert_called_once_with(
            MatchApiV5.__name__,
            matchv5.timeline_by_match.__name__,
            region,
            f"https://{region}.api.riotgames.com/lol/match/v5/matches/{match_id}/timeline",
            {},
        )

        assert ret is expected_return
