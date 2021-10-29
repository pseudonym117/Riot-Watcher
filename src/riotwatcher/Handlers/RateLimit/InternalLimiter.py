import abc
import datetime

from typing import Dict


class InternalLimiter(abc.ABC):
    @abc.abstractmethod
    def wait_until(
        self, region: str, endpoint_name: str, method_name: str
    ) -> datetime.datetime:
        pass

    @abc.abstractmethod
    def update_limiter(
        self,
        region: str,
        endpoint_name: str,
        method_name: str,
        status: int,
        headers: Dict[str, str],
    ):
        pass
