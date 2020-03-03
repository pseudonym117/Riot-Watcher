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
class TestChampionApiV3:
    def test_rotations(self, lol_context, region):
        actual_response = lol_context.watcher.champion.rotations(region)

        lol_context.verify_api_call(
            region, "/lol/platform/v3/champion-rotations", {}, actual_response
        )
