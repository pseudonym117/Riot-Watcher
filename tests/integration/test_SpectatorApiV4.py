import sys

import pytest

if sys.version_info > (3, 0):
    import unittest.mock as mock
else:
    import mock


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
class TestSpectatorApiV4(object):
    @pytest.mark.parametrize("encrypted_summoner_id", ["12345", "99999999999999999"])
    def test_by_summoner(self, mock_context_v4, region, encrypted_summoner_id):
        actual_response = mock_context_v4.watcher.spectator.by_summoner(
            region, encrypted_summoner_id
        )

        assert mock_context_v4.expected_response == actual_response
        mock_context_v4.get.assert_called_once_with(
            "https://{region}.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/{encrypted_summoner_id}".format(
                region=region, encrypted_summoner_id=encrypted_summoner_id
            ),
            params={},
            headers={"X-Riot-Token": mock_context_v4.api_key},
        )

    def test_featured_games(self, mock_context_v4, region):
        actual_response = mock_context_v4.watcher.spectator.featured_games(region)

        assert mock_context_v4.expected_response == actual_response
        mock_context_v4.get.assert_called_once_with(
            "https://{region}.api.riotgames.com/lol/spectator/v4/featured-games".format(
                region=region
            ),
            params={},
            headers={"X-Riot-Token": mock_context_v4.api_key},
        )
