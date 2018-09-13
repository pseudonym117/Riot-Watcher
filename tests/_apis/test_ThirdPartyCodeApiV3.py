
import sys

if sys.version_info > (3, 0):
    from unittest.mock import MagicMock
else:
    from mock import MagicMock

from riotwatcher._apis import ThirdPartyCodeApiV3


class TestThirdPartyCodeApiV3(object):
    def test_by_summoner(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.request.return_value = expected_return

        third_party_code = ThirdPartyCodeApiV3(mock_base_api)
        region = 'afaaas'
        summoner_id = 82357

        ret = third_party_code.by_summoner(region, summoner_id)

        mock_base_api.request.assert_called_once_with(
            ThirdPartyCodeApiV3.__name__,
            third_party_code.by_summoner.__name__,
            region,
            '/lol/platform/v3/third-party-code/by-summoner/82357'
        )

        assert ret is expected_return
