import sys

import pytest

if sys.version_info > (3, 0):
    from unittest.mock import MagicMock
else:
    from mock import MagicMock

from riotwatcher._apis import SpectatorApiV4


@pytest.mark.unit
class TestSpectatorApiV4(object):
    def test_by_summoner(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        spectator = SpectatorApiV4(mock_base_api)
        region = "agagd"
        encrypted_summoner_id = "98532"

        ret = spectator.by_summoner(region, encrypted_summoner_id)

        mock_base_api.raw_request.assert_called_once_with(
            SpectatorApiV4.__name__,
            spectator.by_summoner.__name__,
            region,
            "https://agagd.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/{encrypted_summoner_id}".format(
                encrypted_summoner_id=encrypted_summoner_id
            ),
            {},
        )

        assert ret is expected_return

    def test_featured_games(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        spectator = SpectatorApiV4(mock_base_api)
        region = "hfh42"

        ret = spectator.featured_games(region)

        mock_base_api.raw_request.assert_called_once_with(
            SpectatorApiV4.__name__,
            spectator.featured_games.__name__,
            region,
            "https://hfh42.api.riotgames.com/lol/spectator/v4/featured-games",
            {},
        )

        assert ret is expected_return
