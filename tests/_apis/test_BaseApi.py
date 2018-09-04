import unittest
import sys

if sys.version_info > (3, 0):
    from unittest.mock import MagicMock
    from unittest import mock
else:
    from mock import MagicMock
    import mock

    
from riotwatcher._apis import BaseApi


class BaseApiTestCase(unittest.TestCase):
    def setUp(self):
        self._expected_preview_return = object()
        self._expected_after_return = object()

        # Mock with returns in the handler
        self._request_handler_mock = MagicMock(name='request_handler')

        self._request_handler_mock.preview_request = MagicMock(name='preview_request')
        self._request_handler_mock.preview_request.return_value = self._expected_preview_return
        self._request_handler_mock.after_request = MagicMock(name='after_request')
        self._request_handler_mock.after_request.return_value = self._expected_after_return

        self._request_handler_mock.preview_static_request = MagicMock(name='preview_static_request')
        self._request_handler_mock.preview_static_request.return_value = self._expected_preview_return
        self._request_handler_mock.after_static_request = MagicMock(name='after_static_request')
        self._request_handler_mock.after_static_request.return_value = self._expected_after_return

        # Mock without returns in the handler
        self._request_handler_mock_no_return = MagicMock(name='request_handler')
        self._request_handler_mock_no_return.preview_request = MagicMock(name='preview_request')
        self._request_handler_mock_no_return.after_request = MagicMock(name='after_request')
        self._request_handler_mock_no_return.preview_static_request = MagicMock(name='preview_static_request')
        self._request_handler_mock_no_return.after_static_request = MagicMock(name='after_static_request')
        self._request_handler_mock_no_return.preview_request.return_value = None
        self._request_handler_mock_no_return.after_request.return_value = None
        self._request_handler_mock_no_return.preview_static_request.return_value = None
        self._request_handler_mock_no_return.after_static_request.return_value = None

        self._api_key = 'sadf'

        self._mock_api_response = 'api_response_xx'

    # BASE TESTS

    def test_base_api_request_preview_handler(self):
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

    def test_base_api_request_after_handler_with_preview_return(self):
        base_api = BaseApi(self._api_key, [self._request_handler_mock])
        endpoint_name = 'endpoint_xx'
        method_name = 'method_xx'
        region = 'region_xx'
        url_ext = 'url_xx'
        kwarg = 'extra_xx'

        ret = base_api.request(endpoint_name, method_name, region, url_ext, extra=kwarg)

        self._request_handler_mock.after_request.assert_called_once_with(
            region,
            endpoint_name,
            method_name,
            'https://region_xx.api.riotgames.com%s' % url_ext,
            self._expected_preview_return
        )

        self.assertEqual(ret, self._expected_after_return)

    @mock.patch('requests.get')
    def test_base_api_request_after_handler_with_preview_no_return(self, mock_get):
        mock_get.return_value = self._mock_api_response

        base_api = BaseApi(self._api_key, [self._request_handler_mock_no_return])
        endpoint_name = 'endpoint_xx'
        method_name = 'method_xx'
        region = 'region_xx'
        url_ext = 'url_xx'
        kwarg = 'extra_xx'

        ret = base_api.request(endpoint_name, method_name, region, url_ext, extra=kwarg)

        self._request_handler_mock_no_return.after_request.assert_called_once_with(
            region,
            endpoint_name,
            method_name,
            'https://region_xx.api.riotgames.com%s' % url_ext,
            self._mock_api_response
        )

        mock_get.assert_called_once_with(
            'https://region_xx.api.riotgames.com%s' % url_ext,
            headers={'X-Riot-Token': self._api_key},
            params={'extra': kwarg}
        )

        self.assertEqual(ret, self._mock_api_response)

    # STATIC TESTS

    def test_base_api_request_static_preview_handler(self):
        base_api = BaseApi(self._api_key, [self._request_handler_mock])
        version = 'version_xx'
        locale = 'locale_xx'
        url_ext = 'url_xx'

        ret = base_api.request_static(version, locale, url_ext)

        self._request_handler_mock.preview_static_request.assert_called_once_with(
            version,
            locale,
            'https://ddragon.leagueoflegends.com/cdn/%s/data/%s/%s.json' % (version, locale, url_ext)
        )

    def test_base_api_request_static_after_handler_with_preview_return(self):
        base_api = BaseApi(self._api_key, [self._request_handler_mock])
        version = 'version_xx'
        locale = 'locale_xx'
        url_ext = 'url_xx'

        ret = base_api.request_static(version, locale, url_ext)

        self._request_handler_mock.after_static_request.assert_called_once_with(
            version,
            locale,
            'https://ddragon.leagueoflegends.com/cdn/%s/data/%s/%s.json' % (version, locale, url_ext),
            self._expected_preview_return
        )

        self.assertEqual(ret, self._expected_after_return)

    @mock.patch('requests.get')
    def test_base_api_request_static_after_handler_with_preview_no_return(self, mock_get):
        mock_get.return_value = self._mock_api_response

        base_api = BaseApi(self._api_key, [self._request_handler_mock_no_return])
        version = 'version_xx'
        locale = 'locale_xx'
        url_ext = 'url_xx'

        ret = base_api.request_static(version, locale, url_ext)

        self._request_handler_mock_no_return.after_static_request.assert_called_once_with(
            version,
            locale,
            'https://ddragon.leagueoflegends.com/cdn/%s/data/%s/%s.json' % (version, locale, url_ext),
            self._mock_api_response
        )

        mock_get.assert_called_once_with(
            'https://ddragon.leagueoflegends.com/cdn/%s/data/%s/%s.json' % (version, locale, url_ext),
        )

        self.assertEqual(ret, self._mock_api_response)

    # VERSION TESTS

    def test_base_api_request_version_preview_handler(self):
        base_api = BaseApi(self._api_key, [self._request_handler_mock])
        region = 'region_xx'

        ret = base_api.request_version(region)

        self._request_handler_mock.preview_static_request.assert_called_once_with(
            '',
            '',
            'https://ddragon.leagueoflegends.com/realms/%s.json' % region
        )

    def test_base_api_request_version_after_handler_with_preview_return(self):
        base_api = BaseApi(self._api_key, [self._request_handler_mock])
        region = 'region_xx'

        ret = base_api.request_version(region)

        self._request_handler_mock.after_static_request.assert_called_once_with(
            '',
            '',
            'https://ddragon.leagueoflegends.com/realms/%s.json' % region,
            self._expected_preview_return
        )

        self.assertEqual(ret, self._expected_after_return)

    @mock.patch('requests.get')
    def test_base_api_request_version_after_handler_with_preview_no_return(self, mock_get):
        mock_get.return_value = self._mock_api_response

        base_api = BaseApi(self._api_key, [self._request_handler_mock_no_return])
        region = 'region_xx'

        ret = base_api.request_version(region)

        self._request_handler_mock_no_return.after_static_request.assert_called_once_with(
            '',
            '',
            'https://ddragon.leagueoflegends.com/realms/%s.json' % region,
            self._mock_api_response
        )

        mock_get.assert_called_once_with(
            'https://ddragon.leagueoflegends.com/realms/%s.json' % region,
        )

        self.assertEqual(ret, self._mock_api_response)
