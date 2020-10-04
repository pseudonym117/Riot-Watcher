import pytest


@pytest.fixture(params=["12345", "99999999999999"])
def match_id(request):
    return request.param


@pytest.fixture(params=["competitive", "unrated", "spikerush"])
def queue(request):
    return request.param


@pytest.mark.val
@pytest.mark.integration
class TestMatchApi:
    def test_by_id(self, val_context, region, match_id):
        actual_response = val_context.watcher.match.by_id(region, match_id)

        val_context.verify_api_call(
            region, f"/val/match/v1/matches/{match_id}", {}, actual_response
        )

    def test_matchlist_by_puuid(self, val_context, region, puuid):
        actual_response = val_context.watcher.match.matchlist_by_puuid(region, puuid)

        val_context.verify_api_call(
            region, f"/val/match/v1/matchlists/by-puuid/{puuid}", {}, actual_response
        )

    def test_recent_matches(self, val_context, region, queue):
        actual_response = val_context.watcher.match.recent_matches(region, queue)

        val_context.verify_api_call(
            region,
            f"/val/match/v1/recent-matches/by-queue/{queue}",
            {},
            actual_response,
        )
