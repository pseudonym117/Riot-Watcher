
import sys

import pytest

if sys.version_info > (3, 0):
    import unittest.mock as mock
else:
    import mock


class SpectatorApiContext(object):
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
def spectator_api_ctx(mock_context):
    return SpectatorApiContext(mock_context)


@pytest.mark.integration
@pytest.mark.parametrize('region', ['br1', 'eun1', 'euw1', 'jp1', 'kr', 'la1', 'la2', 'na', 'na1', 'oc1', 'tr1', 'ru', 'pbe1', ])
class TestSpectatorApi(object):
    @pytest.mark.parametrize('summoner_id', [12345, 99999999999999999, -1, ])
    def test_by_summoner(self, spectator_api_ctx, region, summoner_id):
        actual_response = spectator_api_ctx.watcher.spectator.by_summoner(region, summoner_id)

        assert spectator_api_ctx.expected_response == actual_response
        spectator_api_ctx.get.assert_called_once_with(
            'https://{region}.api.riotgames.com/lol/spectator/v3/active-games/by-summoner/{summoner_id}'.format(
                region=region,
                summoner_id=summoner_id,
            ),
            params={},
            headers={'X-Riot-Token': spectator_api_ctx.api_key},
        )
    
    def test_featured_games(self, spectator_api_ctx, region):
        actual_response = spectator_api_ctx.watcher.spectator.featured_games(region)

        assert spectator_api_ctx.expected_response == actual_response
        spectator_api_ctx.get.assert_called_once_with(
            'https://{region}.api.riotgames.com/lol/spectator/v3/featured-games'.format(
                region=region,
            ),
            params={},
            headers={'X-Riot-Token': spectator_api_ctx.api_key},
        )
