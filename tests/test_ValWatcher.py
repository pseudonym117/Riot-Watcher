import pytest

from riotwatcher import ValWatcher


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
