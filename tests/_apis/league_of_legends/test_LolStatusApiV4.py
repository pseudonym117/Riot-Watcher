from unittest.mock import MagicMock

import pytest

from riotwatcher._apis.league_of_legends import LolStatusApiV4


@pytest.mark.lol
@pytest.mark.unit
class TestLolStatusApiV4:
    def test_platform_data(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        status = LolStatusApiV4(mock_base_api)
        region = "afaaas"

        ret = status.platform_data(region)

        mock_base_api.raw_request.assert_called_once_with(
            LolStatusApiV4.__name__,
            status.platform_data.__name__,
            region,
            f"https://{region}.api.riotgames.com/lol/status/v4/platform-data",
            {},
        )

        assert ret is expected_return
