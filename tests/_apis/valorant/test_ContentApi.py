from unittest.mock import MagicMock

import pytest

from riotwatcher._apis.valorant import ContentApi


@pytest.mark.unit
@pytest.mark.val
class TestContentApi:
    def test_contents(self, region, locale):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        content = ContentApi(mock_base_api)

        ret = content.contents(region, locale)

        mock_base_api.raw_request.assert_called_once_with(
            ContentApi.__name__,
            content.contents.__name__,
            region,
            f"https://{region}.api.riotgames.com/val/content/v1/contents",
            {"locale": locale},
        )

        assert ret == expected_return
