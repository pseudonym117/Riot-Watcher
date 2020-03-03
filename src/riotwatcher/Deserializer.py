import abc

from typing import Any


class Deserializer(abc.ABC):
    @abc.abstractmethod
    def deserialize(self, endpoint_name: str, method_name: str, data: str) -> Any:
        pass
