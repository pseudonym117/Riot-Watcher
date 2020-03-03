from unittest.mock import MagicMock

import pytest

from riotwatcher._apis.legends_of_runeterra import RankedApi


@pytest.mark.lor
@pytest.mark.unit
class TestRankedApi:
    def test_leaderboards(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        ranked = RankedApi(mock_base_api)
        region = "afaaas"

        ret = ranked.leaderboards(region)

        mock_base_api.raw_request.assert_called_once_with(
            RankedApi.__name__,
            ranked.leaderboards.__name__,
            region,
            f"https://{region}.api.riotgames.com/lor/ranked/v1/leaderboards",
            {},
        )

        assert ret is expected_return
