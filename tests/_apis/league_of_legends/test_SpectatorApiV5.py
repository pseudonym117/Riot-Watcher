from unittest.mock import MagicMock

import pytest

from riotwatcher._apis.league_of_legends import SpectatorApiV5


@pytest.mark.lol
@pytest.mark.unit
class TestSpectatorApiV5:
    def test_by_summoner(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        spectator = SpectatorApiV5(mock_base_api)
        region = "agagd"
        encrypted_puuid = "98532"

        ret = spectator.by_summoner(region, encrypted_puuid)

        mock_base_api.raw_request.assert_called_once_with(
            SpectatorApiV5.__name__,
            spectator.by_summoner.__name__,
            region,
            f"https://{region}.api.riotgames.com/lol/spectator/v5/active-games/by-summoner/{encrypted_puuid}",
            {},
        )

        assert ret is expected_return

    def test_featured_games(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        spectator = SpectatorApiV5(mock_base_api)
        region = "hfh42"

        ret = spectator.featured_games(region)

        mock_base_api.raw_request.assert_called_once_with(
            SpectatorApiV5.__name__,
            spectator.featured_games.__name__,
            region,
            f"https://{region}.api.riotgames.com/lol/spectator/v5/featured-games",
            {},
        )

        assert ret is expected_return
