import json

from ..Deserializer import Deserializer


class DictionaryDeserializer(Deserializer):
    def deserialize(self, endpoint_name: str, method_name: str, data: str,) -> dict:
        return json.loads(data)
