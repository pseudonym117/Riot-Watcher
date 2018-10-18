
import sys

import pytest

if sys.version_info > (3, 0):
    import unittest.mock as mock
else:
    import mock


class StatusApiContext(object):
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
def status_api_ctx(mock_context):
    return StatusApiContext(mock_context)


@pytest.mark.integration
@pytest.mark.parametrize('region', ['br1', 'eun1', 'euw1', 'jp1', 'kr', 'la1', 'la2', 'na', 'na1', 'oc1', 'tr1', 'ru', 'pbe1', ])
class TestStatusApi(object):
    def test_shard_data(self, status_api_ctx, region):
        actual_response = status_api_ctx.watcher.lol_status.shard_data(region)

        assert status_api_ctx.expected_response == actual_response
        status_api_ctx.get.assert_called_once_with(
            'https://{region}.api.riotgames.com/lol/status/v3/shard-data'.format(region=region),
            params={},
            headers={'X-Riot-Token': status_api_ctx.api_key},
        )
