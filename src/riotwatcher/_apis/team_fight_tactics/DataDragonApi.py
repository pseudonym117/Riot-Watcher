import re

from .. import BaseApi, Endpoint
from .urls import DataDragonUrls


class DataDragonApi:
    def __init__(self, base_api: BaseApi):
        self._base_api = base_api

    def arenas(self, version: str, locale: str = None):
        return self._request(DataDragonUrls.arenas, version, locale)

    def augments(self, version: str, locale: str = None):
        return self._request(DataDragonUrls.augments, version, locale)

    def champions(self, version: str, locale: str = None):
        return self._request(DataDragonUrls.champions, version, locale)

    def items(self, version: str, locale: str = None):
        return self._request(DataDragonUrls.items, version, locale)

    def queues(self, version: str, locale: str = None):
        return self._request(DataDragonUrls.queues, version, locale)

    def regalia(self, version: str, locale: str = None):
        return self._request(DataDragonUrls.regalia, version, locale)

    def tacticians(self, version: str, locale: str = None):
        return self._request(DataDragonUrls.tacticians, version, locale)

    def traits(self, version: str, locale: str = None):
        return self._request(DataDragonUrls.traits, version, locale)

    def versions_for_region(self, region: str):
        region = re.sub(r"\d", "", region)
        url, query = DataDragonUrls.versions(region=region)
        return self._base_api.raw_request_static(url, query)

    def versions_all(self):
        url, query = DataDragonUrls.versions_all()
        return self._base_api.raw_request_static(url, query)

    def _request(self, endpoint: Endpoint, version: str, locale: str):
        url, query = endpoint(version=version, locale=locale if locale else "en_US")
        return self._base_api.raw_request_static(url, query)
