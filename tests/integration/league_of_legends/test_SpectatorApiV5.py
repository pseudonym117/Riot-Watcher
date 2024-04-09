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
class TestSpectatorApiV5:
    @pytest.mark.parametrize("encrypted_puuid", ["12345", "99999999999999999"])
    def test_by_summoner(self, lol_context, region, encrypted_puuid):
        actual_response = lol_context.watcher.spectator.by_summoner(
            region, encrypted_puuid
        )

        lol_context.verify_api_call(
            region,
            f"/lol/spectator/v5/active-games/by-summoner/{encrypted_puuid}",
            {},
            actual_response,
        )

    def test_featured_games(self, lol_context, region):
        actual_response = lol_context.watcher.spectator.featured_games(region)

        lol_context.verify_api_call(
            region, "/lol/spectator/v5/featured-games", {}, actual_response
        )
