
import sys

if sys.version_info > (3, 0):
    from unittest.mock import MagicMock
else:
    from mock import MagicMock

from riotwatcher._apis import LolStatusApiV3


class TestLolStatusApiV3(object):
    def test_shard_data(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        status = LolStatusApiV3(mock_base_api)
        region = 'afaaas'

        ret = status.shard_data(region)

        mock_base_api.raw_request.assert_called_once_with(
            LolStatusApiV3.__name__,
            status.shard_data.__name__,
            region,
            'https://afaaas.api.riotgames.com/lol/status/v3/shard-data',
            {}
        )

        assert ret is expected_return
