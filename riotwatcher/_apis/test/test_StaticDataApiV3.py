
import unittest
import sys

if sys.version_info > (3, 0):
    from unittest.mock import MagicMock
else:
    from mock import MagicMock

from .. import StaticDataApiV3


class StaticDataApiV3TestCase(unittest.TestCase):
    def setUp(self):
        self._expected_return = object()

        self._base_api_mock = MagicMock(name='base_api')
        self._base_api_mock.request = MagicMock(name='request')
        self._base_api_mock.request.return_value = self._expected_return

    def test_all_champions_default(self):
        static_data = StaticDataApiV3(self._base_api_mock)
        region = 'agdgdahm'

        ret = static_data.champions(region)

        self._base_api_mock.request.assert_called_once_with(
            StaticDataApiV3.__name__,
            static_data.champions.__name__,
            region,
            '/lol/static-data/v3/champions',
            locale=None,
            version=None,
            tags=None,
            dataById=None
        )

        self.assertIs(self._expected_return, ret)

    def test_all_champions(self):
        static_data = StaticDataApiV3(self._base_api_mock)
        region = 'agdgdahm'
        locale = 'enjd'
        version = '5.32a'
        tags = ['hello', 'another', 'one']
        data_by_id = True

        ret = static_data.champions(
            region,
            locale=locale,
            version=version,
            tags=tags,
            data_by_id=data_by_id
        )

        self._base_api_mock.request.assert_called_once_with(
            StaticDataApiV3.__name__,
            static_data.champions.__name__,
            region,
            '/lol/static-data/v3/champions',
            locale=locale,
            version=version,
            tags=tags,
            dataById=data_by_id
        )

        self.assertIs(self._expected_return, ret)

    def test_champion_default(self):
        static_data = StaticDataApiV3(self._base_api_mock)
        region = 'agdgdahm'
        champion_id = 264647

        ret = static_data.champion(region, champion_id)

        self._base_api_mock.request.assert_called_once_with(
            StaticDataApiV3.__name__,
            static_data.champion.__name__,
            region,
            '/lol/static-data/v3/champions/{id}'.format(id=champion_id),
            locale=None,
            version=None,
            tags=None
        )

        self.assertIs(self._expected_return, ret)

    def test_champion(self):
        static_data = StaticDataApiV3(self._base_api_mock)
        region = 'agdgdahm'
        champion_id = 264647
        locale = 'egh2'
        version = '3t5.32a'
        tags = ['jbe', 'eherhw', 'qtqq']

        ret = static_data.champion(
            region,
            champion_id,
            locale=locale,
            version=version,
            tags=tags
        )

        self._base_api_mock.request.assert_called_once_with(
            StaticDataApiV3.__name__,
            static_data.champion.__name__,
            region,
            '/lol/static-data/v3/champions/{id}'.format(id=champion_id),
            locale=locale,
            version=version,
            tags=tags
        )

        self.assertIs(self._expected_return, ret)

    def test_all_items_default(self):
        static_data = StaticDataApiV3(self._base_api_mock)
        region = 'agdgdahm'

        ret = static_data.items(region)

        self._base_api_mock.request.assert_called_once_with(
            StaticDataApiV3.__name__,
            static_data.items.__name__,
            region,
            '/lol/static-data/v3/items',
            locale=None,
            version=None,
            tags=None
        )

        self.assertIs(self._expected_return, ret)

    def test_all_items(self):
        static_data = StaticDataApiV3(self._base_api_mock)
        region = 'asassahjjn'
        locale = 'ahadhe'
        version = 'ffs3.32a'
        tags = ['aasga', 'h54iu6', 'three']

        ret = static_data.items(
            region,
            locale=locale,
            version=version,
            tags=tags
        )

        self._base_api_mock.request.assert_called_once_with(
            StaticDataApiV3.__name__,
            static_data.items.__name__,
            region,
            '/lol/static-data/v3/items',
            locale=locale,
            version=version,
            tags=tags
        )

        self.assertIs(self._expected_return, ret)

    def test_item_default(self):
        static_data = StaticDataApiV3(self._base_api_mock)
        region = 'agdgdahm'
        item_id = 2347

        ret = static_data.item(region, item_id)

        self._base_api_mock.request.assert_called_once_with(
            StaticDataApiV3.__name__,
            static_data.item.__name__,
            region,
            '/lol/static-data/v3/items/{id}'.format(id=item_id),
            locale=None,
            version=None,
            tags=None
        )

        self.assertIs(self._expected_return, ret)

    def test_item(self):
        static_data = StaticDataApiV3(self._base_api_mock)
        region = 'ag51e'
        champion_id = 84531
        locale = 'dhahe'
        version = 'afs.32a'
        tags = ['wery', '274hb', 'akek']

        ret = static_data.item(
            region,
            champion_id,
            locale=locale,
            version=version,
            tags=tags
        )

        self._base_api_mock.request.assert_called_once_with(
            StaticDataApiV3.__name__,
            static_data.item.__name__,
            region,
            '/lol/static-data/v3/items/{id}'.format(id=champion_id),
            locale=locale,
            version=version,
            tags=tags
        )

        self.assertIs(self._expected_return, ret)

    def test_language_strings_default(self):
        static_data = StaticDataApiV3(self._base_api_mock)
        region = 'ag51e'

        ret = static_data.language_strings(region)

        self._base_api_mock.request.assert_called_once_with(
            StaticDataApiV3.__name__,
            static_data.language_strings.__name__,
            region,
            '/lol/static-data/v3/language-strings',
            locale=None,
            version=None
        )

        self.assertIs(self._expected_return, ret)

    def test_language_strings(self):
        static_data = StaticDataApiV3(self._base_api_mock)
        region = 'j5tj5nnnnn'
        locale = 'eheq'
        version = 'ddag.32a'

        ret = static_data.language_strings(
            region,
            locale=locale,
            version=version
        )

        self._base_api_mock.request.assert_called_once_with(
            StaticDataApiV3.__name__,
            static_data.language_strings.__name__,
            region,
            '/lol/static-data/v3/language-strings',
            locale=locale,
            version=version
        )

        self.assertIs(self._expected_return, ret)

    def test_languages(self):
        static_data = StaticDataApiV3(self._base_api_mock)
        region = 'afaga'

        ret = static_data.languages(region)

        self._base_api_mock.request.assert_called_once_with(
            StaticDataApiV3.__name__,
            static_data.languages.__name__,
            region,
            '/lol/static-data/v3/languages',
        )

        self.assertIs(self._expected_return, ret)

    def test_maps(self):
        static_data = StaticDataApiV3(self._base_api_mock)
        region = 'afasg33v'
        locale = 'sfah222'
        version = '4.20b'

        ret = static_data.maps(region, locale=locale, version=version)

        self._base_api_mock.request.assert_called_once_with(
            StaticDataApiV3.__name__,
            static_data.maps.__name__,
            region,
            '/lol/static-data/v3/maps',
            locale=locale,
            version=version
        )

        self.assertIs(self._expected_return, ret)

    def test_maps_default(self):
        static_data = StaticDataApiV3(self._base_api_mock)
        region = 'sdsdsjjjjjjrf'

        ret = static_data.maps(region)

        self._base_api_mock.request.assert_called_once_with(
            StaticDataApiV3.__name__,
            static_data.maps.__name__,
            region,
            '/lol/static-data/v3/maps',
            locale=None,
            version=None
        )

        self.assertIs(self._expected_return, ret)

    def test_masteries(self):
        static_data = StaticDataApiV3(self._base_api_mock)
        region = 'sdgsvrw4'
        locale = 'dsgdsg34'
        version = '4.20b'
        tags = ['safa122', 'fw3fb2', 'asfa']

        ret = static_data.masteries(region, locale=locale, version=version, tags=tags)

        self._base_api_mock.request.assert_called_once_with(
            StaticDataApiV3.__name__,
            static_data.masteries.__name__,
            region,
            '/lol/static-data/v3/masteries',
            locale=locale,
            version=version,
            tags=tags
        )

        self.assertIs(self._expected_return, ret)

    def test_masteries_default(self):
        static_data = StaticDataApiV3(self._base_api_mock)
        region = 'asfa331g1ggg'

        ret = static_data.masteries(region)

        self._base_api_mock.request.assert_called_once_with(
            StaticDataApiV3.__name__,
            static_data.masteries.__name__,
            region,
            '/lol/static-data/v3/masteries',
            locale=None,
            version=None,
            tags=None
        )

        self.assertIs(self._expected_return, ret)

    def test_mastery(self):
        static_data = StaticDataApiV3(self._base_api_mock)
        region = 'asfav32'
        mastery_id = 6274
        locale = 'j645wk'
        version = '4.iopn83'
        tags = ['asdj5', 'mut', 'r3hrb']

        ret = static_data.mastery(region, mastery_id, locale=locale, version=version, tags=tags)

        self._base_api_mock.request.assert_called_once_with(
            StaticDataApiV3.__name__,
            static_data.mastery.__name__,
            region,
            '/lol/static-data/v3/masteries/{id}'.format(id=mastery_id),
            locale=locale,
            version=version,
            tags=tags
        )

        self.assertIs(self._expected_return, ret)

    def test_mastery_default(self):
        static_data = StaticDataApiV3(self._base_api_mock)
        region = 'asfsafav'
        mastery_id = 9826

        ret = static_data.mastery(region, mastery_id)

        self._base_api_mock.request.assert_called_once_with(
            StaticDataApiV3.__name__,
            static_data.mastery.__name__,
            region,
            '/lol/static-data/v3/masteries/{id}'.format(id=mastery_id),
            locale=None,
            version=None,
            tags=None
        )

        self.assertIs(self._expected_return, ret)

    def test_profile_icons_default(self):
        static_data = StaticDataApiV3(self._base_api_mock)
        region = 'gewv4'

        ret = static_data.profile_icons(region)

        self._base_api_mock.request.assert_called_once_with(
            StaticDataApiV3.__name__,
            static_data.profile_icons.__name__,
            region,
            '/lol/static-data/v3/profile-icons',
            locale=None,
            version=None
        )

        self.assertIs(self._expected_return, ret)

    def test_profile_icons(self):
        static_data = StaticDataApiV3(self._base_api_mock)
        region = 'gewv4'
        locale = 'afnnn64'
        version = '27yhtgf'

        ret = static_data.profile_icons(region, locale=locale, version=version)

        self._base_api_mock.request.assert_called_once_with(
            StaticDataApiV3.__name__,
            static_data.profile_icons.__name__,
            region,
            '/lol/static-data/v3/profile-icons',
            locale=locale,
            version=version
        )

        self.assertIs(self._expected_return, ret)

    def test_realms(self):
        static_data = StaticDataApiV3(self._base_api_mock)
        region = 'asfb222rf76'

        ret = static_data.realms(region)

        self._base_api_mock.request.assert_called_once_with(
            StaticDataApiV3.__name__,
            static_data.realms.__name__,
            region,
            '/lol/static-data/v3/realms',
        )

        self.assertIs(self._expected_return, ret)

    def test_runes(self):
        static_data = StaticDataApiV3(self._base_api_mock)
        region = 'thhghe3'
        locale = 'asf'
        version = '4.grg22'
        tags = ['jyu5m', 'ijunds', 'mn4tgd']

        ret = static_data.runes(region, locale=locale, version=version, tags=tags)

        self._base_api_mock.request.assert_called_once_with(
            StaticDataApiV3.__name__,
            static_data.runes.__name__,
            region,
            '/lol/static-data/v3/runes',
            locale=locale,
            version=version,
            tags=tags
        )

        self.assertIs(self._expected_return, ret)

    def test_runes_default(self):
        static_data = StaticDataApiV3(self._base_api_mock)
        region = 'asfa331g1ggg'

        ret = static_data.runes(region)

        self._base_api_mock.request.assert_called_once_with(
            StaticDataApiV3.__name__,
            static_data.runes.__name__,
            region,
            '/lol/static-data/v3/runes',
            locale=None,
            version=None,
            tags=None
        )

        self.assertIs(self._expected_return, ret)

    def test_rune(self):
        static_data = StaticDataApiV3(self._base_api_mock)
        region = 'okmhgr'
        rune_id = 863387
        locale = '64n6gt'
        version = '4.erg'
        tags = ['rrrfdg', 'ks', 'gggfkmm']

        ret = static_data.rune(region, rune_id, locale=locale, version=version, tags=tags)

        self._base_api_mock.request.assert_called_once_with(
            StaticDataApiV3.__name__,
            static_data.rune.__name__,
            region,
            '/lol/static-data/v3/runes/{id}'.format(id=rune_id),
            locale=locale,
            version=version,
            tags=tags
        )

        self.assertIs(self._expected_return, ret)

    def test_rune_default(self):
        static_data = StaticDataApiV3(self._base_api_mock)
        region = 'jktfb'
        rune_id = 97332

        ret = static_data.rune(region, rune_id)

        self._base_api_mock.request.assert_called_once_with(
            StaticDataApiV3.__name__,
            static_data.rune.__name__,
            region,
            '/lol/static-data/v3/runes/{id}'.format(id=rune_id),
            locale=None,
            version=None,
            tags=None
        )

        self.assertIs(self._expected_return, ret)

    def test_summoner_spells(self):
        static_data = StaticDataApiV3(self._base_api_mock)
        region = 'thhghe3'
        locale = 'asf'
        version = '4.grg22'
        data_by_id = True
        tags = ['jyu5m', 'ijunds', 'mn4tgd']

        ret = static_data.summoner_spells(
            region,
            locale=locale,
            version=version,
            data_by_id=data_by_id,
            tags=tags
        )

        self._base_api_mock.request.assert_called_once_with(
            StaticDataApiV3.__name__,
            static_data.summoner_spells.__name__,
            region,
            '/lol/static-data/v3/summoner-spells',
            locale=locale,
            version=version,
            dataById=data_by_id,
            tags=tags
        )

        self.assertIs(self._expected_return, ret)

    def test_summoner_spells_default(self):
        static_data = StaticDataApiV3(self._base_api_mock)
        region = 'ukntrb'

        ret = static_data.summoner_spells(region)

        self._base_api_mock.request.assert_called_once_with(
            StaticDataApiV3.__name__,
            static_data.summoner_spells.__name__,
            region,
            '/lol/static-data/v3/summoner-spells',
            locale=None,
            version=None,
            dataById=None,
            tags=None
        )

        self.assertIs(self._expected_return, ret)

    def test_summoner_spell(self):
        static_data = StaticDataApiV3(self._base_api_mock)
        region = '87iujg'
        summoner_spell_id = 123
        locale = '64n6gt'
        version = '4.erg'
        tags = ['rrrfdg', 'ks', 'gggfkmm']

        ret = static_data.summoner_spell(
            region,
            summoner_spell_id,
            locale=locale,
            version=version,
            tags=tags
        )

        self._base_api_mock.request.assert_called_once_with(
            StaticDataApiV3.__name__,
            static_data.summoner_spell.__name__,
            region,
            '/lol/static-data/v3/summoner-spells/{id}'.format(id=summoner_spell_id),
            locale=locale,
            version=version,
            tags=tags
        )

        self.assertIs(self._expected_return, ret)

    def test_summoner_spell_default(self):
        static_data = StaticDataApiV3(self._base_api_mock)
        region = 'trgbr'
        summoner_spell_id = 875

        ret = static_data.summoner_spell(region, summoner_spell_id)

        self._base_api_mock.request.assert_called_once_with(
            StaticDataApiV3.__name__,
            static_data.summoner_spell.__name__,
            region,
            '/lol/static-data/v3/summoner-spells/{id}'.format(id=summoner_spell_id),
            locale=None,
            version=None,
            tags=None
        )

        self.assertIs(self._expected_return, ret)

    def test_versions(self):
        static_data = StaticDataApiV3(self._base_api_mock)
        region = 'ggdkmm70'

        ret = static_data.versions(region)

        self._base_api_mock.request.assert_called_once_with(
            StaticDataApiV3.__name__,
            static_data.versions.__name__,
            region,
            '/lol/static-data/v3/versions',
        )

        self.assertIs(self._expected_return, ret)
