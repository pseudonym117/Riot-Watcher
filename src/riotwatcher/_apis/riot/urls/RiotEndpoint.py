from ... import Endpoint, UrlConfig


class RiotEndpoint:
    def __init__(self, url: str, **kwargs):
        self._url = f"/riot{url}"

    def __call__(self, **kwargs):
        final_url = f"{UrlConfig.riot_url}{self._url}"

        endpoint = Endpoint(final_url, **kwargs)
        return endpoint(**kwargs)
