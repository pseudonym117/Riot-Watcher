
class StaticDataApiV3:
    def __init__(self, base_api):
        self._base_api = base_api

    def champions(
            self,
            region,
            champion_id=None,
            version=None,
            champ_list_data=None,
            champ_data=None,
            data_by_id=None,
            locale=None
    ):
        if champion_id is None:
            return self._base_api.request(
                region,
                '/lol/static-data/v3/champions',
                version=version,
                champListData=champ_list_data,
                dataById=data_by_id,
                locale=locale
            )
        else:
            return self._base_api.request(
                region,
                '/lol/static-data/v3/champions/{id}'.format(id=champion_id),
                version=version,
                locale=locale,
                champData=champ_data
            )

    def items(self, region, item_id=None, version=None, item_data=None, item_list_data=None, locale=None):
        if item_id is None:
            return self._base_api.request(
                region,
                '/lol/static-data/v3/items',
                version=version,
                itemListData=item_list_data,
                locale=locale
            )
        else:
            return self._base_api.request(
                region,
                '/lol/static-data/v3/items/{id}'.format(id=item_id),
                version=version,
                itemData=item_data,
                locale=locale
            )

    def language_strings(self, region, version=None, locale=None):
        return self._base_api.request(region, '/lol/static-data/v3/language-strings', version=version, locale=locale)

    def languages(self, region):
        return self._base_api.request(region, '/lol/static-data/v3/languages')

    def maps(self, region, version=None, locale=None):
        return self._base_api.request(region, '/lol/static-data/v3/maps', version=version, locale=locale)

    def masteries(self, region, mastery_id=None, version=None, mastery_data=None, mastery_list_data=None, locale=None):
        if mastery_id is None:
            return self._base_api.request(
                region,
                '/lol/static-data/v3/masteries',
                version=version,
                masteryListData=mastery_list_data,
                locale=locale
            )
        else:
            return self._base_api.request(
                region,
                '/lol/static-data/v3/masteries/{id}'.format(id=mastery_id),
                version=version,
                masteryData=mastery_data,
                locale=locale
            )

    def profile_icons(self, region, version=None, locale=None):
        return self._base_api.request(region, '/lol/static-data/v3/profile-icons', version=version, locale=locale)

    def realms(self, region):
        return self._base_api.request(region, '/lol/static-data/v3/realms')

    def runes(self, region, rune_id=None, version=None, rune_data=None, rune_list_data=None, locale=None):
        if rune_id is None:
            return self._base_api.request(
                region,
                '/lol/static-data/v3/runes',
                version=version,
                runeListData=rune_list_data,
                locale=locale
            )
        else:
            return self._base_api.request(
                region,
                '/lol/static-data/v3/runes/{id}'.format(id=rune_id),
                version=version,
                runeData=rune_data,
                locale=locale
            )

    def summoner_spells(
            self,
            region,
            summoner_spell_id=None,
            version=None,
            spell_data=None,
            spell_list_data=None,
            data_by_id=None,
            locale=None
    ):
        if summoner_spell_id is None:
            return self._base_api.request(
                region,
                '/lol/static-data/v3/summoner-spells',
                version=version,
                spellListData=spell_list_data,
                dataById=data_by_id,
                locale=locale
            )
        else:
            return self._base_api.request(
                region,
                '/lol/static-data/v3/summoner-spells/{id}'.format(id=summoner_spell_id),
                version=version,
                spellData=spell_data,
                locale=locale
            )

    def versions(self, region):
        return self._base_api.request(region, '/lol/static-data/v3/versions')
