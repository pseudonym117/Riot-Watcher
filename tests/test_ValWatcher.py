import pytest

from riotwatcher import ValWatcher, IllegalArgumentError


@pytest.mark.val
@pytest.mark.usefixtures("reset_globals")
class TestValWatcher:
    def test_require_api_key(self):
        with pytest.raises(ValueError):
            ValWatcher(None)

    def test_allows_positional_api_key(self):
        ValWatcher("RGAPI-this-is-a-fake")

    def test_allows_keyword_api_key(self):
        ValWatcher(api_key="RGAPI-this-is-a-fake")

    def test_stealing_api_key_doesnt_work(self):
        watcher = ValWatcher(api_key="RGAPI-this-is-a-fake")
        with pytest.raises(IllegalArgumentError):
            watcher.match.by_id("example.com/?stolen-request=", "fake-match")
