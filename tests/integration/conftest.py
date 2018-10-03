
import sys

import pytest

if sys.version_info > (3, 0):
    import unittest.mock as mock
else:
    import mock

@pytest.fixture
def mock_get(monkeypatch):
    with monkeypatch.context() as m:
        mock_req = mock.MagicMock()
        m.setattr('requests.get', mock_req)

        yield mock_req

class MockContext(object):
    def __init__(self, api_key, mock_get, watcher):
        self._api_key = api_key
        self._get = mock_get
        self._watcher = watcher
    
    @property
    def api_key(self):
        return self._api_key

    @property
    def get(self):
        return self._get
    
    @property
    def watcher(self):
        return self._watcher

@pytest.fixture
def mock_context(mock_get):
    import riotwatcher

    api_key = 'abcdefg'
    return MockContext(api_key, mock_get, riotwatcher.RiotWatcher(api_key))
