import unittest
import sys

if sys.version_info > (3, 0):
    from unittest.mock import MagicMock
else:
    from mock import MagicMock
from .. import BaseApi


class BaseApiTestCase(unittest.TestCase):
    def setUp(self):
        self._expected_return = object()

        self._request_handler_mock = MagicMock(name='request_handler')
        self._request_handler_mock.preview_request = MagicMock(name='preview_request')
        self._request_handler_mock.preview_request.return_value = self._expected_return
        self._request_handler_mock.after_request = MagicMock(name='after_request')
        self._request_handler_mock.after_request.return_value = self._expected_return
        self._request_handler_mock.preview_static_request = MagicMock(name='preview_static_request')
        self._request_handler_mock.preview_static_request.return_value = self._expected_return
        self._request_handler_mock.after_static_request = MagicMock(name='after_static_request')
        self._request_handler_mock.after_static_request.return_value = self._expected_return

        self._api_key = 'sadf'

    def test_base_api_request(self):
        base_api = BaseApi(self._api_key, [self._request_handler_mock])
        endpoint_name = 'endpoint_xx'
        method_name = 'method_xx'
        region = 'region_xx'
        url_ext = 'url_xx'
        kwarg = 'extra_xx'

        base_api.request(endpoint_name, method_name, region, url_ext, extra=kwarg)

        self._request_handler_mock.preview_request.assert_called_once_with(
            region,
            endpoint_name,
            method_name,
            'https://region_xx.api.riotgames.com%s' % url_ext,
            {'extra': kwarg}
        )

        self._request_handler_mock.after_request.assert_called_once_with(
            region,
            endpoint_name,
            method_name,
            'https://region_xx.api.riotgames.com%s' % url_ext,
            self._expected_return
        )

    def test_base_api_static_request(self):
        base_api = BaseApi(self._api_key, [self._request_handler_mock])
        version = 'version_xx'
        locale = 'locale_xx'
        url_ext = 'url_xx'

        base_api.request_static(version, locale, url_ext)

        self._request_handler_mock.preview_static_request.assert_called_once_with(
            version,
            locale,
            'http://ddragon.leagueoflegends.com/cdn/%s/data/%s/%s.json' % (version, locale, url_ext),
        )

        self._request_handler_mock.after_static_request.assert_called_once_with(
            version,
            locale,
            'http://ddragon.leagueoflegends.com/cdn/%s/data/%s/%s.json' % (version, locale, url_ext),
            self._expected_return
        )

    def test_base_api_version_request(self):
        base_api = BaseApi(self._api_key, [self._request_handler_mock])
        endpoint_name = 'endpoint_xx'
        method_name = 'method_xx'
        region = 'region_xx'

        base_api.request_version(endpoint_name, method_name, region)

        self._request_handler_mock.preview_request.assert_called_once_with(
            region,
            endpoint_name,
            method_name,
            'https://ddragon.leagueoflegends.com/realms/%s.json' % region,
            {}
        )

        self._request_handler_mock.after_request.assert_called_once_with(
            region,
            endpoint_name,
            method_name,
            'https://ddragon.leagueoflegends.com/realms/%s.json' % region,
            self._expected_return
        )
