from unittest.mock import MagicMock

import pytest

from riotwatcher._apis.league_of_legends import ThirdPartyCodeApiV4


@pytest.mark.lol
@pytest.mark.unit
class TestThirdPartyCodeApiV4:
    def test_by_summoner(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        third_party_code = ThirdPartyCodeApiV4(mock_base_api)
        region = "afaaas"
        encrypted_summoner_id = "82357"

        ret = third_party_code.by_summoner(region, encrypted_summoner_id)

        mock_base_api.raw_request.assert_called_once_with(
            ThirdPartyCodeApiV4.__name__,
            third_party_code.by_summoner.__name__,
            region,
            f"https://{region}.api.riotgames.com/lol/platform/v4/third-party-code/by-summoner/{encrypted_summoner_id}",
            {},
        )

        assert ret is expected_return
