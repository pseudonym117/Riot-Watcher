from collections import namedtuple
import datetime
import json
import unittest.mock as mock
from typing import T

import pytest

real_datetime_class = datetime.datetime


class DatetimeSubclassMeta(type):
    @classmethod
    def __instancecheck__(mcs, obj) -> bool:
        return isinstance(obj, real_datetime_class)


class BaseMockDatetime(real_datetime_class):
    @classmethod
    def now(cls) -> datetime.datetime:
        if hasattr(cls, "_now") and cls._now is not None:
            return cls._now
        else:
            return real_datetime_class.now()

    @classmethod
    def set_now(cls, datetime_value: datetime.datetime):
        cls._now = datetime_value


MockedDatetime = DatetimeSubclassMeta("datetime", (BaseMockDatetime,), {})


@pytest.fixture
def mock_datetime(monkeypatch):
    with monkeypatch.context() as ctx:
        ctx.setattr(datetime, "datetime", MockedDatetime)
        yield

        del MockedDatetime._now


@pytest.fixture
def mock_get(monkeypatch) -> mock.MagicMock:
    with monkeypatch.context() as m:
        mock_req = mock.MagicMock()
        m.setattr("requests.Session.get", mock_req)

        yield mock_req


@pytest.fixture
def reset_globals():
    from riotwatcher._apis import UrlConfig

    initial = UrlConfig.root_url
    yield
    UrlConfig.root_url = initial


class MockContext:
    def __init__(
        self, api_key: str, mock_get: mock.MagicMock, watcher, kernel_url: str
    ):
        self._api_key = api_key
        self._expected_response = {"has_value": "yes"}
        self._get = mock_get
        self._watcher = watcher
        self._kernel_url = kernel_url

        mock_response = mock.MagicMock()
        mock_response.text = json.dumps(self._expected_response)

        self.get.return_value = mock_response

    @property
    def api_key(self) -> str:
        return self._api_key

    @property
    def expected_response(self) -> dict:
        return self._expected_response

    @property
    def get(self) -> mock.MagicMock:
        return self._get

    @property
    def watcher(self):
        return self._watcher

    def verify_api_call(
        self, region: str, endpoint: str, query_params: dict, actual_response: T
    ):
        assert self.expected_response == actual_response

        if self._kernel_url:
            base_url = self._kernel_url
            query_params["platform"] = region
        else:
            base_url = f"https://{region}.api.riotgames.com"

        self.get.assert_called_once_with(
            f"{base_url}{endpoint}",
            params=query_params,
            headers={"X-Riot-Token": self.api_key},
        )


@pytest.fixture(params=(None, "https://kernel-proxy:8080"))
@pytest.mark.usefixtures("reset_globals")
def lol_context(mock_get: mock.MagicMock, request) -> MockContext:
    import riotwatcher

    api_key = "abcdefg"
    yield MockContext(
        api_key,
        mock_get,
        riotwatcher.LolWatcher(api_key, kernel_url=request.param),
        request.param,
    )


@pytest.fixture
@pytest.mark.usefixtures("reset_globals")
def tft_context(mock_get: mock.MagicMock) -> MockContext:
    import riotwatcher

    api_key = "abcdefg"
    yield MockContext(
        api_key, mock_get, riotwatcher.TftWatcher(api_key), None,
    )


@pytest.fixture
@pytest.mark.usefixtures("reset_globals")
def lor_context(mock_get: mock.MagicMock) -> MockContext:
    import riotwatcher

    api_key = "abcdefg"
    yield MockContext(
        api_key, mock_get, riotwatcher.LorWatcher(api_key), None,
    )


@pytest.fixture
@pytest.mark.usefixtures("reset_globals")
def riot_context(mock_get: mock.MagicMock) -> MockContext:
    import riotwatcher

    api_key = "abcdefg"
    yield MockContext(
        api_key, mock_get, riotwatcher.RiotWatcher(api_key), None,
    )


@pytest.fixture
@pytest.mark.usefixtures("reset_globals")
def val_context(mock_get: mock.MagicMock) -> MockContext:
    import riotwatcher

    api_key = "abcdefg"
    yield MockContext(
        api_key, mock_get, riotwatcher.ValWatcher(api_key), None,
    )


RegionRemap = namedtuple("RegionRemap", ["original", "to"])


@pytest.fixture(
    params=[
        ("na1", "americas"),
        ("NA1", "americas"),
        ("br1", "americas"),
        ("la1", "americas"),
        ("la2", "americas"),
        ("oc1", "americas"),
        ("euw1", "europe"),
        ("eun1", "europe"),
        ("tr1", "europe"),
        ("ru", "europe"),
        ("jp1", "asia"),
        ("kr", "asia"),
    ]
)
def region_remap(request):
    return RegionRemap(*request.param)
