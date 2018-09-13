
import sys

if sys.version_info > (3, 0):
    from unittest.mock import MagicMock
else:
    from mock import MagicMock

from riotwatcher._apis import SpectatorApiV3


class TestSpectatorApiV3TestCase(object):
    def test_by_summoner(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.request.return_value = expected_return

        spectator = SpectatorApiV3(mock_base_api)
        region = 'agagd'
        summoner_id = 98532

        ret = spectator.by_summoner(region, summoner_id)

        mock_base_api.request.assert_called_once_with(
            SpectatorApiV3.__name__,
            spectator.by_summoner.__name__,
            region,
            '/lol/spectator/v3/active-games/by-summoner/{summonerId}'.format(summonerId=summoner_id)
        )

        assert ret is expected_return

    def test_featured_games(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.request.return_value = expected_return

        spectator = SpectatorApiV3(mock_base_api)
        region = 'hfh42'

        ret = spectator.featured_games(region)

        mock_base_api.request.assert_called_once_with(
            SpectatorApiV3.__name__,
            spectator.featured_games.__name__,
            region,
            '/lol/spectator/v3/featured-games'
        )

        assert ret is expected_return
