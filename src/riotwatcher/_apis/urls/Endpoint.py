import re

from .UrlConfig import UrlConfig


class Endpoint(object):
    def __init__(self, url, **kwargs):
        self._url = url

        url_params = re.findall(r"{(\w*)}", self._url)

        if "" in url_params:
            raise ValueError("nameless format parameters not supported!")
        self._url_params = url_params
        self._query_params = [key for key in kwargs.keys() if key not in url_params]

    def __call__(self, **kwargs):
        for req_param in self._url_params:
            if req_param not in kwargs:
                raise ValueError('parameter "{}" is required!'.format(req_param))

        query_params = {
            key: value for key, value in kwargs.items() if key in self._query_params
        }

        return (self._url.format(**kwargs), query_params)


class RegionEndpoint(object):
    def __init__(self, url, **kwargs):
        self._url = "/lol" + url

    def __call__(self, **kwargs):
        final_url = UrlConfig.root_url + self._url

        endpoint = Endpoint(final_url, **kwargs)
        return endpoint(**kwargs)
