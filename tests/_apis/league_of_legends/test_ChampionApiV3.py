from unittest.mock import MagicMock

import pytest

from riotwatcher._apis.league_of_legends import ChampionApiV3


@pytest.mark.lol
@pytest.mark.unit
class TestChampionApiV3:
    def test_rotations(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        champ = ChampionApiV3(mock_base_api)
        test_region = "fhfds"

        ret = champ.rotations(test_region)

        mock_base_api.raw_request.assert_called_once_with(
            ChampionApiV3.__name__,
            champ.rotations.__name__,
            test_region,
            f"https://{test_region}.api.riotgames.com/lol/platform/v3/champion-rotations",
            {},
        )

        assert ret is expected_return
