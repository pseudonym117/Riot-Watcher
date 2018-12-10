import re

from .urls import DataDragonUrls


class DataDragonApi(object):
    def __init__(self, base_api):
        self._base_api = base_api

    def champions(self, version, full=False, locale=None):
        return self._request(
            DataDragonUrls.champions_full if full else DataDragonUrls.champions,
            version,
            locale,
        )

    def items(self, version, locale=None):
        return self._request(DataDragonUrls.items, version, locale)

    def languages(self, version, locale=None):
        return self._request(DataDragonUrls.languages, version, locale)

    def maps(self, version, locale=None):
        return self._request(DataDragonUrls.maps, version, locale)

    def masteries(self, version, locale=None):
        return self._request(DataDragonUrls.masteries, version, locale)

    def profile_icons(self, version, locale=None):
        return self._request(DataDragonUrls.profile_icons, version, locale)

    def runes(self, version, locale=None):
        return self._request(DataDragonUrls.runes, version, locale)

    def runes_reforged(self, version, locale=None):
        return self._request(DataDragonUrls.runes_reforged, version, locale)

    def summoner_spells(self, version, locale=None):
        return self._request(DataDragonUrls.summoner_spells, version, locale)

    def versions_for_region(self, region):
        region = re.sub(r"\d", "", region)
        url, query = DataDragonUrls.versions(region=region)
        return self._base_api.raw_request_static(url, query)

    def _request(self, endpoint, version, locale):
        url, query = endpoint(version=version, locale=locale if locale else "en_US")
        return self._base_api.raw_request_static(url, query)
