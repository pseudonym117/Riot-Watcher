import logging
from datetime import datetime

from requests import Response

from . import RequestHandler

LOG = logging.getLogger(__name__)


class DeprecationHandler(RequestHandler):
    def __init__(self):
        super().__init__()
        self._warned = set()

    def after_request(
        self,
        region: str,
        endpoint_name: str,
        method_name: str,
        url: str,
        response: Response,
    ) -> Response:
        deprecation = response.headers.get("X-Riot-Deprecated")
        if deprecation is not None:
            try:
                deprecation = datetime.utcfromtimestamp(int(deprecation) // 1000)
            except (OSError, ValueError):
                # API returned unexected value in header, so just do nothing
                return response
            key = f"{endpoint_name}.{method_name}"
            if key not in self._warned:
                # technically race condition here, but worst case is we double log
                self._warned.add(key)
                LOG.warning(
                    " ".join(
                        [
                            "Method %s has been deprecated by Riot!",
                            "It will no longer work after %s",
                        ]
                    ),
                    key,
                    deprecation,
                )
        return response
