import re


class Endpoint(object):
    def __init__(self, url, **kwargs):
        self._url = url

        url_params = re.findall(r"{(\w*)}", self._url)

        if "" in url_params:
            raise ValueError("nameless format parameters not supported!")
        self._url_params = url_params
        self._query_params = kwargs.keys()

    def __call__(self, **kwargs):
        for req_param in self._url_params:
            if req_param not in kwargs:
                raise ValueError('parameter "{}" is required!'.format(req_param))

        query_params = {
            key: value for key, value in kwargs.items() if key in self._query_params
        }

        return (self._url.format(**kwargs), query_params)


class RegionEndpoint(Endpoint):
    def __init__(self, url, **kwargs):
        nurl = "https://{region}.api.riotgames.com/lol" + url
        super(RegionEndpoint, self).__init__(nurl, **kwargs)
