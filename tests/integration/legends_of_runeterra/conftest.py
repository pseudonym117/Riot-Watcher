import pytest


@pytest.fixture(params=["EUROPE", "ASIA", "AMERICAS"])
def region(request):
    return request.param
