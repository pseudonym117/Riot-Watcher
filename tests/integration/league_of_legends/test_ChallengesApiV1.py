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
class TestChallengesApiV1(object):
    def test_config(self, lol_context, region):
        actual_response = lol_context.watcher.challenges.config(region)

        lol_context.verify_api_call(
            region,
            f"/lol/challenges/v1/challenges/config",
            {},
            actual_response
        )

    def test_percentiles(self, lol_context, region):
        actual_response = lol_context.watcher.challenges.percentiles(region)

        lol_context.verify_api_call(
            region,
            f"/lol/challenges/v1/challenges/percentiles",
            {},
            actual_response
        )

    @pytest.mark.parametrize("challenge_id", ["50", "101101"])
    def test_challenge_config(self, lol_context, region, challenge_id):
        actual_response = lol_context.watcher.challenges.challenge_config(region, challenge_id)

        lol_context.verify_api_call(
            region,
            f"/lol/challenges/v1/challenges/{challenge_id}/config",
            {},
            actual_response
        )

    @pytest.mark.parametrize("challenge_id", ["50", "101101"])
    @pytest.mark.parametrize("level", ["oq39as", "GRANDMASTER"])
    def test_leaderboards(self, lol_context, region, challenge_id, level):
        actual_response = lol_context.watcher.challenges.leaderboards(region, challenge_id, level)

        lol_context.verify_api_call(
            region,
            f"/lol/challenges/v1/challenges/{challenge_id}/leaderboards/by-level/{level}",
            {},
            actual_response
        )

    @pytest.mark.parametrize("challenge_id", ["50", "101101"])
    def test_percentiles_by_challenge_id(self, lol_context, region, challenge_id):
        actual_response = lol_context.watcher.challenges.percentiles_by_challenge_id(region, challenge_id)

        lol_context.verify_api_call(
            region,
            f"/lol/challenges/v1/challenges/{challenge_id}/percentiles",
            {},
            actual_response
        )

    @pytest.mark.parametrize("puuid", ["dQw4w9WgXcQ", "12093qowie"])
    def test_by_puuid(self, lol_context, region, puuid):
        actual_response = lol_context.watcher.challenges.by_puuid(region, puuid)

        lol_context.verify_api_call(
            region,
            f"/lol/challenges/v1/player-data/{puuid}",
            {},
            actual_response
        )
