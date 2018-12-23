import re

from .urls import DataDragonUrls


class DataDragonApi(object):
    def __init__(self, http_client):
        self._http_client = http_client

    async def champions(self, version, full=False, locale=None):
        return await self._request(
            DataDragonUrls.champions_full if full else DataDragonUrls.champions,
            version,
            locale,
        )

    async def items(self, version, locale=None):
        return await self._request(DataDragonUrls.items, version, locale)

    async def languages(self, version, locale=None):
        return await self._request(DataDragonUrls.languages, version, locale)

    async def maps(self, version, locale=None):
        return await self._request(DataDragonUrls.maps, version, locale)

    async def masteries(self, version, locale=None):
        return await self._request(DataDragonUrls.masteries, version, locale)

    async def profile_icons(self, version, locale=None):
        return await self._request(DataDragonUrls.profile_icons, version, locale)

    async def runes(self, version, locale=None):
        return await self._request(DataDragonUrls.runes, version, locale)

    async def runes_reforged(self, version, locale=None):
        return await self._request(DataDragonUrls.runes_reforged, version, locale)

    async def summoner_spells(self, version, locale=None):
        return await self._request(DataDragonUrls.summoner_spells, version, locale)

    async def versions_for_region(self, region):
        region = re.sub(r"\d", "", region)
        url, query = DataDragonUrls.versions(region=region)
        return await self._http_client._request_static(url, query)

    async def _request(self, endpoint, version, locale):
        url, query = endpoint(version=version, locale=locale if locale else "en_US")
        return await self._http_client._request_static(url, query)
