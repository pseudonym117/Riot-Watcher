import logging

from datetime import datetime

from . import RequestHandler


class DeprecationHandler(RequestHandler):
    def __init__(self):
        super(DeprecationHandler, self).__init__()
        self._warned = set()

    def after_request(self, region, endpoint_name, method_name, url, response):
        deprecation = response.headers.get("X-Riot-Deprecated")
        if deprecation is not None:
            try:
                deprecation = datetime.utcfromtimestamp(int(deprecation) // 1000)
            except (OSError, ValueError):
                # API returned unexected value in header, so just do nothing
                return response
            key = "{}.{}".format(endpoint_name, method_name)
            if key not in self._warned:
                # technically race condition here, but worst case is we double log a warning
                self._warned.add(key)
                logging.warning(
                    "Method %s has been deprecated by Riot! It will no longer work after %s",
                    key,
                    deprecation,
                )
        return response
