import sys
import unittest

import pytest

if sys.version_info > (3, 0):
    from unittest import mock
else:
    import mock


from riotwatcher._apis import BaseApi


class BaseApiTestCase(unittest.TestCase):
    def setUp(self):
        self._expected_preview_return = object()
        self._expected_after_return = object()

        # Mock with returns in the handler
        self._request_handler_mock = mock.MagicMock(name="request_handler")

        self._request_handler_mock.preview_request = mock.MagicMock(
            name="preview_request"
        )
        self._request_handler_mock.preview_request.return_value = (
            self._expected_preview_return
        )
        self._request_handler_mock.after_request = mock.MagicMock(name="after_request")
        self._request_handler_mock.after_request.return_value = (
            self._expected_after_return
        )

        self._request_handler_mock.preview_static_request = mock.MagicMock(
            name="preview_static_request"
        )
        self._request_handler_mock.preview_static_request.return_value = (
            self._expected_preview_return
        )
        self._request_handler_mock.after_static_request = mock.MagicMock(
            name="after_static_request"
        )
        self._request_handler_mock.after_static_request.return_value = (
            self._expected_after_return
        )

        # Mock without returns in the handler
        self._request_handler_mock_no_return = mock.MagicMock(name="request_handler")
        self._request_handler_mock_no_return.preview_request = mock.MagicMock(
            name="preview_request"
        )
        self._request_handler_mock_no_return.after_request = mock.MagicMock(
            name="after_request"
        )
        self._request_handler_mock_no_return.preview_static_request = mock.MagicMock(
            name="preview_static_request"
        )
        self._request_handler_mock_no_return.after_static_request = mock.MagicMock(
            name="after_static_request"
        )
        self._request_handler_mock_no_return.preview_request.return_value = None
        self._request_handler_mock_no_return.after_request.return_value = None
        self._request_handler_mock_no_return.preview_static_request.return_value = None
        self._request_handler_mock_no_return.after_static_request.return_value = None

        self._api_key = "sadf"

        self._mock_api_response = "api_response_xx"

    # BASE TESTS

    def test_base_api_request_preview_handler(self):
        base_api = BaseApi(self._api_key, [self._request_handler_mock])
        endpoint_name = "endpoint_xx"
        method_name = "method_xx"
        region = "region_xx"
        url_ext = "url_xx"
        kwarg = "extra_xx"

        base_api.request(endpoint_name, method_name, region, url_ext, extra=kwarg)

        self._request_handler_mock.preview_request.assert_called_once_with(
            region,
            endpoint_name,
            method_name,
            "https://region_xx.api.riotgames.com%s" % url_ext,
            {"extra": kwarg},
        )

    def test_base_api_request_after_handler_with_preview_return(self):
        base_api = BaseApi(self._api_key, [self._request_handler_mock])
        endpoint_name = "endpoint_xx"
        method_name = "method_xx"
        region = "region_xx"
        url_ext = "url_xx"
        kwarg = "extra_xx"

        ret = base_api.request(endpoint_name, method_name, region, url_ext, extra=kwarg)

        self._request_handler_mock.after_request.assert_called_once_with(
            region,
            endpoint_name,
            method_name,
            "https://region_xx.api.riotgames.com%s" % url_ext,
            self._expected_preview_return,
        )

        self.assertEqual(ret, self._expected_after_return)

    @mock.patch("requests.get")
    def test_base_api_request_after_handler_with_preview_no_return(self, mock_get):
        mock_get.return_value = self._mock_api_response

        base_api = BaseApi(self._api_key, [self._request_handler_mock_no_return])
        endpoint_name = "endpoint_xx"
        method_name = "method_xx"
        region = "region_xx"
        url_ext = "url_xx"
        kwarg = "extra_xx"

        ret = base_api.request(endpoint_name, method_name, region, url_ext, extra=kwarg)

        self._request_handler_mock_no_return.after_request.assert_called_once_with(
            region,
            endpoint_name,
            method_name,
            "https://region_xx.api.riotgames.com%s" % url_ext,
            self._mock_api_response,
        )

        mock_get.assert_called_once_with(
            "https://region_xx.api.riotgames.com%s" % url_ext,
            headers={"X-Riot-Token": self._api_key},
            params={"extra": kwarg},
        )

        self.assertEqual(ret, self._mock_api_response)

    # STATIC TESTS

    def test_base_api_request_static_preview_handler(self):
        base_api = BaseApi(self._api_key, [self._request_handler_mock])
        version = "version_xx"
        locale = "locale_xx"
        url_ext = "url_xx"

        ret = base_api.request_static(version, locale, url_ext)

        self._request_handler_mock.preview_static_request.assert_called_once_with(
            "https://ddragon.leagueoflegends.com/cdn/%s/data/%s/%s.json"
            % (version, locale, url_ext),
            {},
        )

    def test_base_api_request_static_after_handler_with_preview_return(self):
        base_api = BaseApi(self._api_key, [self._request_handler_mock])
        version = "version_xx"
        locale = "locale_xx"
        url_ext = "url_xx"

        ret = base_api.request_static(version, locale, url_ext)

        self._request_handler_mock.after_static_request.assert_called_once_with(
            "https://ddragon.leagueoflegends.com/cdn/%s/data/%s/%s.json"
            % (version, locale, url_ext),
            self._expected_preview_return,
        )

        self.assertEqual(ret, self._expected_after_return)

    @mock.patch("requests.get")
    def test_base_api_request_static_after_handler_with_preview_no_return(
        self, mock_get
    ):
        mock_get.return_value = self._mock_api_response

        base_api = BaseApi(self._api_key, [self._request_handler_mock_no_return])
        version = "version_xx"
        locale = "locale_xx"
        url_ext = "url_xx"

        ret = base_api.request_static(version, locale, url_ext)

        self._request_handler_mock_no_return.after_static_request.assert_called_once_with(
            "https://ddragon.leagueoflegends.com/cdn/%s/data/%s/%s.json"
            % (version, locale, url_ext),
            self._mock_api_response,
        )

        mock_get.assert_called_once_with(
            "https://ddragon.leagueoflegends.com/cdn/%s/data/%s/%s.json"
            % (version, locale, url_ext)
        )

        self.assertEqual(ret, self._mock_api_response)


@pytest.mark.unit
class TestBaseApi(object):
    def test_raw_request_default_timeout(self, mock_get):
        expected_url, expected_query_params = "url", {}
        expected_api_key = "12345"
        expected_headers = {"X-Riot-Token": expected_api_key}
        expected_resp = object()

        api = BaseApi(expected_api_key)

        mock_get.return_value = expected_resp

        resp = api.raw_request(
            "endpoint", "method", "region", expected_url, expected_query_params
        )

        assert resp is expected_resp

        mock_get.assert_called_once_with(
            expected_url, params=expected_query_params, headers=expected_headers
        )

    def test_raw_request_with_timeout(self, mock_get):
        expected_url, expected_query_params = "url", {}
        expected_api_key, expected_timeout = "12345", 5
        expected_headers = {"X-Riot-Token": expected_api_key}
        expected_resp = object()

        api = BaseApi(expected_api_key, timeout=expected_timeout)

        mock_get.return_value = expected_resp

        resp = api.raw_request(
            "endpoint", "method", "region", expected_url, expected_query_params
        )

        assert resp is expected_resp

        mock_get.assert_called_once_with(
            expected_url,
            params=expected_query_params,
            headers=expected_headers,
            timeout=expected_timeout,
        )

    def test_raw_request_static_default_timeout(self, mock_get):
        expected_url, expected_query_params = "url", {}
        expected_resp = object()

        api = BaseApi("12345")

        mock_get.return_value = expected_resp

        resp = api.raw_request_static(expected_url, expected_query_params)

        assert resp is expected_resp

        mock_get.assert_called_once_with(expected_url, params=expected_query_params)

    def test_raw_request_static_with_timeout(self, mock_get):
        expected_url, expected_query_params = "url", {}
        expected_timeout = 5
        expected_resp = object()

        api = BaseApi("12345", timeout=expected_timeout)

        mock_get.return_value = expected_resp

        resp = api.raw_request_static(expected_url, expected_query_params)

        assert resp is expected_resp

        mock_get.assert_called_once_with(
            expected_url, params=expected_query_params, timeout=expected_timeout
        )
