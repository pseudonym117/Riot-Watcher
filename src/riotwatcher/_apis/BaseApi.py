import aiohttp
import asyncio
import weakref


class BaseApi(object):
    def __init__(self, api_key, connector=None, loop=None,
                 early_handlers=[], late_handlers=[]):
        self.loop = asyncio.get_event_loop() if loop is None else loop
        self._api_key = api_key
        self._session = aiohttp.ClientSession(connector=connector, loop=self.loop)
        self._locks = weakref.WeakValueDictionary()

        self._early_handlers = early_handlers
        self._late_handlers = late_handlers

    @property
    def api_key(self):
        return self._api_key

    async def _request(self, endpoint_name, method_name, region, url, query_params):
        query_params = {k: v for k, v in query_params.items() if v is not None}
        resp = None

        if self._early_handlers:
            for handler in self._early_handlers:
                resp = await handler.before_request(
                    region, endpoint_name, method_name, url, query_params
                )
                if resp:
                    break

        if not resp:
            headers = {"X-Riot-Token": self.api_key}
            async with self._session.request('GET', url, params=query_params, headers=headers) as resp:
                if self._late_handlers:
                    for handler in self._late_handlers:
                        _resp = await handler.after_request(
                            region, endpoint_name, method_name, url, resp
                        )
                        if _resp is not None:
                            resp = _resp

        return resp

    async def _request_static(self, url, query_params):
        resp = None

        if self._early_handlers:
            for handler in self._early_handlers:
                resp = await handler.before_static_request(
                    url, query_params
                )
                if resp:
                    break

        if not resp:
            async with self._session.request('GET', url) as resp:
                if self._late_handlers:
                    for handler in self._late_handlers:
                        _resp = await handler.after_static_request(
                            url, resp
                        )
                        if _resp is not None:
                            resp = _resp

        return resp