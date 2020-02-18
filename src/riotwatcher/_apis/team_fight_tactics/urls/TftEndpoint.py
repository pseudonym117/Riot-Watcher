from ... import Endpoint, UrlConfig


class TftEndpoint:
    def __init__(self, url: str, **kwargs):
        self._url = f"/tft{url}"

    def __call__(self, **kwargs):
        final_url = f"{UrlConfig.tft_url}{self._url}"

        endpoint = Endpoint(final_url, **kwargs)
        return endpoint(**kwargs)
