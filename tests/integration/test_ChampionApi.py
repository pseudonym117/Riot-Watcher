
import json
import random
import sys

import pytest

if sys.version_info > (3, 0):
    import unittest.mock as mock
else:
    import mock


class ChampionApiContext(object):
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
def champion_api_ctx(mock_context):
    return ChampionApiContext(mock_context)


@pytest.mark.integration
@pytest.mark.parametrize('region', ['br1', 'eun1', 'euw1', 'jp1', 'kr', 'la1', 'la2', 'na', 'na1', 'oc1', 'tr1', 'ru', 'pbe1', ])
class TestChampionApi(object):
    @pytest.mark.parametrize('free_to_play', (True, False, ))
    def test_all(self, champion_api_ctx, region, free_to_play):
        actual_response = champion_api_ctx.watcher.champion.all(region, free_to_play=free_to_play)

        assert champion_api_ctx.expected_response == actual_response
        champion_api_ctx.get.assert_called_once_with(
            'https://{region}.api.riotgames.com/lol/platform/v3/champions'.format(region=region),
            params={'freeToPlay': 'true' if free_to_play else 'false'},
            headers={'X-Riot-Token': champion_api_ctx.api_key},
        )

    @pytest.mark.parametrize('champion_id', range(50))
    def test_by_id(self, champion_api_ctx, region, champion_id):
        actual_response = champion_api_ctx.watcher.champion.by_id(region, champion_id)

        assert champion_api_ctx.expected_response == actual_response
        champion_api_ctx.get.assert_called_once_with(
            'https://{region}.api.riotgames.com/lol/platform/v3/champions/{id}'.format(
                region=region,
                id=champion_id,
            ),
            params={},
            headers={'X-Riot-Token': champion_api_ctx.api_key},
        )
    
    def test_rotations(self, champion_api_ctx, region):
        actual_response = champion_api_ctx.watcher.champion.rotations(region)

        assert champion_api_ctx.expected_response == actual_response
        champion_api_ctx.get.assert_called_once_with(
            'https://{region}.api.riotgames.com/lol/platform/v3/champion-rotations'.format(
                region=region,
            ),
            params={},
            headers={'X-Riot-Token': champion_api_ctx.api_key},
        )
