from unittest.mock import MagicMock

import pytest

from riotwatcher._apis.team_fight_tactics import SummonerApi


@pytest.mark.tft
@pytest.mark.unit
class TestSummonerApi:
    def test_by_account(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        summoner = SummonerApi(mock_base_api)
        region = "afas"
        encrypted_account_id = "15asf2-54321"

        ret = summoner.by_account(region, encrypted_account_id)

        mock_base_api.raw_request.assert_called_once_with(
            SummonerApi.__name__,
            summoner.by_account.__name__,
            region,
            f"https://{region}.api.riotgames.com/tft/summoner/v1/summoners/by-account/{encrypted_account_id}",
            {},
        )

        assert ret is expected_return

    def test_by_name(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        summoner = SummonerApi(mock_base_api)
        region = "afas"
        summoner_name = "pseudonym117"

        ret = summoner.by_name(region, summoner_name)

        mock_base_api.raw_request.assert_called_once_with(
            SummonerApi.__name__,
            summoner.by_name.__name__,
            region,
            f"https://{region}.api.riotgames.com/tft/summoner/v1/summoners/by-name/{summoner_name}",
            {},
        )

        assert ret is expected_return

    def test_by_puuid(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        summoner = SummonerApi(mock_base_api)
        region = "afas"
        puuid = "15462gsfg321"

        ret = summoner.by_puuid(region, puuid)

        mock_base_api.raw_request.assert_called_once_with(
            SummonerApi.__name__,
            summoner.by_puuid.__name__,
            region,
            f"https://{region}.api.riotgames.com/tft/summoner/v1/summoners/by-puuid/{puuid}",
            {},
        )

        assert ret is expected_return

    def test_by_id(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        summoner = SummonerApi(mock_base_api)
        region = "afas"
        encrypted_summoner_id = "sdfgasg222"

        ret = summoner.by_id(region, encrypted_summoner_id)

        mock_base_api.raw_request.assert_called_once_with(
            SummonerApi.__name__,
            summoner.by_id.__name__,
            region,
            f"https://{region}.api.riotgames.com/tft/summoner/v1/summoners/{encrypted_summoner_id}",
            {},
        )

        assert ret is expected_return
