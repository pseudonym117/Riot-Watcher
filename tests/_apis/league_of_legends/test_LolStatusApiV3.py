from unittest.mock import MagicMock

import pytest

from riotwatcher._apis.league_of_legends import LolStatusApiV3


@pytest.mark.lol
@pytest.mark.unit
class TestLolStatusApiV3:
    def test_shard_data(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        status = LolStatusApiV3(mock_base_api)
        region = "afaaas"

        ret = status.shard_data(region)

        mock_base_api.raw_request.assert_called_once_with(
            LolStatusApiV3.__name__,
            status.shard_data.__name__,
            region,
            f"https://{region}.api.riotgames.com/lol/status/v3/shard-data",
            {},
        )

        assert ret is expected_return
