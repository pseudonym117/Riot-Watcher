import sys

import pytest

if sys.version_info > (3, 0):
    from unittest.mock import MagicMock
else:
    from mock import MagicMock

from riotwatcher._apis import ThirdPartyCodeApiV4


@pytest.mark.unit
class TestThirdPartyCodeApiV4(object):
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
            "https://afaaas.api.riotgames.com/lol/platform/v4/third-party-code/by-summoner/82357",
            {},
        )

        assert ret is expected_return
