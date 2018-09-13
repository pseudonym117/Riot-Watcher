
import sys

if sys.version_info > (3, 0):
    from unittest.mock import MagicMock
else:
    from mock import MagicMock


from riotwatcher._apis import ChampionApiV3


class TestChampionApiV3(object):
    def test_all_default(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.request.return_value = expected_return

        champ = ChampionApiV3(mock_base_api)
        region = 'na1'

        ret = champ.all(region)

        mock_base_api.request.assert_called_once_with(
            ChampionApiV3.__name__,
            champ.all.__name__,
            region,
            '/lol/platform/v3/champions',
            freeToPlay="false"
        )

        assert ret is expected_return

    def test_champions_free_to_play(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.request.return_value = expected_return

        champ = ChampionApiV3(mock_base_api)
        test_region = 'fsfsf'

        ret = champ.all(test_region, free_to_play=True)

        mock_base_api.request.assert_called_once_with(
            ChampionApiV3.__name__,
            champ.all.__name__,
            test_region,
            '/lol/platform/v3/champions',
            freeToPlay="true"
        )

        assert ret is expected_return

    def test_champ_by_id(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.request.return_value = expected_return

        champ = ChampionApiV3(mock_base_api)
        test_region = 'fsfsf'
        champ_id = 75

        ret = champ.by_id(test_region, champ_id)

        mock_base_api.request.assert_called_once_with(
            ChampionApiV3.__name__,
            champ.by_id.__name__,
            test_region,
            '/lol/platform/v3/champions/75'
        )

        assert ret is expected_return

    def test_rotations(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.request.return_value = expected_return

        champ = ChampionApiV3(mock_base_api)
        test_region = 'fhfds'

        ret = champ.rotations(test_region)

        mock_base_api.request.assert_called_once_with(
            ChampionApiV3.__name__,
            champ.rotations.__name__,
            test_region,
            '/lol/platform/v3/champion-rotations',
        )

        assert ret is expected_return
