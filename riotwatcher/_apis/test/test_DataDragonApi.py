import unittest
import sys

if sys.version_info > (3, 0):
    from unittest.mock import MagicMock
else:
    from mock import MagicMock
from .. import DataDragonApi


class DataDragonApiTestCase(unittest.TestCase):
    def setUp(self):
        self._expected_return = object()

        self._base_api_mock = MagicMock(name='base_api')
        self._base_api_mock.request_static = MagicMock(name='request_static')
        self._base_api_mock.request_static.return_value = self._expected_return

    def test_all_champions_default(self):
        static_data = DataDragonApi(self._base_api_mock)

        version = '234'

        ret = static_data.champions(version)

        self._base_api_mock.request_static.assert_called_once_with(
            version,
            'en_US',
            'champion'
        )

        self.assertIs(self._expected_return, ret)

    def test_all_champions_full(self):
        static_data = DataDragonApi(self._base_api_mock)

        version = '234'
        locale = 'asdf'

        ret = static_data.champions(version, True, locale)

        self._base_api_mock.request_static.assert_called_once_with(
            version,
            locale,
            'championFull'
        )

        self.assertIs(self._expected_return, ret)

    def test_items(self):
        static_data = DataDragonApi(self._base_api_mock)

        version = '234'
        locale = 'sdfasdf'

        ret = static_data.items(version, locale)

        self._base_api_mock.request_static.assert_called_once_with(
            version,
            locale,
            'item'
        )

        self.assertIs(self._expected_return, ret)

    def test_languages(self):
        static_data = DataDragonApi(self._base_api_mock)

        version = '234'
        locale = 'sdfasdf'

        ret = static_data.languages(version, locale)

        self._base_api_mock.request_static.assert_called_once_with(
            version,
            locale,
            'language'
        )

        self.assertIs(self._expected_return, ret)

    def test_maps(self):
        static_data = DataDragonApi(self._base_api_mock)

        version = '234'
        locale = 'sdfasdf'

        ret = static_data.maps(version, locale)

        self._base_api_mock.request_static.assert_called_once_with(
            version,
            locale,
            'map'
        )

        self.assertIs(self._expected_return, ret)

    def test_masteries(self):
        static_data = DataDragonApi(self._base_api_mock)

        version = '234'
        locale = 'sdfasdf'

        ret = static_data.masteries(version, locale)

        self._base_api_mock.request_static.assert_called_once_with(
            version,
            locale,
            'mastery'
        )

        self.assertIs(self._expected_return, ret)

    def test_profile_icons(self):
        static_data = DataDragonApi(self._base_api_mock)

        version = '234'
        locale = 'sdfasdf'

        ret = static_data.profileIcons(version, locale)

        self._base_api_mock.request_static.assert_called_once_with(
            version,
            locale,
            'profileicon'
        )

        self.assertIs(self._expected_return, ret)

    def test_runes(self):
        static_data = DataDragonApi(self._base_api_mock)

        version = '234'
        locale = 'sdfasdf'

        ret = static_data.runes(version, locale)

        self._base_api_mock.request_static.assert_called_once_with(
            version,
            locale,
            'rune'
        )

        self.assertIs(self._expected_return, ret)

    def test_summoner_spells(self):
        static_data = DataDragonApi(self._base_api_mock)

        version = '234'
        locale = 'sdfasdf'

        ret = static_data.summonerSpells(version, locale)

        self._base_api_mock.request_static.assert_called_once_with(
            version,
            locale,
            'summoner'
        )

        self.assertIs(self._expected_return, ret)
