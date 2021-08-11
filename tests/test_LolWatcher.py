import pytest

from riotwatcher import LolWatcher
from riotwatcher._apis.league_of_legends import (
    MatchApiV4,
    MatchApiV5,
    LolStatusApiV3,
    LolStatusApiV4,
)


@pytest.mark.lol
@pytest.mark.usefixtures("reset_globals")
class TestLolWatcher:
    def test_require_api_key_or_kernel(self):
        with pytest.raises(ValueError):
            LolWatcher()

    def test_allows_positional_api_key(self):
        LolWatcher("RGAPI-this-is-a-fake")

    def test_allows_keyword_api_key(self):
        LolWatcher(api_key="RGAPI-this-is-a-fake")

    def test_allows_kernel_url(self):
        LolWatcher(kernel_url="https://fake-kernel-server")

    def test_defaults_match_v4(self):
        watcher = LolWatcher(api_key="RGAPI-this-is-a-fake")
        assert isinstance(watcher.match, MatchApiV4)

    def test_uses_match_v4_when_false(self):
        watcher = LolWatcher(api_key="RGAPI-this-is-a-fake", default_match_v5=False)
        assert isinstance(watcher.match, MatchApiV4)

    def test_uses_match_v5_when_true(self):
        watcher = LolWatcher(api_key="RGAPI-this-is-a-fake", default_match_v5=True)
        assert isinstance(watcher.match, MatchApiV5)

    def test_defaults_status_v3(self):
        watcher = LolWatcher(api_key="RGAPI-this-is-a-fake")
        assert isinstance(watcher.lol_status, LolStatusApiV3)

    def test_uses_status_v3_when_false(self):
        watcher = LolWatcher(api_key="RGAPI-this-is-a-fake", default_status_v4=False)
        assert isinstance(watcher.lol_status, LolStatusApiV3)

    def test_uses_status_v4_when_true(self):
        watcher = LolWatcher(api_key="RGAPI-this-is-a-fake", default_status_v4=True)
        assert isinstance(watcher.lol_status, LolStatusApiV4)
