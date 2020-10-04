from unittest.mock import MagicMock

import pytest

from riotwatcher._apis.valorant import MatchApi


@pytest.fixture(params=["12345"])
def match_id(request):
    return request.param


@pytest.fixture(params=["queue420"])
def queue(request):
    return request.param


@pytest.mark.unit
@pytest.mark.val
class TestMatchApi:
    def test_by_id(self, region, match_id):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        match = MatchApi(mock_base_api)

        ret = match.by_id(region, match_id)

        mock_base_api.raw_request.assert_called_once_with(
            MatchApi.__name__,
            match.by_id.__name__,
            region,
            f"https://{region}.api.riotgames.com/val/match/v1/matches/{match_id}",
            {},
        )

        assert ret == expected_return

    def test_matchlist_by_puuid(self, region, puuid):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        match = MatchApi(mock_base_api)

        ret = match.matchlist_by_puuid(region, puuid)

        mock_base_api.raw_request.assert_called_once_with(
            MatchApi.__name__,
            match.matchlist_by_puuid.__name__,
            region,
            f"https://{region}.api.riotgames.com/val/match/v1/matchlists/by-puuid/{puuid}",
            {},
        )

        assert ret == expected_return

    def test_recent_matches(self, region, queue):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        match = MatchApi(mock_base_api)

        ret = match.recent_matches(region, queue)

        mock_base_api.raw_request.assert_called_once_with(
            MatchApi.__name__,
            match.recent_matches.__name__,
            region,
            f"https://{region}.api.riotgames.com/val/match/v1/recent-matches/by-queue/{queue}",
            {},
        )

        assert ret == expected_return
