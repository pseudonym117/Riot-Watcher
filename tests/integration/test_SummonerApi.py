import sys

import pytest

if sys.version_info > (3, 0):
    import unittest.mock as mock
else:
    import mock


@pytest.mark.integration
@pytest.mark.parametrize(
    "region",
    [
        "br1",
        "eun1",
        "euw1",
        "jp1",
        "kr",
        "la1",
        "la2",
        "na",
        "na1",
        "oc1",
        "tr1",
        "ru",
        "pbe1",
    ],
)
class TestSummonerApi(object):
    @pytest.mark.parametrize("account_id", [12345, 99999999999999999999])
    def test_by_account(self, mock_context, region, account_id):
        actual_response = mock_context.watcher.summoner.by_account(region, account_id)

        assert mock_context.expected_response == actual_response
        mock_context.get.assert_called_once_with(
            "https://{region}.api.riotgames.com/lol/summoner/v3/summoners/by-account/{account_id}".format(
                region=region, account_id=account_id
            ),
            params={},
            headers={"X-Riot-Token": mock_context.api_key},
        )

    @pytest.mark.parametrize("summoner_name", ["pseudonym117", "Riot Tuxedo"])
    def test_by_name(self, mock_context, region, summoner_name):
        actual_response = mock_context.watcher.summoner.by_name(region, summoner_name)

        assert mock_context.expected_response == actual_response
        mock_context.get.assert_called_once_with(
            "https://{region}.api.riotgames.com/lol/summoner/v3/summoners/by-name/{summoner_name}".format(
                region=region, summoner_name=summoner_name
            ),
            params={},
            headers={"X-Riot-Token": mock_context.api_key},
        )

    @pytest.mark.parametrize("summoner_id", [12345, 99999999999999999999])
    def test_by_id(self, mock_context, region, summoner_id):
        actual_response = mock_context.watcher.summoner.by_id(region, summoner_id)

        assert mock_context.expected_response == actual_response
        mock_context.get.assert_called_once_with(
            "https://{region}.api.riotgames.com/lol/summoner/v3/summoners/{summoner_id}".format(
                region=region, summoner_id=summoner_id
            ),
            params={},
            headers={"X-Riot-Token": mock_context.api_key},
        )
