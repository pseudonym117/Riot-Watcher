
import sys

import pytest

if sys.version_info > (3, 0):
    import unittest.mock as mock
else:
    import mock


@pytest.mark.integration
@pytest.mark.parametrize('region', ['br1', 'eun1', 'euw1', 'jp1', 'kr', 'la1', 'la2', 'na', 'na1', 'oc1', 'tr1', 'ru', 'pbe1', ])
class TestSpectatorApi(object):
    @pytest.mark.parametrize('summoner_id', [12345, 99999999999999999, -1, ])
    def test_by_summoner(self, mock_context, region, summoner_id):
        actual_response = mock_context.watcher.spectator.by_summoner(region, summoner_id)

        assert mock_context.expected_response == actual_response
        mock_context.get.assert_called_once_with(
            'https://{region}.api.riotgames.com/lol/spectator/v3/active-games/by-summoner/{summoner_id}'.format(
                region=region,
                summoner_id=summoner_id,
            ),
            params={},
            headers={'X-Riot-Token': mock_context.api_key},
        )
    
    def test_featured_games(self, mock_context, region):
        actual_response = mock_context.watcher.spectator.featured_games(region)

        assert mock_context.expected_response == actual_response
        mock_context.get.assert_called_once_with(
            'https://{region}.api.riotgames.com/lol/spectator/v3/featured-games'.format(
                region=region,
            ),
            params={},
            headers={'X-Riot-Token': mock_context.api_key},
        )
