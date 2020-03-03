import pytest


queues = ("RANKED_SOLO_5x5", "RANKED_FLEX_SR", "RANKED_FLEX_TT", "RANKED_TFT")


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
class TestLeagueApiV4:
    @pytest.mark.parametrize("queue", queues)
    def test_challenger_by_queue(self, lol_context, region, queue):
        actual_response = lol_context.watcher.league.challenger_by_queue(region, queue)

        lol_context.verify_api_call(
            region,
            f"/lol/league/v4/challengerleagues/by-queue/{queue}",
            {},
            actual_response,
        )

    @pytest.mark.parametrize("queue", queues)
    def test_grandmaster_by_queue(self, lol_context, region, queue):
        actual_response = lol_context.watcher.league.grandmaster_by_queue(region, queue)

        lol_context.verify_api_call(
            region,
            f"/lol/league/v4/grandmasterleagues/by-queue/{queue}",
            {},
            actual_response,
        )

    @pytest.mark.parametrize("queue", queues)
    def test_masters_by_queue(self, lol_context, region, queue):
        actual_response = lol_context.watcher.league.masters_by_queue(region, queue)

        lol_context.verify_api_call(
            region,
            f"/lol/league/v4/masterleagues/by-queue/{queue}",
            {},
            actual_response,
        )

    @pytest.mark.parametrize("league_id", [1, 500, 99999999999999])
    def test_by_id(self, lol_context, region, league_id):
        actual_response = lol_context.watcher.league.by_id(region, league_id)

        lol_context.verify_api_call(
            region, f"/lol/league/v4/leagues/{league_id}", {}, actual_response,
        )

    @pytest.mark.parametrize(
        "encrypted_summoner_id",
        ["50", "424299938281", "9999999999999999999999", "rtbf12345"],
    )
    def test_by_summoner(self, lol_context, region, encrypted_summoner_id):
        actual_response = lol_context.watcher.league.by_summoner(
            region, encrypted_summoner_id
        )

        lol_context.verify_api_call(
            region,
            f"/lol/league/v4/entries/by-summoner/{encrypted_summoner_id}",
            {},
            actual_response,
        )

    @pytest.mark.parametrize("queue", queues)
    @pytest.mark.parametrize("tier", ["IRON", "SILVER", "DIAMOND"])
    @pytest.mark.parametrize("division", ["I", "IV"])
    @pytest.mark.parametrize("page", [2, 420])
    def test_entries(self, lol_context, region, queue, tier, division, page):
        actual_response = lol_context.watcher.league.entries(
            region, queue, tier, division, page=page
        )

        lol_context.verify_api_call(
            region,
            f"/lol/league/v4/entries/{queue}/{tier}/{division}",
            {"page": page},
            actual_response,
        )
