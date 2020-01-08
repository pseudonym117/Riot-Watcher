import pytest

from riotwatcher import RiotWatcher


@pytest.mark.usefixtures("reset_globals")
class TestRiotWatcher:
    def test_require_api_key_or_kernel(self):
        with pytest.raises(ValueError):
            RiotWatcher()

    def test_allows_positional_api_key(self):
        RiotWatcher("RGAPI-this-is-a-fake")

    def test_allows_keyword_api_key(self):
        RiotWatcher(api_key="RGAPI-this-is-a-fake")

    def test_allows_kernel_url(self):
        RiotWatcher(kernel_url="https://fake-kernel-server")
