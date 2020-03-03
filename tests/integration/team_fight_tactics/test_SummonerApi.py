import pytest


@pytest.mark.tft
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
class TestSummonerApi:
    @pytest.mark.parametrize("encrypted_account_id", ["12345", "99999999999999999999"])
    def test_by_account(self, tft_context, region, encrypted_account_id):
        actual_response = tft_context.watcher.summoner.by_account(
            region, encrypted_account_id
        )

        tft_context.verify_api_call(
            region,
            f"/tft/summoner/v1/summoners/by-account/{encrypted_account_id}",
            {},
            actual_response,
        )

    @pytest.mark.parametrize("summoner_name", ["pseudonym117", "Riot Tuxedo"])
    def test_by_name(self, tft_context, region, summoner_name):
        actual_response = tft_context.watcher.summoner.by_name(region, summoner_name)

        tft_context.verify_api_call(
            region,
            f"/tft/summoner/v1/summoners/by-name/{summoner_name}",
            {},
            actual_response,
        )

    @pytest.mark.parametrize("puuid", ["12345", "99999999999999999999"])
    def test_by_puuid(self, tft_context, region, puuid):
        actual_response = tft_context.watcher.summoner.by_puuid(region, puuid)

        tft_context.verify_api_call(
            region, f"/tft/summoner/v1/summoners/by-puuid/{puuid}", {}, actual_response,
        )

    @pytest.mark.parametrize("encrypted_summoner_id", ["12345", "99999999999999999999"])
    def test_by_id(self, tft_context, region, encrypted_summoner_id):
        actual_response = tft_context.watcher.summoner.by_id(
            region, encrypted_summoner_id
        )

        tft_context.verify_api_call(
            region,
            f"/tft/summoner/v1/summoners/{encrypted_summoner_id}",
            {},
            actual_response,
        )
