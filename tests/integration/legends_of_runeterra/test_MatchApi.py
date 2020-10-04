import pytest


@pytest.fixture(params=["533c8122-f17b-44c1-9254-81a9288a9a6b"])
def match_id(request):
    return request.param


@pytest.mark.lor
@pytest.mark.integration
class TestRankedApi:
    def test_by_puuid(self, lor_context, region, puuid):
        actual_response = lor_context.watcher.match.by_puuid(region, puuid)

        lor_context.verify_api_call(
            region, f"/lor/match/v1/matches/by-puuid/{puuid}/ids", {}, actual_response,
        )

    def test_by_id(self, lor_context, region, match_id):
        actual_response = lor_context.watcher.match.by_id(region, match_id)

        lor_context.verify_api_call(
            region, f"/lor/match/v1/matches/{match_id}", {}, actual_response,
        )
