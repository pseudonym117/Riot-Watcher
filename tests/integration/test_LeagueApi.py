
import sys

import pytest

if sys.version_info > (3, 0):
    import unittest.mock as mock
else:
    import mock


class LeagueApiContext(object):
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
def league_api_ctx(mock_context):
    return LeagueApiContext(mock_context)

@pytest.mark.integration
@pytest.mark.parametrize('region', ['br1', 'eun1', 'euw1', 'jp1', 'kr', 'la1', 'la2', 'na', 'na1', 'oc1', 'tr1', 'ru', 'pbe1', ])
class TestLeagueApi(object):
    @pytest.mark.parametrize('queue', ['RANKED_SOLO_5x5', 'RANKED_FLEX_SR', 'RANKED_FLEX_TT'])
    def test_challenger_by_queue(self, league_api_ctx, region, queue):
        actual_response = league_api_ctx.watcher.league.challenger_by_queue(
            region,
            queue,
        )

        assert league_api_ctx.expected_response == actual_response
        league_api_ctx.get.assert_called_once_with(
            'https://{region}.api.riotgames.com/lol/league/v3/challengerleagues/by-queue/{queue}'.format(
                region=region,
                queue=queue,
            ),
            params={},
            headers={'X-Riot-Token': league_api_ctx.api_key},
        )
    
    @pytest.mark.parametrize('queue', ['RANKED_SOLO_5x5', 'RANKED_FLEX_SR', 'RANKED_FLEX_TT'])
    def test_masters_by_queue(self, league_api_ctx, region, queue):
        actual_response = league_api_ctx.watcher.league.masters_by_queue(region, queue)

        assert league_api_ctx.expected_response == actual_response
        league_api_ctx.get.assert_called_once_with(
            'https://{region}.api.riotgames.com/lol/league/v3/masterleagues/by-queue/{queue}'.format(
                region=region,
                queue=queue,
            ),
            params={},
            headers={'X-Riot-Token': league_api_ctx.api_key},
        )
    
    @pytest.mark.parametrize('league_id', [1, 500, 99999999999999])
    def test_by_id(self, league_api_ctx, region, league_id):
        actual_response = league_api_ctx.watcher.league.by_id(region, league_id)

        assert league_api_ctx.expected_response == actual_response
        league_api_ctx.get.assert_called_once_with(
            'https://{region}.api.riotgames.com/lol/league/v3/leagues/{league_id}'.format(
                region=region,
                league_id=league_id,
            ),
            params={},
            headers={'X-Riot-Token': league_api_ctx.api_key},
        )
    
    @pytest.mark.parametrize('summoner_id', [1, 50, 424299938281, 9999999999999999999999, 'rtbf12345', ])
    def test_positions_by_summoner(self, league_api_ctx, region, summoner_id):
        actual_response = league_api_ctx.watcher.league.positions_by_summoner(
            region,
            summoner_id,
        )

        assert league_api_ctx.expected_response == actual_response
        league_api_ctx.get.assert_called_once_with(
            'https://{region}.api.riotgames.com/lol/league/v3/positions/by-summoner/{summoner_id}'.format(
                region=region,
                summoner_id=summoner_id,
            ),
            params={},
            headers={'X-Riot-Token': league_api_ctx.api_key},
        )
