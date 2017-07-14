
from . import NamedEndpoint


class StaticDataApiV3(NamedEndpoint):
    def __init__(self, base_api):
        super(StaticDataApiV3, self).__init__(base_api, StaticDataApiV3.__name__)

    def champions(
            self,
            region,
            locale=None,
            version=None,
            tags=None,
            data_by_id=None
    ):
        return self._request(
            self.champions.__name__,
            region,
            '/lol/static-data/v3/champions',
            locale=locale,
            version=version,
            tags=tags,
            dataById=data_by_id
        )

    def champion(
            self,
            region,
            champion_id,
            version=None,
            tags=None,
            locale=None
    ):
        return self._request(
            self.champion.__name__,
            region,
            '/lol/static-data/v3/champions/{id}'.format(id=champion_id),
            version=version,
            locale=locale,
            tags=tags
        )

    def items(self, region, locale=None, version=None, tags=None):
        return self._request(
            self.items.__name__,
            region,
            '/lol/static-data/v3/items',
            locale=locale,
            version=version,
            tags=tags
        )

    def item(self, region, item_id, locale=None, version=None, tags=None):
        return self._request(
            self.item.__name__,
            region,
            '/lol/static-data/v3/items/{id}'.format(id=item_id),
            locale=locale,
            version=version,
            tags=tags,
        )

    def language_strings(self, region, version=None, locale=None):
        return self._request(
            self.language_strings.__name__,
            region,
            '/lol/static-data/v3/language-strings',
            version=version,
            locale=locale
        )

    def languages(self, region):
        return self._request(
            self.languages.__name__,
            region,
            '/lol/static-data/v3/languages'
        )

    def maps(self, region, locale=None, version=None):
        return self._request(
            self.maps.__name__,
            region,
            '/lol/static-data/v3/maps',
            locale=locale,
            version=version,
        )

    def masteries(self, region, locale=None, version=None, tags=None):
        return self._request(
            self.masteries.__name__,
            region,
            '/lol/static-data/v3/masteries',
            locale=locale,
            version=version,
            tags=tags
        )

    def mastery(self, region, mastery_id, locale=None, version=None, tags=None):
        return self._request(
            self.mastery.__name__,
            region,
            '/lol/static-data/v3/masteries/{id}'.format(id=mastery_id),
            locale=locale,
            version=version,
            tags=tags
        )

    def profile_icons(self, region, locale=None, version=None):
        return self._request(
            self.profile_icons.__name__,
            region,
            '/lol/static-data/v3/profile-icons',
            version=version,
            locale=locale
        )

    def realms(self, region):
        return self._request(self.realms.__name__, region, '/lol/static-data/v3/realms')

    def runes(self, region, locale=None, version=None, tags=None):
        return self._request(
            self.runes.__name__,
            region,
            '/lol/static-data/v3/runes',
            locale=locale,
            version=version,
            tags=tags
        )

    def rune(self, region, rune_id, locale=None, version=None, tags=None):
        return self._request(
            self.rune.__name__,
            region,
            '/lol/static-data/v3/runes/{id}'.format(id=rune_id),
            locale=locale,
            version=version,
            tags=tags
        )

    def summoner_spells(
            self,
            region,
            locale=None,
            version=None,
            data_by_id=None,
            tags=None,
    ):
        return self._request(
            self.summoner_spells.__name__,
            region,
            '/lol/static-data/v3/summoner-spells',
            locale=locale,
            version=version,
            tags=tags,
            dataById=data_by_id
        )

    def summoner_spell(self, region, summoner_spell_id, locale=None, version=None, tags=None):
        return self._request(
            self.summoner_spell.__name__,
            region,
            '/lol/static-data/v3/summoner-spells/{id}'.format(id=summoner_spell_id),
            locale=locale,
            version=version,
            tags=tags
        )

    def versions(self, region):
        return self._request(self.versions.__name__, region, '/lol/static-data/v3/versions')
