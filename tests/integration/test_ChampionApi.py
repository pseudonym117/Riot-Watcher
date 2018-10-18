
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
