import pytest

from riotwatcher._apis import BaseApi


@pytest.mark.common
@pytest.mark.unit
class TestBaseApi:
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
