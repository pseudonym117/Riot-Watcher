from unittest.mock import MagicMock

import pytest

from riotwatcher._apis.riot import AccountApi


@pytest.fixture(params=["pseudonym"])
def ign(request):
    return request.param


@pytest.fixture(params=["sudo"])
def tag(request):
    return request.param


@pytest.fixture(params=["val", "lor"])
def game(request):
    return request.param


@pytest.mark.riot
@pytest.mark.unit
class TestAccountApi:
    def test_by_puuid(self, region, puuid):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        account = AccountApi(mock_base_api)

        ret = account.by_puuid(region, puuid)

        mock_base_api.raw_request.assert_called_once_with(
            AccountApi.__name__,
            account.by_puuid.__name__,
            region,
            f"https://{region}.api.riotgames.com/riot/account/v1/accounts/by-puuid/{puuid}",
            {},
        )

        assert ret is expected_return

    def test_by_riot_id(self, region, ign, tag):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        account = AccountApi(mock_base_api)

        ret = account.by_riot_id(region, ign, tag)

        mock_base_api.raw_request.assert_called_once_with(
            AccountApi.__name__,
            account.by_riot_id.__name__,
            region,
            f"https://{region}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{ign}/{tag}",
            {},
        )

        assert ret is expected_return

    def test_active_shard(self, region, game, puuid):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        account = AccountApi(mock_base_api)

        ret = account.active_shard(region, game, puuid)

        mock_base_api.raw_request.assert_called_once_with(
            AccountApi.__name__,
            account.active_shard.__name__,
            region,
            f"https://{region}.api.riotgames.com/riot/account/v1/active-shards/by-game/{game}/by-puuid/{puuid}",
            {},
        )

        assert ret is expected_return
