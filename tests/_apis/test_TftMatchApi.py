from unittest.mock import MagicMock

import pytest

from riotwatcher._apis import TftMatchApi


@pytest.mark.unit
class TestTftMatchApi:
    def test_by_puuid(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        match = TftMatchApi(mock_base_api)
        region = "afas"
        puuid = "15462-54321"

        ret = match.by_puuid(region, puuid)

        mock_base_api.raw_request.assert_called_once_with(
            TftMatchApi.__name__,
            match.by_puuid.__name__,
            region,
            f"https://{region}.api.riotgames.com/tft/match/v1/matches/by-puuid/{puuid}/ids",
            {},
        )

        assert ret is expected_return

    def test_by_id(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        match = TftMatchApi(mock_base_api)
        region = "afas"
        match_id = "hdjshsfh333"

        ret = match.by_id(region, match_id)

        mock_base_api.raw_request.assert_called_once_with(
            TftMatchApi.__name__,
            match.by_id.__name__,
            region,
            f"https://{region}.api.riotgames.com/tft/match/v1/matches/{match_id}",
            {},
        )

        assert ret is expected_return
