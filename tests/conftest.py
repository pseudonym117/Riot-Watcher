import datetime
import sys

import pytest

if sys.version_info > (3, 0):
    import unittest.mock as mock
else:
    import mock


real_datetime_class = datetime.datetime


class DatetimeSubclassMeta(type):
    @classmethod
    def __instancecheck__(mcs, obj):
        return isinstance(obj, real_datetime_class)


class BaseMockDatetime(real_datetime_class):
    @classmethod
    def now(cls):
        if hasattr(cls, "_now") and cls._now is not None:
            return cls._now
        else:
            return real_datetime_class.now()

    @classmethod
    def set_now(cls, datetime_value):
        cls._now = datetime_value


MockedDatetime = DatetimeSubclassMeta("datetime", (BaseMockDatetime,), {})


@pytest.fixture
def mock_datetime(monkeypatch):
    with monkeypatch.context() as ctx:
        ctx.setattr(datetime, "datetime", MockedDatetime)
        yield

        del MockedDatetime._now


@pytest.fixture
def mock_get(monkeypatch):
    with monkeypatch.context() as m:
        mock_req = mock.MagicMock()
        m.setattr("requests.get", mock_req)

        yield mock_req


class MockContext(object):
    def __init__(self, api_key, mock_get, watcher, kernel_url):
        self._api_key = api_key
        self._expected_response = {"has_value": "yes"}
        self._get = mock_get
        self._watcher = watcher
        self._kernel_url = kernel_url

        mock_response = mock.MagicMock()
        mock_response.json.return_value = self._expected_response

        self.get.return_value = mock_response

    @property
    def api_key(self):
        return self._api_key

    @property
    def expected_response(self):
        return self._expected_response

    @property
    def get(self):
        return self._get

    @property
    def watcher(self):
        return self._watcher

    def verify_api_call(self, region, endpoint, query_params, actual_response):
        assert self.expected_response == actual_response

        if self._kernel_url:
            base_url = self._kernel_url
            query_params["region"] = region
        else:
            base_url = "https://{region}.api.riotgames.com/lol".format(region=region)

        self.get.assert_called_once_with(
            "{base_url}{endpoint}".format(base_url=base_url, endpoint=endpoint),
            params=query_params,
            headers={"X-Riot-Token": self.api_key},
        )

    def base_api_url_and_params(self, region):
        if self._kernel_url:
            return self._kernel_url, {"region": region}
        else:
            return "https://{region}.api.riotgames.com/lol".format(region=region), {}


@pytest.fixture(params=(None, "https://kernel-proxy:8080"))
def mock_context(mock_get, request):
    import riotwatcher

    api_key = "abcdefg"
    return MockContext(
        api_key,
        mock_get,
        riotwatcher.RiotWatcher(api_key, kernel_url=request.param),
        request.param,
    )
