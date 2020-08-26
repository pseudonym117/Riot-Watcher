import pytest


@pytest.fixture(params=["12345", "99999999999999999999"])
def puuid(request):
    return request.param
