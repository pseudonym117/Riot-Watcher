from unittest.mock import MagicMock

import pytest

from riotwatcher._apis.team_fight_tactics import LeagueApi


@pytest.mark.tft
@pytest.mark.unit
class TestLeagueApi:
    def test_challenger(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        league = LeagueApi(mock_base_api)
        region = "afas"

        ret = league.challenger(region)

        mock_base_api.raw_request.assert_called_once_with(
            LeagueApi.__name__,
            league.challenger.__name__,
            region,
            f"https://{region}.api.riotgames.com/tft/league/v1/challenger",
            {},
        )

        assert ret is expected_return

    def test_by_summoner(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        league = LeagueApi(mock_base_api)
        region = "afas"
        encrypted_summoner_id = "15462"

        ret = league.by_summoner(region, encrypted_summoner_id)

        mock_base_api.raw_request.assert_called_once_with(
            LeagueApi.__name__,
            league.by_summoner.__name__,
            region,
            f"https://{region}.api.riotgames.com/tft/league/v1/entries/by-summoner/{encrypted_summoner_id}",
            {},
        )

        assert ret is expected_return

    def test_entries(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        league = LeagueApi(mock_base_api)
        region, tier, division = "afas", "WOOD", "V"

        ret = league.entries(region, tier, division)

        mock_base_api.raw_request.assert_called_once_with(
            LeagueApi.__name__,
            league.entries.__name__,
            region,
            f"https://{region}.api.riotgames.com/tft/league/v1/entries/{tier}/{division}",
            {"page": 1},
        )

        assert ret is expected_return

    def test_grandmaster(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        league = LeagueApi(mock_base_api)
        region = "afas"

        ret = league.grandmaster(region)

        mock_base_api.raw_request.assert_called_once_with(
            LeagueApi.__name__,
            league.grandmaster.__name__,
            region,
            f"https://{region}.api.riotgames.com/tft/league/v1/grandmaster",
            {},
        )

        assert ret is expected_return

    def test_by_id(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        league = LeagueApi(mock_base_api)
        region = "afas"
        league_id = "hdhddfd"

        ret = league.by_id(region, league_id)

        mock_base_api.raw_request.assert_called_once_with(
            LeagueApi.__name__,
            league.by_id.__name__,
            region,
            f"https://{region}.api.riotgames.com/tft/league/v1/leagues/{league_id}",
            {},
        )

        assert ret is expected_return

    def test_master(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        league = LeagueApi(mock_base_api)
        region = "afas"

        ret = league.master(region)

        mock_base_api.raw_request.assert_called_once_with(
            LeagueApi.__name__,
            league.master.__name__,
            region,
            f"https://{region}.api.riotgames.com/tft/league/v1/master",
            {},
        )

        assert ret is expected_return

    def test_rated_ladders(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        league = LeagueApi(mock_base_api)
        region = "afas"
        queue = "hdhddfd"

        ret = league.rated_ladders(region, queue)

        mock_base_api.raw_request.assert_called_once_with(
            LeagueApi.__name__,
            league.rated_ladders.__name__,
            region,
            f"https://{region}.api.riotgames.com/tft/league/v1/rated-ladders/{queue}/top",
            {},
        )

        assert ret is expected_return
