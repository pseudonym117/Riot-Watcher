from unittest.mock import MagicMock

import pytest

from riotwatcher._apis.league_of_legends import ClashApiV1


@pytest.mark.lol
@pytest.mark.unit
class TestClashApiV1:
    def test_by_summoner(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        clash = ClashApiV1(mock_base_api)
        region = "htr35ge"
        summoner_id = "98532"

        ret = clash.by_summoner(region, summoner_id)

        mock_base_api.raw_request.assert_called_once_with(
            ClashApiV1.__name__,
            clash.by_summoner.__name__,
            region,
            f"https://{region}.api.riotgames.com/lol/clash/v1/players/by-summoner/{summoner_id}",
            {},
        )

        assert ret is expected_return

    def test_by_team(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        clash = ClashApiV1(mock_base_api)
        region = "htr35ge"
        team_id = "psesn886"

        ret = clash.by_team(region, team_id)

        mock_base_api.raw_request.assert_called_once_with(
            ClashApiV1.__name__,
            clash.by_team.__name__,
            region,
            f"https://{region}.api.riotgames.com/lol/clash/v1/teams/{team_id}",
            {},
        )

        assert ret is expected_return

    def test_tournaments(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        clash = ClashApiV1(mock_base_api)
        region = "htr35ge"

        ret = clash.tournaments(region)

        mock_base_api.raw_request.assert_called_once_with(
            ClashApiV1.__name__,
            clash.tournaments.__name__,
            region,
            f"https://{region}.api.riotgames.com/lol/clash/v1/tournaments",
            {},
        )

        assert ret is expected_return

    def test_tournament_by_team(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        clash = ClashApiV1(mock_base_api)
        region = "htr35ge"
        team_id = "25979"

        ret = clash.tournament_by_team(region, team_id)

        mock_base_api.raw_request.assert_called_once_with(
            ClashApiV1.__name__,
            clash.tournament_by_team.__name__,
            region,
            f"https://{region}.api.riotgames.com/lol/clash/v1/tournaments/by-team/{team_id}",
            {},
        )

        assert ret is expected_return

    def test_by_tournament(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        clash = ClashApiV1(mock_base_api)
        region = "htr35ge"
        tournament_id = "25979"

        ret = clash.by_tournament(region, tournament_id)

        mock_base_api.raw_request.assert_called_once_with(
            ClashApiV1.__name__,
            clash.by_tournament.__name__,
            region,
            f"https://{region}.api.riotgames.com/lol/clash/v1/tournaments/{tournament_id}",
            {},
        )

        assert ret is expected_return
