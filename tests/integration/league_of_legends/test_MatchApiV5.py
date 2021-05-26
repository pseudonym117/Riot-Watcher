import pytest


@pytest.mark.lol
@pytest.mark.integration
@pytest.mark.parametrize(
    "region",
    [
        "EUROPE",
        "AMERICAS",
        "ASIA",       
    ],
)
class TestMatchApiV5:
    @pytest.mark.parametrize("match_id", ["EUW1_12345", "EUW1_54321", "EUW1_1", "EUW_1222222222222222222222"])
    def test_by_id(self, lol_context, region, match_id):
        actual_response = lol_context.watcher.matchv5.by_id(region, match_id)

        lol_context.verify_api_call(
            region, f"/lol/match/v5/matches/{match_id}", {}, actual_response,
        )

    @pytest.mark.parametrize("puuid", ["12345", "3333333333333333333"])
    @pytest.mark.parametrize("count", [None, 20])
    @pytest.mark.parametrize("start", [None, 0])    
    def test_matchlist_by_account(
        self,
        lol_context,
        region,
        puuid,
        start,
        count,       
    ):        

        actual_response = lol_context.watcher.matchv5.matchlist_by_puuid(
            region,
            puuid,
            start=start,
            count=count,            
        )

        expected_params = {}
        if count is not None:
            expected_params["count"] = count
        if start is not None:
            expected_params["start"] = start        

        lol_context.verify_api_call(
            region,
            f"/lol/match/v5/matches/by-puuid/{puuid}/ids",
            expected_params,
            actual_response,
        )

    @pytest.mark.parametrize("match_id", ["EUW1_12345", "EUW1_54321", "EUW1_1", "EUW_1222222222222222222222"])
    def test_timeline_by_match(self, lol_context, region, match_id):
        actual_response = lol_context.watcher.matchv5.timeline_by_match(region, match_id)

        lol_context.verify_api_call(
            region, f"/lol/match/v5/matches/{match_id}/timeline", {}, actual_response,
        )
