import pytest


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
class TestStatusApiV3:
    def test_shard_data(self, mock_context, region):
        actual_response = mock_context.watcher.lol_status.shard_data(region)

        mock_context.verify_api_call(
            region, "/lol/status/v3/shard-data", {}, actual_response
        )
