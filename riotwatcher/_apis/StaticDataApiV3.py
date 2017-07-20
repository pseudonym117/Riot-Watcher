
from . import NamedEndpoint


class StaticDataApiV3(NamedEndpoint):
    """
    This class wraps the Static-Data-v3 endpoint calls provided by the Riot API.
    See https://developer.riotgames.com/api-methods/#lol-static-data-v3 for more detailed information
    """

    def __init__(self, base_api):
        """
        Initialize a new StaticDataApiV3 which uses the provided base_api

        :param BaseApi base_api: the root API object to use for making all requests.
        """
        super(StaticDataApiV3, self).__init__(base_api, StaticDataApiV3.__name__)

    def champions(
            self,
            region,
            locale=None,
            version=None,
            tags=None,
            data_by_id=None
    ):
        """
        Retrieves champion list.
        Not all data is returned by default. See the tags parameter for more information.
        Requests to this API are not counted against the application Rate Limits.

        :param string region:   The region to execute this request on
        :param string locale:   Locale code for returned data (e.g., en_US, es_ES). If not specified, the default
                                locale for the region is used.
        :param string version:  Patch version for returned data. If not specified, the latest version for the region
                                is used. List of valid versions can be obtained from the versions method.
        :param Set[string] tags:Tags to return additional data. Only type, version, data, id, key, name, and title are
                                returned by default if this parameter isn't specified. To return all additional data,
                                use the tag 'all'.
        :param bool data_by_id: If specified as true, the returned data map will use the champions' IDs as the keys.
                                If not specified or specified as false, the returned data map will use the champions'
                                keys instead.

        :returns: ChampionListDto: This object contains champion list data.
        """
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
        """
        Retrieves champion by ID.
        Not all data is returned by default. See the tags parameter for more information.
        Requests to this API are not counted against the application Rate Limits.

        :param string region:   The region to execute this request on
        :param int champion_id: Champion ID
        :param string locale:   Locale code for returned data (e.g., en_US, es_ES). If not specified, the default locale
                                for the region is used.
        :param string version:  Patch version for returned data. If not specified, the latest version for the region is
                                used. List of valid versions can be obtained from the versions method.
        :param Set[string] tags:Tags to return additional data. Only id, key, name, and title are returned by default if
                                this parameter isn't specified. To return all additional data, use the tag 'all'.

        :returns: ChampionDto: This object contains champion data.
        """
        return self._request(
            self.champion.__name__,
            region,
            '/lol/static-data/v3/champions/{id}'.format(id=champion_id),
            version=version,
            locale=locale,
            tags=tags
        )

    def items(self, region, locale=None, version=None, tags=None):
        """
        Retrieves item list.
        Not all data is returned by default. See the tags parameter for more information.
        Requests to this API are not counted against the application Rate Limits.

        :param string region:   The region to execute this request on
        :param string locale:   Locale code for returned data (e.g., en_US, es_ES). If not specified, the default locale
                                for the region is used.
        :param string version:  Patch version for returned data. If not specified, the latest version for the region is
                                used. List of valid versions can be obtained from the versions method.
        :param Set[string] tags:Tags to return additional data. Only type, version, data, id, name, description,
                                plaintext, and group are returned by default if this parameter isn't specified. To
                                return all additional data, use the tag 'all'.

        :returns: ItemListDto: This object contains item list data.
        """
        return self._request(
            self.items.__name__,
            region,
            '/lol/static-data/v3/items',
            locale=locale,
            version=version,
            tags=tags
        )

    def item(self, region, item_id, locale=None, version=None, tags=None):
        """
        Retrieves item by ID.
        Not all data is returned by default. See the tags parameter for more information.
        Requests to this API are not counted against the application Rate Limits.

        :param string region:   The region to execute this request on
        :param int item_id:     Item ID
        :param string locale:   Locale code for returned data (e.g., en_US, es_ES). If not specified, the default locale
                                for the region is used.
        :param string version:  Patch version for returned data. If not specified, the latest version for the region is
                                used. List of valid versions can be obtained from the versions method.
        :param Set[string] tags:Tags to return additional data. Only type, version, data, id, name, description,
                                plaintext, and group are returned by default if this parameter isn't specified. To
                                return all additional data, use the tag 'all'.

        :returns: ItemDto: This object contains item data.
        """
        return self._request(
            self.item.__name__,
            region,
            '/lol/static-data/v3/items/{id}'.format(id=item_id),
            locale=locale,
            version=version,
            tags=tags,
        )

    def language_strings(self, region, version=None, locale=None):
        """
        Retrieve language strings data.
        Language strings data was not generated for patch version 7.4.2.
        Requests to this API are not counted against the application Rate Limits.

        :param string region:   The region to execute this request on
        :param string locale:   Locale code for returned data (e.g., en_US, es_ES). If not specified, the default locale
                                for the region is used.
        :param string version:  Patch version for returned data. If not specified, the latest version for the region is
                                used. List of valid versions can be obtained from the versions method.

        :returns: LanguageStringsDto: This object contains language strings data.
        """
        return self._request(
            self.language_strings.__name__,
            region,
            '/lol/static-data/v3/language-strings',
            version=version,
            locale=locale
        )

    def languages(self, region):
        """
        Retrieve supported languages data.
        Requests to this API are not counted against the application Rate Limits.

        :param string region:   The region to execute this request on

        :returns: List[string]:
        """
        return self._request(
            self.languages.__name__,
            region,
            '/lol/static-data/v3/languages'
        )

    def maps(self, region, locale=None, version=None):
        """
        Retrieve map data.
        This endpoint is only supported for patch version 5.5.3 and later.
        Also, map data was not generated for patch versions 5.15.1, 5.16.1, and 5.17.1.
        Requests to this API are not counted against the application Rate Limits.

        :param string region:   The region to execute this request on
        :param string locale:   Locale code for returned data (e.g., en_US, es_ES). If not specified, the default locale
                                for the region is used.
        :param string version:  Patch version for returned data. If not specified, the latest version for the region is
                                used. List of valid versions can be obtained from the versions method.

        :returns: MapDataDto: This object contains map data.
        """
        return self._request(
            self.maps.__name__,
            region,
            '/lol/static-data/v3/maps',
            locale=locale,
            version=version,
        )

    def masteries(self, region, locale=None, version=None, tags=None):
        """
        Retrieves mastery list.
        Not all data specified below is returned by default. See the tags parameter for more information.
        Requests to this API are not counted against the application Rate Limits.

        :param string region:   The region to execute this request on
        :param string locale:   Locale code for returned data (e.g., en_US, es_ES). If not specified, the default locale
                                for the region is used.
        :param string version:  Patch version for returned data. If not specified, the latest version for the region is
                                used. List of valid versions can be obtained from the versions method.
        :param Set[string] tags:Tags to return additional data. Only type, version, data, id, name, and description are
                                returned by default if this parameter isn't specified. To return all additional data,
                                use the tag 'all'.

        :returns: MasteryListDto: This object contains mastery list data.
        """
        return self._request(
            self.masteries.__name__,
            region,
            '/lol/static-data/v3/masteries',
            locale=locale,
            version=version,
            tags=tags
        )

    def mastery(self, region, mastery_id, locale=None, version=None, tags=None):
        """
        Retrieves mastery item by ID.
        Not all data specified below is returned by default. See the tags parameter for more information.
        Requests to this API are not counted against the application Rate Limits.

        :param string region:   The region to execute this request on
        :param int mastery_id:  Mastery ID
        :param string locale:   Locale code for returned data (e.g., en_US, es_ES). If not specified, the default locale
                                for the region is used.
        :param string version:  Patch version for returned data. If not specified, the latest version for the region is
                                used. List of valid versions can be obtained from the versions method.
        :param Set[string] tags:Tags to return additional data. Only id, name, and description are returned by default
                                if this parameter isn't specified. To return all additional data, use the tag 'all'.

        :returns: MasteryDto: This object contains mastery data.
        """
        return self._request(
            self.mastery.__name__,
            region,
            '/lol/static-data/v3/masteries/{id}'.format(id=mastery_id),
            locale=locale,
            version=version,
            tags=tags
        )

    def profile_icons(self, region, locale=None, version=None):
        """
        Retrieve profile icons.
        Requests to this API are not counted against the application Rate Limits.

        :param string region:   The region to execute this request on
        :param string locale:   Locale code for returned data (e.g., en_US, es_ES). If not specified, the default locale
                                for the region is used.
        :param string version:  Patch version for returned data. If not specified, the latest version for the region is
                                used. List of valid versions can be obtained from the versions method.

        :returns: ProfileIconDataDto: This object contains profile icon data.
        """
        return self._request(
            self.profile_icons.__name__,
            region,
            '/lol/static-data/v3/profile-icons',
            version=version,
            locale=locale
        )

    def realms(self, region):
        """
        Retrieve realm data.
        Requests to this API are not counted against the application Rate Limits.

        :param string region:   The region to execute this request on

        :returns: RealmDto: This object contains realm data.
        """
        return self._request(self.realms.__name__, region, '/lol/static-data/v3/realms')

    def runes(self, region, locale=None, version=None, tags=None):
        """
        Retrieves rune list.
        Not all data specified below is returned by default. See the tags parameter for more information.
        Requests to this API are not counted against the application Rate Limits.

        :param string region:   The region to execute this request on
        :param string locale:   Locale code for returned data (e.g., en_US, es_ES). If not specified, the default locale
                                for the region is used.
        :param string version:  Patch version for returned data. If not specified, the latest version for the region is
                                used. List of valid versions can be obtained from the versions method.
        :param Set[string] tags:Tags to return additional data. Only type, version, data, id, name, description, and
                                rune are returned by default if this parameter isn't specified. To return all additional
                                data, use the tag 'all'.

        :returns: RuneListDto: This object contains rune list data.
        """
        return self._request(
            self.runes.__name__,
            region,
            '/lol/static-data/v3/runes',
            locale=locale,
            version=version,
            tags=tags
        )

    def rune(self, region, rune_id, locale=None, version=None, tags=None):
        """
        Retrieves rune by ID.
        Not all data specified below is returned by default. See the tags parameter for more information.
        Requests to this API are not counted against the application Rate Limits.

        :param string region:   The region to execute this request on
        :param int rune_id:     Rune ID
        :param string locale:   Locale code for returned data (e.g., en_US, es_ES). If not specified, the default locale
                                for the region is used.
        :param string version:  Patch version for returned data. If not specified, the latest version for the region is
                                used. List of valid versions can be obtained from the versions method.
        :param Set[string] tags:Tags to return additional data. Only id, name, description, and rune are returned by
                                default if this parameter isn't specified. To return all additional data, use the
                                tag 'all'.

        :returns: RuneDto: This object contains rune data.
        """
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
        """
        Retrieves summoner spell list.
        Not all data specified below is returned by default. See the tags parameter for more information.
        Requests to this API are not counted against the application Rate Limits.

        :param string region:   The region to execute this request on
        :param string locale:   Locale code for returned data (e.g., en_US, es_ES). If not specified, the default locale
                                for the region is used.
        :param string version:  Patch version for returned data. If not specified, the latest version for the region is
                                used. List of valid versions can be obtained from the versions method.
        :param bool data_by_id: If specified as true, the returned data map will use the spells' IDs as the keys. If not
                                specified or specified as false, the returned data map will use the spells' keys instead
        :param Set[string] tags:Tags to return additional data. Only type, version, data, id, key, name, description,
                                and summonerLevel are returned by default if this parameter isn't specified. To return
                                all additional data, use the tag 'all'.

        :returns: SummonerSpellListDto: This object contains summoner spell list data.
        """
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
        """
        Retrieves summoner spell by ID.
        Not all data specified below is returned by default. See the tags parameter
        for more information.
        Requests to this API are not counted against the application Rate Limits.

        :param string region:           The region to execute this request on
        :param int summoner_spell_id:   Summoner spell ID
        :param string locale:           Locale code for returned data (e.g., en_US, es_ES). If not specified, the
                                        default locale for the region is used.
        :param string version:          Patch version for returned data. If not specified, the latest version for the
                                        region is used. List of valid versions can be obtained from the versions method.
        :param Set[string] tags:        Tags to return additional data. Only id, key, name, description, and
                                        summonerLevel are returned by default if this parameter isn't specified. To
                                        return all additional data, use the tag 'all'.

        :returns: SummonerSpellDto: This object contains summoner spell data.
        """
        return self._request(
            self.summoner_spell.__name__,
            region,
            '/lol/static-data/v3/summoner-spells/{id}'.format(id=summoner_spell_id),
            locale=locale,
            version=version,
            tags=tags
        )

    def versions(self, region):
        """
        Retrieve version data.
        Requests to this API are not counted against the application Rate Limits.

        :param string region:   The region to execute this request on

        :returns: List[string]:
        """
        return self._request(self.versions.__name__, region, '/lol/static-data/v3/versions')
