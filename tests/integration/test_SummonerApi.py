
import sys

import pytest

if sys.version_info > (3, 0):
    import unittest.mock as mock
else:
    import mock


class SummonerApiContext(object):
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
def summoner_api_ctx(mock_context):
    return SummonerApiContext(mock_context)


@pytest.mark.integration
@pytest.mark.parametrize('region', ['br1', 'eun1', 'euw1', 'jp1', 'kr', 'la1', 'la2', 'na', 'na1', 'oc1', 'tr1', 'ru', 'pbe1', ])
class TestSummonerApi(object):
    @pytest.mark.parametrize('account_id', [12345, 99999999999999999999, ])
    def test_by_account(self, summoner_api_ctx, region, account_id):
        actual_response = summoner_api_ctx.watcher.summoner.by_account(region, account_id)

        assert summoner_api_ctx.expected_response == actual_response
        summoner_api_ctx.get.assert_called_once_with(
            'https://{region}.api.riotgames.com/lol/summoner/v3/summoners/by-account/{account_id}'.format(
                region=region,
                account_id=account_id,
            ),
            params={},
            headers={'X-Riot-Token': summoner_api_ctx.api_key},
        )

    @pytest.mark.parametrize('summoner_name', ['pseudonym117', 'Riot Tuxedo', ])
    def test_by_name(self, summoner_api_ctx, region, summoner_name):
        actual_response = summoner_api_ctx.watcher.summoner.by_name(region, summoner_name)

        assert summoner_api_ctx.expected_response == actual_response
        summoner_api_ctx.get.assert_called_once_with(
            'https://{region}.api.riotgames.com/lol/summoner/v3/summoners/by-name/{summoner_name}'.format(
                region=region,
                summoner_name=summoner_name,
            ),
            params={},
            headers={'X-Riot-Token': summoner_api_ctx.api_key},
        )
    
    @pytest.mark.parametrize('summoner_id', [12345, 99999999999999999999, ])
    def test_by_id(self, summoner_api_ctx, region, summoner_id):
        actual_response = summoner_api_ctx.watcher.summoner.by_id(region, summoner_id)

        assert summoner_api_ctx.expected_response == actual_response
        summoner_api_ctx.get.assert_called_once_with(
            'https://{region}.api.riotgames.com/lol/summoner/v3/summoners/{summoner_id}'.format(
                region=region,
                summoner_id=summoner_id,
            ),
            params={},
            headers={'X-Riot-Token': summoner_api_ctx.api_key},
        )
