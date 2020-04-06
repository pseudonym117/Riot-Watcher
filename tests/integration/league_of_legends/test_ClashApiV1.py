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
class TestClashApiV1(object):
    @pytest.mark.parametrize("summoner_id", ["424299938281", "rtbf12345"])
    def test_by_summoner(self, lol_context, region, summoner_id):
        actual_response = lol_context.watcher.clash.by_summoner(region, summoner_id)

        lol_context.verify_api_call(
            region,
            f"/lol/clash/v1/players/by-summoner/{summoner_id}",
            {},
            actual_response,
        )

    @pytest.mark.parametrize("team_id", ["50", "7340158"])
    def test_by_team(self, lol_context, region, team_id):
        actual_response = lol_context.watcher.clash.by_team(region, team_id)

        lol_context.verify_api_call(
            region, f"/lol/clash/v1/teams/{team_id}", {}, actual_response,
        )

    def test_tournaments(self, lol_context, region):
        actual_response = lol_context.watcher.clash.tournaments(region)

        lol_context.verify_api_call(
            region, f"/lol/clash/v1/tournaments", {}, actual_response,
        )

    @pytest.mark.parametrize("team_id", ["50", "7340158"])
    def test_tournament_by_team(self, lol_context, region, team_id):
        actual_response = lol_context.watcher.clash.tournament_by_team(region, team_id)

        lol_context.verify_api_call(
            region, f"/lol/clash/v1/tournaments/by-team/{team_id}", {}, actual_response,
        )

    @pytest.mark.parametrize("tournament_id", ["123", "420"])
    def test_by_tournament(self, lol_context, region, tournament_id):
        actual_response = lol_context.watcher.clash.by_tournament(region, tournament_id)

        lol_context.verify_api_call(
            region, f"/lol/clash/v1/tournaments/{tournament_id}", {}, actual_response,
        )
