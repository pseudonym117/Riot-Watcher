import pytest


@pytest.mark.tft
@pytest.mark.integration
@pytest.mark.parametrize(
    "region", ["EUROPE", "ASIA", "AMERICAS",],
)
class TestMatchApi:
    @pytest.mark.parametrize("puuid", ["12345", "99999999999999999999"])
    @pytest.mark.parametrize("count", [5, 50, 200])
    def test_by_puuid(self, tft_context, region, puuid, count):
        actual_response = tft_context.watcher.match.by_puuid(region, puuid, count=count)

        tft_context.verify_api_call(
            region,
            f"/tft/match/v1/matches/by-puuid/{puuid}/ids",
            {"count": count},
            actual_response,
        )

    @pytest.mark.parametrize("match_id", [0, 54321, 3232323232323223])
    def test_by_id(self, tft_context, region, match_id):
        actual_response = tft_context.watcher.match.by_id(region, match_id)

        tft_context.verify_api_call(
            region, f"/tft/match/v1/matches/{match_id}", {}, actual_response
        )


@pytest.mark.tft
@pytest.mark.integration
class TestMatchApiRemapping:
    def test_by_puuid(self, tft_context, region_remap):
        puuid = "12345"
        actual_response = tft_context.watcher.match.by_puuid(
            region_remap.original, puuid
        )

        tft_context.verify_api_call(
            region_remap.to,
            f"/tft/match/v1/matches/by-puuid/{puuid}/ids",
            {"count": 20},
            actual_response,
        )

    def test_by_id(self, tft_context, region_remap):
        match_id = "EUW_123"
        actual_response = tft_context.watcher.match.by_id(
            region_remap.original, match_id
        )

        tft_context.verify_api_call(
            region_remap.to, f"/tft/match/v1/matches/{match_id}", {}, actual_response
        )
