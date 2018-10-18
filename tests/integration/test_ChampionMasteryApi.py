
import sys

import pytest

if sys.version_info > (3, 0):
    import unittest.mock as mock
else:
    import mock

class ChampionMasteryApiContext(object):
    def __init__(self, mock_context):
        self._mock_context = mock_context
        self._expected_response = {'has_value': 'yes', }

        mock_response = mock.MagicMock()
        mock_response.json.return_value = self._expected_response

        mock_context.get.return_value = mock_response

    @property
    def expected_response(self):
        return self._expected_response

    def __getattr__(self, item):
        return getattr(self._mock_context, item)

@pytest.fixture
def mastery_api_ctx(mock_context):
    return ChampionMasteryApiContext(mock_context)

@pytest.mark.integration
@pytest.mark.parametrize('region', ['br1', 'eun1', 'euw1', 'jp1', 'kr', 'la1', 'la2', 'na', 'na1', 'oc1', 'tr1', 'ru', 'pbe1', ])
@pytest.mark.parametrize('summoner_id', [1, 50, 424299938281, 9999999999999999999999, 'rtbf12345', ])
class TestChampionMasteryApi(object):
    def test_by_summoner(self, mastery_api_ctx, region, summoner_id):
        actual_response = mastery_api_ctx.watcher.champion_mastery.by_summoner(
            region,
            summoner_id,
        )

        assert mastery_api_ctx.expected_response == actual_response
        mastery_api_ctx.get.assert_called_once_with(
            'https://{region}.api.riotgames.com/lol/champion-mastery/v3/champion-masteries/by-summoner/{summoner_id}'.format(
                region=region,
                summoner_id=summoner_id,
            ),
            params={},
            headers={'X-Riot-Token': mastery_api_ctx.api_key},
        )
    
    @pytest.mark.parametrize('champion_id', [0, 1, 9999999999, 150])
    def test_by_summoner_by_champion(self, mastery_api_ctx, region, summoner_id, champion_id):
        actual_response = mastery_api_ctx.watcher.champion_mastery.by_summoner_by_champion(
            region,
            summoner_id,
            champion_id,
        )

        assert mastery_api_ctx.expected_response == actual_response
        mastery_api_ctx.get.assert_called_once_with(
            'https://{region}.api.riotgames.com/lol/champion-mastery/v3/champion-masteries/by-summoner/{summoner_id}/by-champion/{champion_id}'.format(
                region=region,
                summoner_id=summoner_id,
                champion_id=champion_id,
            ),
            params={},
            headers={'X-Riot-Token': mastery_api_ctx.api_key},
        )
    
    def test_scores_by_summoner(self, mastery_api_ctx, region, summoner_id):
        actual_response = mastery_api_ctx.watcher.champion_mastery.scores_by_summoner(
            region,
            summoner_id,
        )

        assert mastery_api_ctx.expected_response == actual_response
        mastery_api_ctx.get.assert_called_once_with(
            'https://{region}.api.riotgames.com/lol/champion-mastery/v3/scores/by-summoner/{summoner_id}'.format(
                region=region,
                summoner_id=summoner_id,
            ),
            params={},
            headers={'X-Riot-Token': mastery_api_ctx.api_key},
        )
