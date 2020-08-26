import pytest


@pytest.mark.val
@pytest.mark.integration
class TestContentApi:
    def test_contents(self, val_context, region, locale):
        actual_response = val_context.watcher.content.contents(region, locale=locale)

        val_context.verify_api_call(
            region,
            "/val/content/v1/contents",
            {} if not locale else {"locale": locale},
            actual_response,
        )
