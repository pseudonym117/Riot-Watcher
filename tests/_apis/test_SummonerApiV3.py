
import sys

if sys.version_info > (3, 0):
    from unittest.mock import MagicMock
else:
    from mock import MagicMock

from riotwatcher._apis import SummonerApiV3


class TestSummonerApiV3(object):
    def test_by_account(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        summoner = SummonerApiV3(mock_base_api)
        region = 'htr35ge'
        account_id = 98532

        ret = summoner.by_account(region, account_id)

        mock_base_api.raw_request.assert_called_once_with(
            SummonerApiV3.__name__,
            summoner.by_account.__name__,
            region,
            'https://htr35ge.api.riotgames.com/lol/summoner/v3/summoners/by-account/{accountId}'.format(
                accountId=account_id,
            ),
            {},
        )

        assert ret is expected_return

    def test_by_name(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        summoner = SummonerApiV3(mock_base_api)
        region = 'htr35ge'
        summoner_name = 'psesn886'

        ret = summoner.by_name(region, summoner_name)

        mock_base_api.raw_request.assert_called_once_with(
            SummonerApiV3.__name__,
            summoner.by_name.__name__,
            region,
            'https://htr35ge.api.riotgames.com/lol/summoner/v3/summoners/by-name/{summonerName}'.format(
                summonerName=summoner_name,
            ),
            {},
        )

        assert ret is expected_return

    def test_by_id(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        summoner = SummonerApiV3(mock_base_api)
        region = 'htr35ge'
        summoner_id = 25979

        ret = summoner.by_id(region, summoner_id)

        mock_base_api.raw_request.assert_called_once_with(
            SummonerApiV3.__name__,
            summoner.by_id.__name__,
            region,
            'https://htr35ge.api.riotgames.com/lol/summoner/v3/summoners/{summonerId}'.format(
                summonerId=summoner_id,
            ),
            {},
        )

        assert ret is expected_return
