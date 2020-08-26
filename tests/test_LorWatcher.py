import pytest

from riotwatcher import LorWatcher


@pytest.mark.lor
@pytest.mark.usefixtures("reset_globals")
class TestLorWatcher:
    def test_require_api_key(self):
        with pytest.raises(ValueError):
            LorWatcher()

    def test_allows_positional_api_key(self):
        LorWatcher("RGAPI-this-is-a-fake")

    def test_allows_keyword_api_key(self):
        LorWatcher(api_key="RGAPI-this-is-a-fake")
