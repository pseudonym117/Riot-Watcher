from unittest.mock import MagicMock

import pytest

from riotwatcher._apis.league_of_legends import LeagueApiV4


@pytest.mark.lol
@pytest.mark.unit
class TestLeagueApiV4:
    def test_challenger_by_queue(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        league = LeagueApiV4(mock_base_api)
        region = "afas"
        queue = "yolo_q"

        ret = league.challenger_by_queue(region, queue)

        mock_base_api.raw_request.assert_called_once_with(
            LeagueApiV4.__name__,
            league.challenger_by_queue.__name__,
            region,
            f"https://{region}.api.riotgames.com/lol/league/v4/challengerleagues/by-queue/{queue}",
            {},
        )

        assert ret is expected_return

    def test_grandmaster_by_queue(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        league = LeagueApiV4(mock_base_api)
        region = "afasf"
        queue = "yolo_q"

        ret = league.grandmaster_by_queue(region, queue)

        mock_base_api.raw_request.assert_called_once_with(
            LeagueApiV4.__name__,
            league.grandmaster_by_queue.__name__,
            region,
            f"https://{region}.api.riotgames.com/lol/league/v4/grandmasterleagues/by-queue/{queue}",
            {},
        )

        assert ret is expected_return

    def test_masters_by_queue(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        league = LeagueApiV4(mock_base_api)
        region = "afasf"
        queue = "yolo_q"

        ret = league.masters_by_queue(region, queue)

        mock_base_api.raw_request.assert_called_once_with(
            LeagueApiV4.__name__,
            league.masters_by_queue.__name__,
            region,
            f"https://{region}.api.riotgames.com/lol/league/v4/masterleagues/by-queue/{queue}",
            {},
        )

        assert ret is expected_return

    def test_by_id(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        league = LeagueApiV4(mock_base_api)
        region = "afasf"
        league_id = "aaa-bbb-ccc"

        ret = league.by_id(region, league_id)

        mock_base_api.raw_request.assert_called_once_with(
            LeagueApiV4.__name__,
            league.by_id.__name__,
            region,
            f"https://{region}.api.riotgames.com/lol/league/v4/leagues/{league_id}",
            {},
        )

        assert ret is expected_return

    def test_by_summoner(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        league = LeagueApiV4(mock_base_api)
        region = "fdsga"
        encrypted_summoner_id = "enc_summoner_1"

        ret = league.by_summoner(region, encrypted_summoner_id)

        mock_base_api.raw_request.assert_called_once_with(
            LeagueApiV4.__name__,
            league.by_summoner.__name__,
            region,
            f"https://{region}.api.riotgames.com/lol/league/v4/entries/by-summoner/{encrypted_summoner_id}",
            {},
        )

        assert ret is expected_return

    def test_entries(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        league = LeagueApiV4(mock_base_api)
        region = "hfhafg"
        queue = "yolo_q"
        tier = "wood"
        division = "VI"
        page = 420

        ret = league.entries(region, queue, tier, division, page=page)

        mock_base_api.raw_request.assert_called_once_with(
            LeagueApiV4.__name__,
            league.entries.__name__,
            region,
            f"https://{region}.api.riotgames.com/lol/league/v4/entries/{queue}/{tier}/{division}",
            {"page": page},
        )

        assert ret is expected_return

    def test_entries_defaults(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        league = LeagueApiV4(mock_base_api)
        region = "fsgqqq"
        queue = "yolo_q"
        tier = "wood"
        division = "III"

        ret = league.entries(region, queue, tier, division)

        mock_base_api.raw_request.assert_called_once_with(
            LeagueApiV4.__name__,
            league.entries.__name__,
            region,
            f"https://{region}.api.riotgames.com/lol/league/v4/entries/{queue}/{tier}/{division}",
            {"page": 1},
        )

        assert ret is expected_return
