from ... import Endpoint, UrlConfig


class ValEndpoint:
    def __init__(self, url: str, **kwargs):
        self._url = f"/val{url}"

    def __call__(self, **kwargs):
        final_url = f"{UrlConfig.val_url}{self._url}"

        endpoint = Endpoint(final_url, **kwargs)
        return endpoint(**kwargs)
