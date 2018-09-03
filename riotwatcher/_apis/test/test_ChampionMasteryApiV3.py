
import sys

if sys.version_info > (3, 0):
    from unittest.mock import MagicMock
else:
    from mock import MagicMock

from .. import ChampionMasteryApiV3


class TestChampionMasteryApiV3(object):
    def test_by_summoner(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.request.return_value = expected_return

        mastery = ChampionMasteryApiV3(mock_base_api)
        region = 'afas'
        summoner_id = 15462

        ret = mastery.by_summoner(region, summoner_id)

        mock_base_api.request.assert_called_once_with(
            ChampionMasteryApiV3.__name__,
            mastery.by_summoner.__name__,
            region,
            '/lol/champion-mastery/v3/champion-masteries/by-summoner/15462'
        )

        assert ret is expected_return

    def test_summoner_by_champion(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.request.return_value = expected_return

        mastery = ChampionMasteryApiV3(mock_base_api)
        region = 'fsgs'
        summoner_id = 53526
        champion_id = 7

        ret = mastery.by_summoner_by_champion(region, summoner_id, champion_id)

        mock_base_api.request.assert_called_once_with(
            ChampionMasteryApiV3.__name__,
            mastery.by_summoner_by_champion.__name__,
            region,
            '/lol/champion-mastery/v3/champion-masteries/by-summoner/53526/by-champion/7'
        )

        assert ret is expected_return

    def test_scored_by_summoner(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.request.return_value = expected_return

        mastery = ChampionMasteryApiV3(mock_base_api)
        region = 'fsgs'
        summoner_id = 6243

        ret = mastery.scores_by_summoner(region, summoner_id)

        mock_base_api.request.assert_called_once_with(
            ChampionMasteryApiV3.__name__,
            mastery.scores_by_summoner.__name__,
            region,
            '/lol/champion-mastery/v3/scores/by-summoner/6243'
        )

        assert ret is expected_return
