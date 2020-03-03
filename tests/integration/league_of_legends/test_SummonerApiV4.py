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
class TestSummonerApiV4:
    @pytest.mark.parametrize("encrypted_account_id", ["12345", "99999999999999999999"])
    def test_by_account(self, lol_context, region, encrypted_account_id):
        actual_response = lol_context.watcher.summoner.by_account(
            region, encrypted_account_id
        )

        lol_context.verify_api_call(
            region,
            f"/lol/summoner/v4/summoners/by-account/{encrypted_account_id}",
            {},
            actual_response,
        )

    @pytest.mark.parametrize("summoner_name", ["pseudonym117", "Riot Tuxedo"])
    def test_by_name(self, lol_context, region, summoner_name):
        actual_response = lol_context.watcher.summoner.by_name(region, summoner_name)

        lol_context.verify_api_call(
            region,
            f"/lol/summoner/v4/summoners/by-name/{summoner_name}",
            {},
            actual_response,
        )

    @pytest.mark.parametrize("encrypted_puuid", ["12345", "99999999999999999999"])
    def test_by_puuid(self, lol_context, region, encrypted_puuid):
        actual_response = lol_context.watcher.summoner.by_puuid(region, encrypted_puuid)

        lol_context.verify_api_call(
            region,
            f"/lol/summoner/v4/summoners/by-puuid/{encrypted_puuid}",
            {},
            actual_response,
        )

    @pytest.mark.parametrize("encrypted_summoner_id", ["12345", "99999999999999999999"])
    def test_by_id(self, lol_context, region, encrypted_summoner_id):
        actual_response = lol_context.watcher.summoner.by_id(
            region, encrypted_summoner_id
        )

        lol_context.verify_api_call(
            region,
            f"/lol/summoner/v4/summoners/{encrypted_summoner_id}",
            {},
            actual_response,
        )
