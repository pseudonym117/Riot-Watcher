from unittest.mock import MagicMock

import pytest

from riotwatcher._apis.league_of_legends import ChallengesApiV1


@pytest.mark.lol
@pytest.mark.unit
class TestChallengesApiV1:
    def test_config(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        challenges = ChallengesApiV1(mock_base_api)
        region = "whoa"

        ret = challenges.config(region)

        mock_base_api.raw_request.assert_called_once_with(
            ChallengesApiV1.__name__,
            challenges.config.__name__,
            region,
            f"https://{region}.api.riotgames.com/lol/challenges/v1/challenges/config",
            {},
        )

        assert ret is expected_return

    def test_percentiles(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        challenges = ChallengesApiV1(mock_base_api)
        region = "this"

        ret = challenges.percentiles(region)

        mock_base_api.raw_request.assert_called_once_with(
            ChallengesApiV1.__name__,
            challenges.percentiles.__name__,
            region,
            f"https://{region}.api.riotgames.com/lol/challenges/v1/challenges/percentiles",
            {},
        )

        assert ret is expected_return

    def test_challenge_config(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        challenges = ChallengesApiV1(mock_base_api)
        region = "is12"
        challenge_id = 628318

        ret = challenges.challenge_config(region, challenge_id)

        mock_base_api.raw_request.assert_called_once_with(
            ChallengesApiV1.__name__,
            challenges.challenge_config.__name__,
            region,
            f"https://{region}.api.riotgames.com/lol/challenges/v1/challenges/{challenge_id}/config",
            {},
        )

        assert ret is expected_return

    def test_leaderboards(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        challenges = ChallengesApiV1(mock_base_api)
        region = "very"
        challenge_id = 101101
        level = "MASTER"

        ret = challenges.leaderboards(region, challenge_id, level)

        mock_base_api.raw_request.assert_called_once_with(
            ChallengesApiV1.__name__,
            challenges.leaderboards.__name__,
            region,
            f"https://{region}.api.riotgames.com/lol/challenges/v1/challenges/{challenge_id}/leaderboards/by-level/{level}",
            {},
        )

        assert ret is expected_return

    def test_percentiles_by_challenge_id(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        challenges = ChallengesApiV1(mock_base_api)
        region = "very"
        challenge_id = 101101

        ret = challenges.percentiles_by_challenge_id(region, challenge_id)

        mock_base_api.raw_request.assert_called_once_with(
            ChallengesApiV1.__name__,
            challenges.percentiles_by_challenge_id.__name__,
            region,
            f"https://{region}.api.riotgames.com/lol/challenges/v1/challenges/{challenge_id}/percentiles",
            {},
        )

        assert ret is expected_return

    def test_by_puuid(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        challenges = ChallengesApiV1(mock_base_api)
        region = "very"
        puuid = "cool123"

        ret = challenges.by_puuid(region, puuid)

        mock_base_api.raw_request.assert_called_once_with(
            ChallengesApiV1.__name__,
            challenges.by_puuid.__name__,
            region,
            f"https://{region}.api.riotgames.com/lol/challenges/v1/player-data/{puuid}",
            {},
        )

        assert ret is expected_return
