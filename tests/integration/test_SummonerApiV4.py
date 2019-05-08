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
class TestSummonerApiV4(object):
    @pytest.mark.parametrize("encrypted_account_id", ["12345", "99999999999999999999"])
    def test_by_account(self, mock_context, region, encrypted_account_id):
        actual_response = mock_context.watcher.summoner.by_account(
            region, encrypted_account_id
        )

        assert mock_context.expected_response == actual_response
        mock_context.get.assert_called_once_with(
            "https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-account/{encrypted_account_id}".format(
                region=region, encrypted_account_id=encrypted_account_id
            ),
            params={},
            headers={"X-Riot-Token": mock_context.api_key},
        )

    @pytest.mark.parametrize("summoner_name", ["pseudonym117", "Riot Tuxedo"])
    def test_by_name(self, mock_context, region, summoner_name):
        actual_response = mock_context.watcher.summoner.by_name(region, summoner_name)

        assert mock_context.expected_response == actual_response
        mock_context.get.assert_called_once_with(
            "https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}".format(
                region=region, summoner_name=summoner_name
            ),
            params={},
            headers={"X-Riot-Token": mock_context.api_key},
        )

    @pytest.mark.parametrize("encrypted_puuid", ["12345", "99999999999999999999"])
    def test_by_puuid(self, mock_context, region, encrypted_puuid):
        actual_response = mock_context.watcher.summoner.by_puuid(
            region, encrypted_puuid
        )

        assert mock_context.expected_response == actual_response
        mock_context.get.assert_called_once_with(
            "https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{encrypted_puuid}".format(
                region=region, encrypted_puuid=encrypted_puuid
            ),
            params={},
            headers={"X-Riot-Token": mock_context.api_key},
        )

    @pytest.mark.parametrize("encrypted_summoner_id", ["12345", "99999999999999999999"])
    def test_by_id(self, mock_context, region, encrypted_summoner_id):
        actual_response = mock_context.watcher.summoner.by_id(
            region, encrypted_summoner_id
        )

        assert mock_context.expected_response == actual_response
        mock_context.get.assert_called_once_with(
            "https://{region}.api.riotgames.com/lol/summoner/v4/summoners/{encrypted_summoner_id}".format(
                region=region, encrypted_summoner_id=encrypted_summoner_id
            ),
            params={},
            headers={"X-Riot-Token": mock_context.api_key},
        )
