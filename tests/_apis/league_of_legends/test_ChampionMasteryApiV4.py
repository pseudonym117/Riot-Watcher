from unittest.mock import MagicMock

import pytest

from riotwatcher._apis.league_of_legends import ChampionMasteryApiV4


@pytest.mark.lol
@pytest.mark.unit
class TestChampionMasteryApiV4:
    def test_by_summoner(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        mastery = ChampionMasteryApiV4(mock_base_api)
        region = "afas"
        encrypted_summoner_id = "15462"

        ret = mastery.by_summoner(region, encrypted_summoner_id)

        mock_base_api.raw_request.assert_called_once_with(
            ChampionMasteryApiV4.__name__,
            mastery.by_summoner.__name__,
            region,
            f"https://{region}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{encrypted_summoner_id}",
            {},
        )

        assert ret is expected_return

    def test_summoner_by_champion(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        mastery = ChampionMasteryApiV4(mock_base_api)
        region = "fsgs"
        encrypted_summoner_id = "53526"
        champion_id = 7

        ret = mastery.by_summoner_by_champion(
            region, encrypted_summoner_id, champion_id
        )

        mock_base_api.raw_request.assert_called_once_with(
            ChampionMasteryApiV4.__name__,
            mastery.by_summoner_by_champion.__name__,
            region,
            f"https://{region}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{encrypted_summoner_id}/by-champion/{champion_id}",
            {},
        )

        assert ret is expected_return

    def test_scored_by_summoner(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        mastery = ChampionMasteryApiV4(mock_base_api)
        region = "fsgs"
        encrypted_summoner_id = "6243"

        ret = mastery.scores_by_summoner(region, encrypted_summoner_id)

        mock_base_api.raw_request.assert_called_once_with(
            ChampionMasteryApiV4.__name__,
            mastery.scores_by_summoner.__name__,
            region,
            f"https://{region}.api.riotgames.com/lol/champion-mastery/v4/scores/by-summoner/{encrypted_summoner_id}",
            {},
        )

        assert ret is expected_return
