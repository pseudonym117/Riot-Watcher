
import unittest
import sys

if sys.version_info > (3, 0):
    from unittest.mock import MagicMock
else:
    from mock import MagicMock

from .. import LolStatusApiV3


class LolStatusApiV3TestCase(unittest.TestCase):
    def setUp(self):
        self._expected_return = object()

        self._base_api_mock = MagicMock(name='base_api')
        self._base_api_mock.request = MagicMock(name='request')
        self._base_api_mock.request.return_value = self._expected_return

    def test_shard_data(self):
        status = LolStatusApiV3(self._base_api_mock)
        region = 'afaaas'

        ret = status.shard_data(region)

        self._base_api_mock.request.assert_called_once_with(
            LolStatusApiV3.__name__,
            status.shard_data.__name__,
            region,
            '/lol/status/v3/shard-data'
        )

        self.assertIs(self._expected_return, ret)
