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
class TestThirdPartyCodeApiV4:
    @pytest.mark.parametrize("encrypted_summoner_id", ["12345", "99999999999999999"])
    def test_by_summoner(self, lol_context, region, encrypted_summoner_id):
        actual_response = lol_context.watcher.third_party_code.by_summoner(
            region, encrypted_summoner_id
        )

        lol_context.verify_api_call(
            region,
            f"/lol/platform/v4/third-party-code/by-summoner/{encrypted_summoner_id}",
            {},
            actual_response,
        )
