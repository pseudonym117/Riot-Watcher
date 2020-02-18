from ... import Endpoint, UrlConfig


class LorEndpoint:
    def __init__(self, url: str, **kwargs):
        self._url = f"/lor{url}"

    def __call__(self, **kwargs):
        final_url = f"{UrlConfig.lor_url}{self._url}"

        endpoint = Endpoint(final_url, **kwargs)
        return endpoint(**kwargs)
