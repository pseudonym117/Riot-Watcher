import pytest


@pytest.mark.lor
@pytest.mark.integration
class TestRankedApi:
    def test_leaderboards(self, lor_context, region):
        actual_response = lor_context.watcher.ranked.leaderboards(region)

        lor_context.verify_api_call(
            region, "/lor/ranked/v1/leaderboards", {}, actual_response,
        )
