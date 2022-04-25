from collections import namedtuple
from unittest.mock import MagicMock

import pytest

from riotwatcher._apis.league_of_legends import MatchApiV5


MockMatchApi = namedtuple("MockMatchApi", ["base_api", "api", "expected_return"])


@pytest.fixture
def mock_match_api():
    mock_base_api = MagicMock()
    api = MatchApiV5(mock_base_api)
    expected_return = object()
    mock_base_api.raw_request.return_value = expected_return

    return MockMatchApi(mock_base_api, api, expected_return)


@pytest.mark.lol
@pytest.mark.unit
class TestMatchApiV5:
    def test_by_id(self, mock_match_api):
        region = "afaaas"
        match_id = 54321

        ret = mock_match_api.api.by_id(region, match_id)

        mock_match_api.base_api.raw_request.assert_called_once_with(
            MatchApiV5.__name__,
            mock_match_api.api.by_id.__name__,
            region,
            f"https://{region}.api.riotgames.com/lol/match/v5/matches/{match_id}",
            {},
        )

        assert ret is mock_match_api.expected_return

    def test_by_id_remaps_region(
        self, mock_match_api, region_remap,
    ):
        match_id = 54321
        mock_match_api.api.by_id(region_remap.original, match_id)

        mock_match_api.base_api.raw_request.assert_called_once_with(
            MatchApiV5.__name__,
            mock_match_api.api.by_id.__name__,
            region_remap.to,
            f"https://{region_remap.to}.api.riotgames.com/lol/match/v5/matches/{match_id}",
            {},
        )

    def test_ml_by_puuid_defaults(self, mock_match_api):
        region = "sfsfa"
        puuid = "15357"

        ret = mock_match_api.api.matchlist_by_puuid(region, puuid)

        mock_match_api.base_api.raw_request.assert_called_once_with(
            MatchApiV5.__name__,
            mock_match_api.api.matchlist_by_puuid.__name__,
            region,
            f"https://{region}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids",
            {
                "start": None,
                "count": None,
                "queue": None,
                "type": None,
                "startTime": None,
                "endTime": None,
            },
        )

        assert ret is mock_match_api.expected_return

    def test_ml_by_puuid_remaps_region(
        self, mock_match_api, region_remap,
    ):
        puuid = "54321"
        mock_match_api.api.matchlist_by_puuid(region_remap.original, puuid)

        mock_match_api.base_api.raw_request.assert_called_once_with(
            MatchApiV5.__name__,
            mock_match_api.api.matchlist_by_puuid.__name__,
            region_remap.to,
            f"https://{region_remap.to}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids",
            {
                "start": None,
                "count": None,
                "queue": None,
                "type": None,
                "startTime": None,
                "endTime": None,
            },
        )

    def test_ml_by_account_takes_param(self, mock_match_api):
        region = "sfsfa"
        puuid = "15357"

        start = "asfaf"
        count = "afasf"
        queue = 420
        type = "norms"
        start_time = 1000
        end_time = 2000

        ret = mock_match_api.api.matchlist_by_puuid(
            region,
            puuid,
            start=start,
            count=count,
            queue=queue,
            type=type,
            start_time=start_time,
            end_time=end_time,
        )

        mock_match_api.base_api.raw_request.assert_called_once_with(
            MatchApiV5.__name__,
            mock_match_api.api.matchlist_by_puuid.__name__,
            region,
            f"https://{region}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids",
            {
                "start": start,
                "count": count,
                "queue": queue,
                "type": type,
                "startTime": start_time,
                "endTime": end_time,
            },
        )

        assert ret is mock_match_api.expected_return

    def test_timeline_by_match(self, mock_match_api):
        region = "afaaas"
        match_id = 262464

        ret = mock_match_api.api.timeline_by_match(region, match_id)

        mock_match_api.base_api.raw_request.assert_called_once_with(
            MatchApiV5.__name__,
            mock_match_api.api.timeline_by_match.__name__,
            region,
            f"https://{region}.api.riotgames.com/lol/match/v5/matches/{match_id}/timeline",
            {},
        )

        assert ret is mock_match_api.expected_return

    def test_timeline_by_match_region(
        self, mock_match_api, region_remap,
    ):
        match_id = 54321
        mock_match_api.api.timeline_by_match(region_remap.original, match_id)

        mock_match_api.base_api.raw_request.assert_called_once_with(
            MatchApiV5.__name__,
            mock_match_api.api.timeline_by_match.__name__,
            region_remap.to,
            f"https://{region_remap.to}.api.riotgames.com/lol/match/v5/matches/{match_id}/timeline",
            {},
        )
