import sys

import pytest

if sys.version_info > (3, 0):
    from unittest.mock import MagicMock
else:
    from mock import MagicMock


from riotwatcher._apis import DataDragonApi


@pytest.mark.unit
class TestDataDragonApi(object):
    def test_all_champions_default(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request_static.return_value = expected_return

        static_data = DataDragonApi(mock_base_api)

        version = "234"

        ret = static_data.champions(version)

        mock_base_api.raw_request_static.assert_called_once_with(
            "https://ddragon.leagueoflegends.com/cdn/{version}/data/{locale}/champion.json".format(
                version=version, locale="en_US"
            ),
            {},
        )

        assert ret is expected_return

    def test_all_champions_full(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request_static.return_value = expected_return

        static_data = DataDragonApi(mock_base_api)

        version = "234"
        locale = "asdf"

        ret = static_data.champions(version, True, locale)

        mock_base_api.raw_request_static.assert_called_once_with(
            "https://ddragon.leagueoflegends.com/cdn/{version}/data/{locale}/championFull.json".format(
                version=version, locale=locale
            ),
            {},
        )

        assert ret is expected_return

    def test_items(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request_static.return_value = expected_return

        static_data = DataDragonApi(mock_base_api)

        version = "234"
        locale = "sdfasdf"

        ret = static_data.items(version, locale)

        mock_base_api.raw_request_static.assert_called_once_with(
            "https://ddragon.leagueoflegends.com/cdn/{version}/data/{locale}/item.json".format(
                version=version, locale=locale
            ),
            {},
        )

        assert ret is expected_return

    def test_languages(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request_static.return_value = expected_return

        static_data = DataDragonApi(mock_base_api)

        version = "234"
        locale = "sdfasdf"

        ret = static_data.languages(version, locale)

        mock_base_api.raw_request_static.assert_called_once_with(
            "https://ddragon.leagueoflegends.com/cdn/{version}/data/{locale}/language.json".format(
                version=version, locale=locale
            ),
            {},
        )

        assert ret is expected_return

    def test_maps(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request_static.return_value = expected_return

        static_data = DataDragonApi(mock_base_api)

        version = "234"
        locale = "sdfasdf"

        ret = static_data.maps(version, locale)

        mock_base_api.raw_request_static.assert_called_once_with(
            "https://ddragon.leagueoflegends.com/cdn/{version}/data/{locale}/map.json".format(
                version=version, locale=locale
            ),
            {},
        )

        assert ret is expected_return

    def test_masteries(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request_static.return_value = expected_return

        static_data = DataDragonApi(mock_base_api)

        version = "234"
        locale = "sdfasdf"

        ret = static_data.masteries(version, locale)

        mock_base_api.raw_request_static.assert_called_once_with(
            "https://ddragon.leagueoflegends.com/cdn/{version}/data/{locale}/mastery.json".format(
                version=version, locale=locale
            ),
            {},
        )

        assert ret is expected_return

    def test_profile_icons(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request_static.return_value = expected_return

        static_data = DataDragonApi(mock_base_api)

        version = "234"
        locale = "sdfasdf"

        ret = static_data.profile_icons(version, locale)

        mock_base_api.raw_request_static.assert_called_once_with(
            "https://ddragon.leagueoflegends.com/cdn/{version}/data/{locale}/profileicon.json".format(
                version=version, locale=locale
            ),
            {},
        )

        assert ret is expected_return

    def test_runes(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request_static.return_value = expected_return

        static_data = DataDragonApi(mock_base_api)

        version = "234"
        locale = "sdfasdf"

        ret = static_data.runes(version, locale)

        mock_base_api.raw_request_static.assert_called_once_with(
            "https://ddragon.leagueoflegends.com/cdn/{version}/data/{locale}/rune.json".format(
                version=version, locale=locale
            ),
            {},
        )

        assert ret is expected_return

    def test_runes_reforged(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request_static.return_value = expected_return

        static_data = DataDragonApi(mock_base_api)

        version = "234"
        locale = "sdfasdf"

        ret = static_data.runes_reforged(version, locale)

        mock_base_api.raw_request_static.assert_called_once_with(
            "https://ddragon.leagueoflegends.com/cdn/{version}/data/{locale}/runesReforged.json".format(
                version=version, locale=locale
            ),
            {},
        )

        assert ret is expected_return

    def test_summoner_spells(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request_static.return_value = expected_return

        static_data = DataDragonApi(mock_base_api)

        version = "234"
        locale = "sdfasdf"

        ret = static_data.summoner_spells(version, locale)

        mock_base_api.raw_request_static.assert_called_once_with(
            "https://ddragon.leagueoflegends.com/cdn/{version}/data/{locale}/summoner.json".format(
                version=version, locale=locale
            ),
            {},
        )

        assert ret is expected_return

    def test_version(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request_static.return_value = expected_return

        static_data = DataDragonApi(mock_base_api)

        region = "euw1"

        ret = static_data.versions_for_region(region)

        mock_base_api.raw_request_static.assert_called_once_with(
            "https://ddragon.leagueoflegends.com/realms/{region}.json".format(
                region="euw"
            ),
            {},
        )

        assert ret is expected_return
