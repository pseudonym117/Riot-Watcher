class DataDragonApi:
    def __init__(self, base_api):
        self._base_api = base_api

    def champions(self, version, locale=None):
        return self._request(version, 'champion', locale)

    def _request(self, version, url_ext, locale='en_US'):
        return self._base_api.request_static(version, locale, url_ext)
