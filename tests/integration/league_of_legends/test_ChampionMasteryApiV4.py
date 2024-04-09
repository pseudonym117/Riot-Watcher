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
@pytest.mark.parametrize("puuid", ["50", "rtbf12345"])
class TestChampionMasteryApiV4(object):
    def test_by_puuid(self, lol_context, region, puuid):
        actual_response = lol_context.watcher.champion_mastery.by_puuid(region, puuid)

        lol_context.verify_api_call(
            region,
            f"/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}",
            {},
            actual_response,
        )

    @pytest.mark.parametrize("champion_id", [0, 1, 9999999999, 150])
    def test_by_puuid_by_champion(self, lol_context, region, puuid, champion_id):
        actual_response = lol_context.watcher.champion_mastery.by_puuid_by_champion(
            region, puuid, champion_id
        )

        lol_context.verify_api_call(
            region,
            f"/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}/by-champion/{champion_id}",
            {},
            actual_response,
        )

    @pytest.mark.parametrize("count", [None, 1, 20])
    def test_top_by_puuid(self, lol_context, region, puuid, count):
        params = {}
        if count is not None:
            params["count"] = count

        actual_response = lol_context.watcher.champion_mastery.top_by_puuid(
            region, puuid, **params
        )

        lol_context.verify_api_call(
            region,
            f"/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}/top",
            params,
            actual_response,
        )

    def test_scores_by_puuid(self, lol_context, region, puuid):
        actual_response = lol_context.watcher.champion_mastery.scores_by_puuid(
            region, puuid
        )

        lol_context.verify_api_call(
            region,
            f"/lol/champion-mastery/v4/scores/by-puuid/{puuid}",
            {},
            actual_response,
        )
