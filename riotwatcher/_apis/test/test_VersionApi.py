import unittest
import sys

if sys.version_info > (3, 0):
    from unittest.mock import MagicMock
else:
    from mock import MagicMock

from .. import VersionApi


class VersionApiTestCase(unittest.TestCase):
    def setUp(self):
        self._expected_return = object()

        self._base_api_mock = MagicMock(name='base_api')
        self._base_api_mock.request_version = MagicMock(name='request_version')
        self._base_api_mock.request_version.return_value = self._expected_return

    def test_all_champions_default(self):
        version_api = VersionApi(self._base_api_mock)

        region = 'euw1'

        ret = version_api.for_region(region)

        self._base_api_mock.request_version.assert_called_once_with(region)

        self.assertIs(self._expected_return, ret)
