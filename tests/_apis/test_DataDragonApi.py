
import sys

if sys.version_info > (3, 0):
    from unittest.mock import MagicMock
else:
    from mock import MagicMock

    
from riotwatcher._apis import DataDragonApi


class TestDataDragonApi(object):
    def test_all_champions_default(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.request_static.return_value = expected_return

        static_data = DataDragonApi(mock_base_api)

        version = '234'

        ret = static_data.champions(version)

        mock_base_api.request_static.assert_called_once_with(
            version,
            'en_US',
            'champion'
        )

        assert ret is expected_return

    def test_all_champions_full(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.request_static.return_value = expected_return

        static_data = DataDragonApi(mock_base_api)

        version = '234'
        locale = 'asdf'

        ret = static_data.champions(version, True, locale)

        mock_base_api.request_static.assert_called_once_with(
            version,
            locale,
            'championFull'
        )

        assert ret is expected_return

    def test_items(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.request_static.return_value = expected_return

        static_data = DataDragonApi(mock_base_api)

        version = '234'
        locale = 'sdfasdf'

        ret = static_data.items(version, locale)

        mock_base_api.request_static.assert_called_once_with(
            version,
            locale,
            'item'
        )

        assert ret is expected_return

    def test_languages(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.request_static.return_value = expected_return

        static_data = DataDragonApi(mock_base_api)

        version = '234'
        locale = 'sdfasdf'

        ret = static_data.languages(version, locale)

        mock_base_api.request_static.assert_called_once_with(
            version,
            locale,
            'language'
        )

        assert ret is expected_return

    def test_maps(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.request_static.return_value = expected_return

        static_data = DataDragonApi(mock_base_api)

        version = '234'
        locale = 'sdfasdf'

        ret = static_data.maps(version, locale)

        mock_base_api.request_static.assert_called_once_with(
            version,
            locale,
            'map'
        )

        assert ret is expected_return

    def test_masteries(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.request_static.return_value = expected_return

        static_data = DataDragonApi(mock_base_api)

        version = '234'
        locale = 'sdfasdf'

        ret = static_data.masteries(version, locale)

        mock_base_api.request_static.assert_called_once_with(
            version,
            locale,
            'mastery'
        )

        assert ret is expected_return

    def test_profile_icons(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.request_static.return_value = expected_return

        static_data = DataDragonApi(mock_base_api)

        version = '234'
        locale = 'sdfasdf'

        ret = static_data.profile_icons(version, locale)

        mock_base_api.request_static.assert_called_once_with(
            version,
            locale,
            'profileicon'
        )

        assert ret is expected_return

    def test_runes(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.request_static.return_value = expected_return

        static_data = DataDragonApi(mock_base_api)

        version = '234'
        locale = 'sdfasdf'

        ret = static_data.runes(version, locale)

        mock_base_api.request_static.assert_called_once_with(
            version,
            locale,
            'rune'
        )

        assert ret is expected_return

    def test_summoner_spells(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.request_static.return_value = expected_return

        static_data = DataDragonApi(mock_base_api)

        version = '234'
        locale = 'sdfasdf'

        ret = static_data.summoner_spells(version, locale)

        mock_base_api.request_static.assert_called_once_with(
            version,
            locale,
            'summoner'
        )

        assert ret is expected_return

    def test_version(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.request_version.return_value = expected_return

        static_data = DataDragonApi(mock_base_api)

        region = 'euw1'

        ret = static_data.versions_for_region(region)

        mock_base_api.request_version.assert_called_once_with(region)

        assert ret is expected_return
