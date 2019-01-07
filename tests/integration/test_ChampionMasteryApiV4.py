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
@pytest.mark.parametrize("encrypted_summoner_id", ["50", "424299938281", "rtbf12345"])
class TestChampionMasteryApiV4(object):
    def test_by_summoner(self, mock_context_v4, region, encrypted_summoner_id):
        actual_response = mock_context_v4.watcher.champion_mastery.by_summoner(
            region, encrypted_summoner_id
        )

        assert mock_context_v4.expected_response == actual_response
        mock_context_v4.get.assert_called_once_with(
            "https://{region}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{encrypted_summoner_id}".format(
                region=region, encrypted_summoner_id=encrypted_summoner_id
            ),
            params={},
            headers={"X-Riot-Token": mock_context_v4.api_key},
        )

    @pytest.mark.parametrize("champion_id", [0, 1, 9999999999, 150])
    def test_by_summoner_by_champion(
        self, mock_context_v4, region, encrypted_summoner_id, champion_id
    ):
        actual_response = mock_context_v4.watcher.champion_mastery.by_summoner_by_champion(
            region, encrypted_summoner_id, champion_id
        )

        assert mock_context_v4.expected_response == actual_response
        mock_context_v4.get.assert_called_once_with(
            "https://{region}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{encrypted_summoner_id}/by-champion/{champion_id}".format(
                region=region,
                encrypted_summoner_id=encrypted_summoner_id,
                champion_id=champion_id,
            ),
            params={},
            headers={"X-Riot-Token": mock_context_v4.api_key},
        )

    def test_scores_by_summoner(self, mock_context_v4, region, encrypted_summoner_id):
        actual_response = mock_context_v4.watcher.champion_mastery.scores_by_summoner(
            region, encrypted_summoner_id
        )

        assert mock_context_v4.expected_response == actual_response
        mock_context_v4.get.assert_called_once_with(
            "https://{region}.api.riotgames.com/lol/champion-mastery/v4/scores/by-summoner/{encrypted_summoner_id}".format(
                region=region, encrypted_summoner_id=encrypted_summoner_id
            ),
            params={},
            headers={"X-Riot-Token": mock_context_v4.api_key},
        )
