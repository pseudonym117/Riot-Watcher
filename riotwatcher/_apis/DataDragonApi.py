class DataDragonApi:
    # TODO support the NamedEndpoint?

    def __init__(self, base_api):
        self._base_api = base_api

    def champions(self, version, full=False, locale=None):
        url_ext = 'champion'

        if full:
            url_ext = 'championFull'

        return self._request(version, url_ext, locale)

    def items(self, version, locale=None):
        url_ext = 'item'

        return self._request(version, url_ext, locale)

    def languages(self, version, locale=None):
        url_ext = 'language'

        return self._request(version, url_ext, locale)

    def maps(self, version, locale=None):
        url_ext = 'map'

        return self._request(version, url_ext, locale)

    def masteries(self, version, locale=None):
        url_ext = 'mastery'

        return self._request(version, url_ext, locale)

    def profile_icons(self, version, locale=None):
        url_ext = 'profileicon'

        return self._request(version, url_ext, locale)

    def runes(self, version, locale=None):
        url_ext = 'rune'

        return self._request(version, url_ext, locale)

    def summoner_spells(self, version, locale=None):
        url_ext = 'summoner'

        return self._request(version, url_ext, locale)

    def versions_for_region(self, region):
        return self._base_api.request_version(region)

    def _request(self, version, url_ext, locale):
        if locale is None:
            locale = 'en_US'

        return self._base_api.request_static(version, locale, url_ext)
