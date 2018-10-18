
import sys

if sys.version_info > (3, 0):
    from unittest.mock import MagicMock
else:
    from mock import MagicMock


from riotwatcher._apis import ChampionApiV3


class TestChampionApiV3(object):
    def test_rotations(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        champ = ChampionApiV3(mock_base_api)
        test_region = 'fhfds'

        ret = champ.rotations(test_region)

        mock_base_api.raw_request.assert_called_once_with(
            ChampionApiV3.__name__,
            champ.rotations.__name__,
            test_region,
            'https://fhfds.api.riotgames.com/lol/platform/v3/champion-rotations',
            {},
        )

        assert ret is expected_return
