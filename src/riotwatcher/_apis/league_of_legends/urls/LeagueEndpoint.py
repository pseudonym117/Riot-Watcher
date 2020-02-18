from ... import Endpoint, UrlConfig


class LeagueEndpoint:
    def __init__(self, url: str, **kwargs):
        self._url = f"/lol{url}"

    def __call__(self, **kwargs):
        final_url = f"{UrlConfig.root_url}{self._url}"

        endpoint = Endpoint(final_url, **kwargs)
        return endpoint(**kwargs)
