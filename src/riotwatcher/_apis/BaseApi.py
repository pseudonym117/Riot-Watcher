from requests import session


class BaseApi:
    def __init__(self, api_key, request_handlers=None, timeout=None):
        self._api_key = api_key
        self._request_handlers = request_handlers
        self._timeout = timeout
        self._session = session()

    @property
    def api_key(self):
        return self._api_key

    def raw_request(
        self,
        endpoint_name: str,
        method_name: str,
        region: str,
        url: str,
        query_params: dict,
    ):
        query_params = {k: v for k, v in query_params.items() if v is not None}

        response = None
        early_ret_idx = None

        if self._request_handlers is not None:
            for idx, handler in enumerate(self._request_handlers, start=1):
                response = handler.preview_request(
                    region, endpoint_name, method_name, url, query_params
                )
                early_ret_idx = idx
                if response is not None:
                    break

        if response is None:
            extra = {}
            if self._timeout is not None:
                extra["timeout"] = self._timeout

            response = self._session.get(
                url,
                params=query_params,
                headers={"X-Riot-Token": self.api_key},
                **extra
            )

        if self._request_handlers is not None:
            for handler in self._request_handlers[early_ret_idx:None:-1]:
                mod = handler.after_request(
                    region, endpoint_name, method_name, url, response
                )
                if mod is not None:
                    response = mod

        return response

    def raw_request_static(self, url, query_params):
        query_params = {k: v for k, v in query_params.items() if v is not None}

        response = None
        early_ret_idx = None

        if self._request_handlers is not None:
            for idx, handler in enumerate(self._request_handlers, start=1):
                response = handler.preview_static_request(url, query_params)
                early_ret_idx = idx
                if response is not None:
                    break

        if response is None:
            extra = {}
            if self._timeout is not None:
                extra["timeout"] = self._timeout

            response = self._session.get(url, params=query_params, **extra)

        if self._request_handlers is not None:
            for handler in self._request_handlers[early_ret_idx:None:-1]:
                mod = handler.after_static_request(url, response)
                if mod is not None:
                    response = mod

        return response
