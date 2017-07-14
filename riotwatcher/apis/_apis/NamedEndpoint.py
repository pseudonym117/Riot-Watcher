
class NamedEndpoint:
    def __init__(self, base_api, endpoint_name):
        self._base_api = base_api
        self._endpoint_name = endpoint_name

    def _request(self, method_name, region, url_ext, **kwargs):
        return self._base_api.request(self._endpoint_name, method_name, region, url_ext, **kwargs)
