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
class TestLeagueApi(object):
    @pytest.mark.parametrize(
        "queue", ["RANKED_SOLO_5x5", "RANKED_FLEX_SR", "RANKED_FLEX_TT"]
    )
    def test_challenger_by_queue(self, mock_context, region, queue):
        actual_response = mock_context.watcher.league.challenger_by_queue(region, queue)

        assert mock_context.expected_response == actual_response
        mock_context.get.assert_called_once_with(
            "https://{region}.api.riotgames.com/lol/league/v3/challengerleagues/by-queue/{queue}".format(
                region=region, queue=queue
            ),
            params={},
            headers={"X-Riot-Token": mock_context.api_key},
        )

    @pytest.mark.parametrize(
        "queue", ["RANKED_SOLO_5x5", "RANKED_FLEX_SR", "RANKED_FLEX_TT"]
    )
    def test_masters_by_queue(self, mock_context, region, queue):
        actual_response = mock_context.watcher.league.masters_by_queue(region, queue)

        assert mock_context.expected_response == actual_response
        mock_context.get.assert_called_once_with(
            "https://{region}.api.riotgames.com/lol/league/v3/masterleagues/by-queue/{queue}".format(
                region=region, queue=queue
            ),
            params={},
            headers={"X-Riot-Token": mock_context.api_key},
        )

    @pytest.mark.parametrize("league_id", [1, 500, 99999999999999])
    def test_by_id(self, mock_context, region, league_id):
        actual_response = mock_context.watcher.league.by_id(region, league_id)

        assert mock_context.expected_response == actual_response
        mock_context.get.assert_called_once_with(
            "https://{region}.api.riotgames.com/lol/league/v3/leagues/{league_id}".format(
                region=region, league_id=league_id
            ),
            params={},
            headers={"X-Riot-Token": mock_context.api_key},
        )

    @pytest.mark.parametrize(
        "summoner_id", [1, 50, 424299938281, 9999999999999999999999, "rtbf12345"]
    )
    def test_positions_by_summoner(self, mock_context, region, summoner_id):
        actual_response = mock_context.watcher.league.positions_by_summoner(
            region, summoner_id
        )

        assert mock_context.expected_response == actual_response
        mock_context.get.assert_called_once_with(
            "https://{region}.api.riotgames.com/lol/league/v3/positions/by-summoner/{summoner_id}".format(
                region=region, summoner_id=summoner_id
            ),
            params={},
            headers={"X-Riot-Token": mock_context.api_key},
        )
