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
class TestLeagueApi:
    def test_challenger(self, tft_context, region):
        actual_response = tft_context.watcher.league.challenger(region)

        tft_context.verify_api_call(
            region, "/tft/league/v1/challenger", {}, actual_response
        )

    @pytest.mark.parametrize(
        "encrypted_summoner_id",
        ["50", "424299938281", "9999999999999999999999", "rtbf12345"],
    )
    def test_by_summoner(self, tft_context, region, encrypted_summoner_id):
        actual_response = tft_context.watcher.league.by_summoner(
            region, encrypted_summoner_id
        )

        tft_context.verify_api_call(
            region,
            f"/tft/league/v1/entries/by-summoner/{encrypted_summoner_id}",
            {},
            actual_response,
        )

    @pytest.mark.parametrize("tier", ["IRON", "SILVER", "DIAMOND"])
    @pytest.mark.parametrize("division", ["I", "IV"])
    @pytest.mark.parametrize("page", [2, 420])
    def test_entries(self, tft_context, region, tier, division, page):
        actual_response = tft_context.watcher.league.entries(
            region, tier, division, page=page
        )

        tft_context.verify_api_call(
            region,
            f"/tft/league/v1/entries/{tier}/{division}",
            {"page": page},
            actual_response,
        )

    def test_grandmaster(self, tft_context, region):
        actual_response = tft_context.watcher.league.grandmaster(region)

        tft_context.verify_api_call(
            region, "/tft/league/v1/grandmaster", {}, actual_response
        )

    @pytest.mark.parametrize("league_id", [1, 500, 99999999999999])
    def test_by_id(self, tft_context, region, league_id):
        actual_response = tft_context.watcher.league.by_id(region, league_id)

        tft_context.verify_api_call(
            region, f"/tft/league/v1/leagues/{league_id}", {}, actual_response
        )

    def test_master(self, tft_context, region):
        actual_response = tft_context.watcher.league.master(region)

        tft_context.verify_api_call(
            region, "/tft/league/v1/master", {}, actual_response
        )

    @pytest.mark.parametrize("queue", ["RANKED_TFT_TURBO"])
    def test_rated_ladders(self, tft_context, region, queue):
        actual_response = tft_context.watcher.league.rated_ladders(region, queue)

        tft_context.verify_api_call(
            region, f"/tft/league/v1/rated-ladders/{queue}/top", {}, actual_response
        )
