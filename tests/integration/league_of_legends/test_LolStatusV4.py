import pytest


@pytest.mark.lol
@pytest.mark.integration
@pytest.mark.parametrize(
    "region",
    [
        "br1",
        "eun1",
        "euw1",
        "jp1",
        "kr",
        "la1",
        "la2",
        "na",
        "na1",
        "oc1",
        "tr1",
        "ru",
        "pbe1",
    ],
)
class TestStatusApiV4:
    def test_platform_data(self, lol_context, region):
        actual_response = lol_context.watcher.lol_status_v4.platform_data(region)

        lol_context.verify_api_call(
            region, "/lol/status/v4/platform-data", {}, actual_response
        )
