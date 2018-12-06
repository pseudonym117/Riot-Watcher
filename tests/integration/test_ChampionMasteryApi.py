
import sys

import pytest

if sys.version_info > (3, 0):
    import unittest.mock as mock
else:
    import mock


@pytest.mark.integration
@pytest.mark.parametrize('region', ['br1', 'eun1', 'euw1', 'jp1', 'kr', 'la1', 'la2', 'na', 'na1', 'oc1', 'tr1', 'ru', 'pbe1', ])
@pytest.mark.parametrize('summoner_id', [1, 50, 424299938281, 9999999999999999999999, 'rtbf12345', ])
class TestChampionMasteryApi(object):
    def test_by_summoner(self, mock_context, region, summoner_id):
        actual_response = mock_context.watcher.champion_mastery.by_summoner(
            region,
            summoner_id,
        )

        assert mock_context.expected_response == actual_response
        mock_context.get.assert_called_once_with(
            'https://{region}.api.riotgames.com/lol/champion-mastery/v3/champion-masteries/by-summoner/{summoner_id}'.format(
                region=region,
                summoner_id=summoner_id,
            ),
            params={},
            headers={'X-Riot-Token': mock_context.api_key},
        )
    
    @pytest.mark.parametrize('champion_id', [0, 1, 9999999999, 150])
    def test_by_summoner_by_champion(self, mock_context, region, summoner_id, champion_id):
        actual_response = mock_context.watcher.champion_mastery.by_summoner_by_champion(
            region,
            summoner_id,
            champion_id,
        )

        assert mock_context.expected_response == actual_response
        mock_context.get.assert_called_once_with(
            'https://{region}.api.riotgames.com/lol/champion-mastery/v3/champion-masteries/by-summoner/{summoner_id}/by-champion/{champion_id}'.format(
                region=region,
                summoner_id=summoner_id,
                champion_id=champion_id,
            ),
            params={},
            headers={'X-Riot-Token': mock_context.api_key},
        )
    
    def test_scores_by_summoner(self, mock_context, region, summoner_id):
        actual_response = mock_context.watcher.champion_mastery.scores_by_summoner(
            region,
            summoner_id,
        )

        assert mock_context.expected_response == actual_response
        mock_context.get.assert_called_once_with(
            'https://{region}.api.riotgames.com/lol/champion-mastery/v3/scores/by-summoner/{summoner_id}'.format(
                region=region,
                summoner_id=summoner_id,
            ),
            params={},
            headers={'X-Riot-Token': mock_context.api_key},
        )
