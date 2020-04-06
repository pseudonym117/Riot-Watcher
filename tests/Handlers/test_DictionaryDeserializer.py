import json

import pytest

from riotwatcher.Handlers import DictionaryDeserializer


@pytest.mark.unit
class TestDictionaryDeserializer:
    def test_basic_json(self):
        deserializer = DictionaryDeserializer()

        expected = {
            "test": {"object": "type", "int": 1},
            "bool": True,
            "list": ["string", "item"],
        }

        actual = deserializer.deserialize("", "", json.dumps(expected))

        assert expected == actual

    def test_empty_string(self):
        deserializer = DictionaryDeserializer()

        actual = deserializer.deserialize("", "", "")

        assert actual == {}
