from collections import namedtuple
from unittest.mock import MagicMock

import pytest

from riotwatcher._apis.team_fight_tactics import MatchApi

MockMatchApi = namedtuple("MockMatchApi", ["base_api", "api", "expected_return"])


@pytest.fixture
def mock_match_api():
    mock_base_api = MagicMock()
    api = MatchApi(mock_base_api)
    expected_return = object()
    mock_base_api.raw_request.return_value = expected_return

    return MockMatchApi(mock_base_api, api, expected_return)


@pytest.mark.tft
@pytest.mark.unit
class TestMatchApi:
    def test_by_puuid(self, mock_match_api):
        region = "afas"
        puuid = "15462-54321"

        ret = mock_match_api.api.by_puuid(region, puuid)

        mock_match_api.base_api.raw_request.assert_called_once_with(
            MatchApi.__name__,
            mock_match_api.api.by_puuid.__name__,
            region,
            f"https://{region}.api.riotgames.com/tft/match/v1/matches/by-puuid/{puuid}/ids",
            {"count": 20},
        )

        assert ret is mock_match_api.expected_return

    def test_by_puuid_remaps_region(self, mock_match_api, region_remap):
        puuid = "1234"

        mock_match_api.api.by_puuid(region_remap.original, puuid)

        mock_match_api.base_api.raw_request.assert_called_once_with(
            MatchApi.__name__,
            mock_match_api.api.by_puuid.__name__,
            region_remap.to,
            f"https://{region_remap.to}.api.riotgames.com/tft/match/v1/matches/by-puuid/{puuid}/ids",
            {"count": 20},
        )

    def test_by_id(self, mock_match_api):
        region = "afas"
        match_id = "hdjshsfh333"

        ret = mock_match_api.api.by_id(region, match_id)

        mock_match_api.base_api.raw_request.assert_called_once_with(
            MatchApi.__name__,
            mock_match_api.api.by_id.__name__,
            region,
            f"https://{region}.api.riotgames.com/tft/match/v1/matches/{match_id}",
            {},
        )

        assert ret is mock_match_api.expected_return

    def test_by_id_remaps_region(self, mock_match_api, region_remap):
        match_id = "hdjshsfh333"

        mock_match_api.api.by_id(region_remap.original, match_id)

        mock_match_api.base_api.raw_request.assert_called_once_with(
            MatchApi.__name__,
            mock_match_api.api.by_id.__name__,
            region_remap.to,
            f"https://{region_remap.to}.api.riotgames.com/tft/match/v1/matches/{match_id}",
            {},
        )

