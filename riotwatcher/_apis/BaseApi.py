import re

import requests


class BaseApi:
    def __init__(self, api_key, request_handlers=None):
        self._api_key = api_key
        self._request_handlers = request_handlers

    @property
    def api_key(self):
        return self._api_key

    def request(self, endpoint_name, method_name, region, url_ext, **kwargs):
        url = 'https://{region}.api.riotgames.com{ext}'.format(region=region, ext=url_ext)

        query_params = {k: v for k, v in kwargs.items() if v is not None}

        response = None
        early_ret_idx = None

        if self._request_handlers is not None:
            for idx, handler in enumerate(self._request_handlers, start=1):
                response = handler.preview_request(
                    region,
                    endpoint_name,
                    method_name,
                    url,
                    query_params
                )
                early_ret_idx = idx
                if response is not None:
                    break

        if response is None:
            response = requests.get(
                url,
                params=query_params,
                headers={'X-Riot-Token': self.api_key}
            )

        if self._request_handlers is not None:
            for handler in self._request_handlers[early_ret_idx:None:-1]:
                mod = handler.after_request(region, endpoint_name, method_name, url, response)
                if mod is not None:
                    response = mod

        return response

    def request_static(self, version, locale, url_ext):
        url = 'https://ddragon.leagueoflegends.com/cdn/{version}/data/{loc}/{ext}.json'.format(version=version,
                                                                                              loc=locale, ext=url_ext)

        response = None
        early_ret_idx = None

        if self._request_handlers is not None:
            for idx, handler in enumerate(self._request_handlers, start=1):
                response = handler.preview_static_request(version, locale, url)
                early_ret_idx = idx
                if response is not None:
                    break

        if response is None:
            response = requests.get(url)

        if self._request_handlers is not None:
            for handler in self._request_handlers[early_ret_idx:None:-1]:
                mod = handler.after_static_request(version, locale, url, response)
                if mod is not None:
                    response = mod

        return response

    def request_version(self, region):
        region = re.sub(r'\d', '', region)
        url = 'https://ddragon.leagueoflegends.com/realms/{region}.json'.format(region=region)

        response = None
        early_ret_idx = None

        if self._request_handlers is not None:
            for idx, handler in enumerate(self._request_handlers, start=1):
                response = handler.preview_static_request(
                    '',
                    '',
                    url
                )
                early_ret_idx = idx
                if response is not None:
                    break

        if response is None:
            response = requests.get(url)

        if self._request_handlers is not None:
            for handler in self._request_handlers[early_ret_idx:None:-1]:
                mod = handler.after_static_request(
                    '',
                    '',
                    url,
                    response)
                if mod is not None:
                    response = mod

        return response
