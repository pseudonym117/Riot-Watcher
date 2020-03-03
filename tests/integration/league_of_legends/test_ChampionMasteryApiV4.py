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
@pytest.mark.parametrize("encrypted_summoner_id", ["50", "424299938281", "rtbf12345"])
class TestChampionMasteryApiV4(object):
    def test_by_summoner(self, lol_context, region, encrypted_summoner_id):
        actual_response = lol_context.watcher.champion_mastery.by_summoner(
            region, encrypted_summoner_id
        )

        lol_context.verify_api_call(
            region,
            f"/lol/champion-mastery/v4/champion-masteries/by-summoner/{encrypted_summoner_id}",
            {},
            actual_response,
        )

    @pytest.mark.parametrize("champion_id", [0, 1, 9999999999, 150])
    def test_by_summoner_by_champion(
        self, lol_context, region, encrypted_summoner_id, champion_id
    ):
        actual_response = lol_context.watcher.champion_mastery.by_summoner_by_champion(
            region, encrypted_summoner_id, champion_id
        )

        lol_context.verify_api_call(
            region,
            f"/lol/champion-mastery/v4/champion-masteries/by-summoner/{encrypted_summoner_id}/by-champion/{champion_id}",
            {},
            actual_response,
        )

    def test_scores_by_summoner(self, lol_context, region, encrypted_summoner_id):
        actual_response = lol_context.watcher.champion_mastery.scores_by_summoner(
            region, encrypted_summoner_id
        )

        lol_context.verify_api_call(
            region,
            f"/lol/champion-mastery/v4/scores/by-summoner/{encrypted_summoner_id}",
            {},
            actual_response,
        )
