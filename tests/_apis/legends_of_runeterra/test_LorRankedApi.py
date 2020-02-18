from unittest.mock import MagicMock

import pytest

from riotwatcher._apis.legends_of_runeterra import LorRankedApi


@pytest.mark.unit
class TestLorRankedApi:
    def test_leaderboards(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        ranked = LorRankedApi(mock_base_api)
        region = "afaaas"

        ret = ranked.leaderboards(region)

        mock_base_api.raw_request.assert_called_once_with(
            LorRankedApi.__name__,
            ranked.leaderboards.__name__,
            region,
            f"https://{region}.api.riotgames.com/lor/ranked/v1/leaderboards",
            {},
        )

        assert ret is expected_return
