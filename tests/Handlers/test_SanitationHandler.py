import pytest

from riotwatcher.Handlers import IllegalArgumentError, SanitationHandler


@pytest.mark.common
@pytest.mark.unit
class TestSanitationHandler:
    @pytest.mark.parametrize(
        "region", ["na1", "Na1", "aN1", "enue", "americas", "europe", "euw1"]
    )
    def test_valid_region_passes(self, region):
        handler = SanitationHandler()

        handler.preview_request(region, None, None, None, None)

    @pytest.mark.parametrize("region", ["", "google.com/?stolen=", "+", "na1?"])
    def test_invalid_region_fails(self, region):
        handler = SanitationHandler()

        with pytest.raises(IllegalArgumentError):
            handler.preview_request(region, None, None, None, None)
