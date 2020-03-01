import pytest

from riotwatcher import LolWatcher


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
