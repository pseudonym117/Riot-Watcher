
import sys

import pytest

if sys.version_info > (3, 0):
    import unittest.mock as mock
else:
    import mock


class ThirdPartyCodeApiContext(object):
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
def third_party_code_api_ctx(mock_context):
    return ThirdPartyCodeApiContext(mock_context)


@pytest.mark.integration
@pytest.mark.parametrize('region', ['br1', 'eun1', 'euw1', 'jp1', 'kr', 'la1', 'la2', 'na', 'na1', 'oc1', 'tr1', 'ru', 'pbe1', ])
class TestThirdPartyCodeApi(object):
    @pytest.mark.parametrize('summoner_id', [12345, 99999999999999999, -1, ])
    def test_by_summoner(self, third_party_code_api_ctx, region, summoner_id):
        actual_response = third_party_code_api_ctx.watcher.third_party_code.by_summoner(region, summoner_id)

        assert third_party_code_api_ctx.expected_response == actual_response
        third_party_code_api_ctx.get.assert_called_once_with(
            'https://{region}.api.riotgames.com/lol/platform/v3/third-party-code/by-summoner/{summoner_id}'.format(
                region=region,
                summoner_id=summoner_id,
            ),
            params={},
            headers={'X-Riot-Token': third_party_code_api_ctx.api_key},
        )
