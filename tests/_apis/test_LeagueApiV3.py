import sys

import pytest

if sys.version_info > (3, 0):
    from unittest.mock import MagicMock
else:
    from mock import MagicMock

from riotwatcher._apis import LeagueApiV3


@pytest.mark.unit
class TestLeagueApiV3(object):
    def test_challenger_by_queue(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        league = LeagueApiV3(mock_base_api)
        region = "afas"
        queue = "yolo_q"

        ret = league.challenger_by_queue(region, queue)

        mock_base_api.raw_request.assert_called_once_with(
            LeagueApiV3.__name__,
            league.challenger_by_queue.__name__,
            region,
            "https://afas.api.riotgames.com/lol/league/v3/challengerleagues/by-queue/{queue}".format(
                queue=queue
            ),
            {},
        )

        assert ret is expected_return

    def test_masters_by_queue(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        league = LeagueApiV3(mock_base_api)
        region = "afasf"
        queue = "yolo_q"

        ret = league.masters_by_queue(region, queue)

        mock_base_api.raw_request.assert_called_once_with(
            LeagueApiV3.__name__,
            league.masters_by_queue.__name__,
            region,
            "https://afasf.api.riotgames.com/lol/league/v3/masterleagues/by-queue/{queue}".format(
                queue=queue
            ),
            {},
        )

        assert ret is expected_return

    def test_by_id(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        league = LeagueApiV3(mock_base_api)
        region = "afasf"
        league_id = "aaa-bbb-ccc"

        ret = league.by_id(region, league_id)

        mock_base_api.raw_request.assert_called_once_with(
            LeagueApiV3.__name__,
            league.by_id.__name__,
            region,
            "https://afasf.api.riotgames.com/lol/league/v3/leagues/{league_id}".format(
                league_id=league_id
            ),
            {},
        )

        assert ret is expected_return

    def test_positions_by_summoner(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        league = LeagueApiV3(mock_base_api)
        region = "afasf"
        summoner_id = 52343

        ret = league.positions_by_summoner(region, summoner_id)

        mock_base_api.raw_request.assert_called_once_with(
            LeagueApiV3.__name__,
            league.positions_by_summoner.__name__,
            region,
            "https://afasf.api.riotgames.com/lol/league/v3/positions/by-summoner/{summonerId}".format(
                summonerId=summoner_id
            ),
            {},
        )

        assert ret is expected_return
