class DataDragonApi:
    # TODO support the NamedEndpoint?

    def __init__(self, base_api):
        self._base_api = base_api

    def champions(self, version, full=False, locale=None):
        url_ext = 'champion'

        if full:
            url_ext = 'championFull'

        return self._request(version, url_ext, locale)

    def _request(self, version, url_ext, locale):
        if locale is None:
            locale = 'en_US'

        return self._base_api.request_static(version, locale, url_ext)
