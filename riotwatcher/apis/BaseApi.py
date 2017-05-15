
import requests


class BaseApi:
    def __init__(self, api_key, request_handlers=None):
        self._api_key = api_key
        self._request_handlers = request_handlers

    def add_request_handler(self, request_handler):
        if self._request_handlers is None:
            self._request_handlers = [request_handler]
        else:
            self._request_handlers.append(request_handler)

    @property
    def api_key(self):
        return self._api_key

    def request(self, region, url_ext, **kwargs):
        url = 'https://{region}.api.riotgames.com{ext}'.format(region=region, ext=url_ext)

        query_params = {k: v for k, v in kwargs.items() if v is not None}

        if self._request_handlers is not None:
            for handler in self._request_handlers:
                handler.preview_request(url, query_params)

        response = requests.get(url, params=query_params, headers={'X-Riot-Token': self.api_key})

        if self._request_handlers is not None:
            for handler in self._request_handlers:
                handler.after_request(url, response)

        return response.json()
