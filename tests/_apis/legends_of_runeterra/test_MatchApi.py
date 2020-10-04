from unittest.mock import MagicMock

import pytest

from riotwatcher._apis.legends_of_runeterra import MatchApi


@pytest.fixture(params=["match_id_001122"])
def match_id(request):
    return request.param


@pytest.mark.lor
@pytest.mark.unit
class TestMatchApi:
    def test_by_puuid(self, region, puuid):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        match = MatchApi(mock_base_api)

        ret = match.by_puuid(region, puuid)

        mock_base_api.raw_request.assert_called_once_with(
            MatchApi.__name__,
            match.by_puuid.__name__,
            region,
            f"https://{region}.api.riotgames.com/lor/match/v1/matches/by-puuid/{puuid}/ids",
            {},
        )

        assert ret is expected_return

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
            f"https://{region}.api.riotgames.com/lor/match/v1/matches/{match_id}",
            {},
        )

        assert ret is expected_return
