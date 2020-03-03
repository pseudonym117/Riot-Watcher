from unittest.mock import MagicMock

import pytest

from riotwatcher._apis.league_of_legends import SummonerApiV4


@pytest.mark.lol
@pytest.mark.unit
class TestSummonerApiV4:
    def test_by_account(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        summoner = SummonerApiV4(mock_base_api)
        region = "htr35ge"
        encrypted_account_id = "98532"

        ret = summoner.by_account(region, encrypted_account_id)

        mock_base_api.raw_request.assert_called_once_with(
            SummonerApiV4.__name__,
            summoner.by_account.__name__,
            region,
            f"https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-account/{encrypted_account_id}",
            {},
        )

        assert ret is expected_return

    def test_by_name(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        summoner = SummonerApiV4(mock_base_api)
        region = "htr35ge"
        summoner_name = "psesn886"

        ret = summoner.by_name(region, summoner_name)

        mock_base_api.raw_request.assert_called_once_with(
            SummonerApiV4.__name__,
            summoner.by_name.__name__,
            region,
            f"https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}",
            {},
        )

        assert ret is expected_return

    def test_by_puuid(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        summoner = SummonerApiV4(mock_base_api)
        region = "htr35ge"
        encrypted_puuid = "hello123"

        ret = summoner.by_puuid(region, encrypted_puuid)

        mock_base_api.raw_request.assert_called_once_with(
            SummonerApiV4.__name__,
            summoner.by_puuid.__name__,
            region,
            f"https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{encrypted_puuid}",
            {},
        )

        assert ret is expected_return

    def test_by_id(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        summoner = SummonerApiV4(mock_base_api)
        region = "htr35ge"
        encrypted_summoner_id = "25979"

        ret = summoner.by_id(region, encrypted_summoner_id)

        mock_base_api.raw_request.assert_called_once_with(
            SummonerApiV4.__name__,
            summoner.by_id.__name__,
            region,
            f"https://{region}.api.riotgames.com/lol/summoner/v4/summoners/{encrypted_summoner_id}",
            {},
        )

        assert ret is expected_return
