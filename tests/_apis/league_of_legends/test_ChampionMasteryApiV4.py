from unittest.mock import MagicMock

import pytest

from riotwatcher._apis.league_of_legends import ChampionMasteryApiV4


@pytest.mark.lol
@pytest.mark.unit
class TestChampionMasteryApiV4:
    def test_by_puuid(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        mastery = ChampionMasteryApiV4(mock_base_api)
        region = "sfsfa"
        puuid = "15357"

        ret = mastery.by_puuid(region, puuid)

        mock_base_api.raw_request.assert_called_once_with(
            ChampionMasteryApiV4.__name__,
            mastery.by_puuid.__name__,
            region,
            f"https://{region}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}",
            {},
        )

        assert ret is expected_return

    def test_by_puuid_by_champion(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        mastery = ChampionMasteryApiV4(mock_base_api)
        region = "fsgs"
        puuid = "53526"
        champion_id = 7

        ret = mastery.by_puuid_by_champion(region, puuid, champion_id)

        mock_base_api.raw_request.assert_called_once_with(
            ChampionMasteryApiV4.__name__,
            mastery.by_puuid_by_champion.__name__,
            region,
            f"https://{region}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}/by-champion/{champion_id}",
            {},
        )

        assert ret is expected_return

    def test_top_by_puuid(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        mastery = ChampionMasteryApiV4(mock_base_api)
        region = "fdsfs"
        puuid = "123415r"
        count = 15

        ret = mastery.top_by_puuid(region, puuid, count=count)

        mock_base_api.raw_request.assert_called_once_with(
            ChampionMasteryApiV4.__name__,
            mastery.top_by_puuid.__name__,
            region,
            f"https://{region}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}/top",
            {"count": count},
        )

        assert ret is expected_return

    def test_top_by_puuid_default_count(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        mastery = ChampionMasteryApiV4(mock_base_api)
        region = "fdsfs"
        puuid = "123415r"

        ret = mastery.top_by_puuid(region, puuid)

        mock_base_api.raw_request.assert_called_once_with(
            ChampionMasteryApiV4.__name__,
            mastery.top_by_puuid.__name__,
            region,
            f"https://{region}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}/top",
            {"count": None},
        )

        assert ret is expected_return

    def test_scores_by_puuid(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        mastery = ChampionMasteryApiV4(mock_base_api)
        region = "fdsfs"
        puuid = "123415r"

        ret = mastery.scores_by_puuid(region, puuid)

        mock_base_api.raw_request.assert_called_once_with(
            ChampionMasteryApiV4.__name__,
            mastery.scores_by_puuid.__name__,
            region,
            f"https://{region}.api.riotgames.com/lol/champion-mastery/v4/scores/by-puuid/{puuid}",
            {},
        )

        assert ret is expected_return
