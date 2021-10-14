import pytest

from riotwatcher import RiotWatcher, IllegalArgumentError


@pytest.mark.riot
@pytest.mark.usefixtures("reset_globals")
class TestRiotWatcher:
    def test_require_api_key(self):
        with pytest.raises(ValueError):
            RiotWatcher(None)

    def test_allows_positional_api_key(self):
        RiotWatcher("RGAPI-this-is-a-fake")

    def test_allows_keyword_api_key(self):
        RiotWatcher(api_key="RGAPI-this-is-a-fake")

    def test_stealing_api_key_doesnt_work(self):
        watcher = RiotWatcher(api_key="RGAPI-this-is-a-fake")
        with pytest.raises(IllegalArgumentError):
            watcher.account.by_puuid("example.com/?stolen-request=", "fake-puuid")
