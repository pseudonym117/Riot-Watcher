import abc
import datetime

from typing import Dict, Optional


class RateLimiter(abc.ABC):
    @abc.abstractmethod
    def wait_until(
        self, region: str, endpoint_name: str, method_name: str
    ) -> Optional[datetime.datetime]:
        pass

    @abc.abstractmethod
    def record_response(
        self,
        region: str,
        endpoint_name: str,
        method_name: str,
        status: int,
        headers: Dict[str, str],
    ):
        pass
