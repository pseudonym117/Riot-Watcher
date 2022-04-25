import pytest


@pytest.mark.lol
@pytest.mark.integration
@pytest.mark.parametrize(
    "region", ["EUROPE", "AMERICAS", "ASIA",],
)
class TestMatchApiV5:
    @pytest.mark.parametrize(
        "match_id", ["EUW1_12345", "EUW1_54321", "EUW1_1", "EUW_1222222222222222222222"]
    )
    def test_by_id(self, lol_context, region, match_id):
        actual_response = lol_context.watcher.match.by_id(region, match_id)

        lol_context.verify_api_call(
            region, f"/lol/match/v5/matches/{match_id}", {}, actual_response,
        )

    @pytest.mark.parametrize("puuid", ["12345", "3333333333333333333"])
    @pytest.mark.parametrize("count", [None, 20])
    @pytest.mark.parametrize("start", [None, 0])
    @pytest.mark.parametrize("queue", [None, 0, 420, 2020])
    @pytest.mark.parametrize("type", [None, "ranked", "normal", "tourney", "tutorial"])
    @pytest.mark.parametrize("start_time", [None, 1000])
    @pytest.mark.parametrize("end_time", [None, 2000])
    def test_matchlist_by_puuid(
        self,
        lol_context,
        region,
        puuid,
        start,
        count,
        queue,
        type,
        start_time,
        end_time,
    ):
        actual_response = lol_context.watcher.match.matchlist_by_puuid(
            region,
            puuid,
            start=start,
            count=count,
            queue=queue,
            type=type,
            start_time=start_time,
            end_time=end_time,
        )

        expected_params = {}
        if count is not None:
            expected_params["count"] = count
        if start is not None:
            expected_params["start"] = start
        if queue is not None:
            expected_params["queue"] = queue
        if type is not None:
            expected_params["type"] = type
        if start_time is not None:
            expected_params["startTime"] = start_time
        if end_time is not None:
            expected_params["endTime"] = end_time

        lol_context.verify_api_call(
            region,
            f"/lol/match/v5/matches/by-puuid/{puuid}/ids",
            expected_params,
            actual_response,
        )

    @pytest.mark.parametrize(
        "match_id", ["EUW1_12345", "EUW1_54321", "EUW1_1", "EUW_1222222222222222222222"]
    )
    def test_timeline_by_match(self, lol_context, region, match_id):
        actual_response = lol_context.watcher.match.timeline_by_match(region, match_id)

        lol_context.verify_api_call(
            region, f"/lol/match/v5/matches/{match_id}/timeline", {}, actual_response,
        )


@pytest.mark.lol
@pytest.mark.integration
class TestMatchV5Remapping:
    def test_by_id(self, lol_context, region_remap):
        match_id = "EUW_1234"
        actual_response = lol_context.watcher.match.by_id(
            region_remap.original, match_id
        )

        lol_context.verify_api_call(
            region_remap.to, f"/lol/match/v5/matches/{match_id}", {}, actual_response,
        )

    def test_matchlist_by_puuid(
        self, lol_context, region_remap,
    ):
        puuid = "12345"
        actual_response = lol_context.watcher.match.matchlist_by_puuid(
            region_remap.original, puuid,
        )

        lol_context.verify_api_call(
            region_remap.to,
            f"/lol/match/v5/matches/by-puuid/{puuid}/ids",
            {},
            actual_response,
        )

    def test_timeline_by_match(self, lol_context, region_remap):
        match_id = "EUW1_12345"
        actual_response = lol_context.watcher.match.timeline_by_match(
            region_remap.original, match_id
        )

        lol_context.verify_api_call(
            region_remap.to,
            f"/lol/match/v5/matches/{match_id}/timeline",
            {},
            actual_response,
        )
