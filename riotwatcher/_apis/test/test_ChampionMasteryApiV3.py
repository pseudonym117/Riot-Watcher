
import unittest
import sys

if sys.version_info > (3, 0):
    from unittest.mock import MagicMock
else:
    from mock import MagicMock

from .. import ChampionMasteryApiV3


class ChampionMasteryApiV3TestCase(unittest.TestCase):
    def setUp(self):
        self._expected_return = object()

        self._base_api_mock = MagicMock(name='base_api')
        self._base_api_mock.request = MagicMock(name='request')
        self._base_api_mock.request.return_value = self._expected_return

    def test_by_summoner(self):
        mastery = ChampionMasteryApiV3(self._base_api_mock)
        region = 'afas'
        summoner_id = 15462

        ret = mastery.by_summoner(region, summoner_id)

        self._base_api_mock.request.assert_called_once_with(
            ChampionMasteryApiV3.__name__,
            mastery.by_summoner.__name__,
            region,
            '/lol/champion-mastery/v3/champion-masteries/by-summoner/15462'
        )

        self.assertIs(self._expected_return, ret)

    def test_summoner_by_champion(self):
        mastery = ChampionMasteryApiV3(self._base_api_mock)
        region = 'fsgs'
        summoner_id = 53526
        champion_id = 7

        ret = mastery.by_summoner_by_champion(region, summoner_id, champion_id)

        self._base_api_mock.request.assert_called_once_with(
            ChampionMasteryApiV3.__name__,
            mastery.by_summoner_by_champion.__name__,
            region,
            '/lol/champion-mastery/v3/champion-masteries/by-summoner/53526/by-champion/7'
        )

        self.assertIs(self._expected_return, ret)

    def test_scored_by_summoner(self):
        mastery = ChampionMasteryApiV3(self._base_api_mock)
        region = 'fsgs'
        summoner_id = 6243

        ret = mastery.scores_by_summoner(region, summoner_id)

        self._base_api_mock.request.assert_called_once_with(
            ChampionMasteryApiV3.__name__,
            mastery.scores_by_summoner.__name__,
            region,
            '/lol/champion-mastery/v3/scores/by-summoner/6243'
        )

        self.assertIs(self._expected_return, ret)
