import pytest

from riotwatcher import TftWatcher, IllegalArgumentError


@pytest.mark.tft
@pytest.mark.usefixtures("reset_globals")
class TestTftWatcher:
    def test_require_api_key(self):
        with pytest.raises(ValueError):
            TftWatcher()

    def test_allows_positional_api_key(self):
        TftWatcher("RGAPI-this-is-a-fake")

    def test_allows_keyword_api_key(self):
        TftWatcher(api_key="RGAPI-this-is-a-fake")

    def test_stealing_api_key_doesnt_work(self):
        watcher = TftWatcher(api_key="RGAPI-this-is-a-fake")
        with pytest.raises(IllegalArgumentError):
            watcher.summoner.by_puuid("example.com/?stolen-request=", "fake-puuid")
