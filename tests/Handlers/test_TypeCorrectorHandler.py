import pytest

from riotwatcher.Handlers import TypeCorrectorHandler


@pytest.mark.common
@pytest.mark.unit
class TestTypeCorrectorHandler:
    def test_bool_remapped_to_string(self):
        corrector = TypeCorrectorHandler()

        query_params = {
            "a": "test",
            "b": 123,
            "c": True,
            "d": False,
            "e": ["first", "test"],
            "f": [123, 456],
            "g": [True, False],
            "h": ["hard", 2, True, False],
        }

        corrector.preview_request(None, None, None, None, query_params)

        assert "test" == query_params["a"]
        assert 123 == query_params["b"]
        assert "true" == query_params["c"]
        assert "false" == query_params["d"]
        assert ["first", "test"] == query_params["e"]
        assert [123, 456] == query_params["f"]
        assert ["true", "false"] == query_params["g"]
        assert ["hard", 2, "true", "false"] == query_params["h"]
