import pytest


@pytest.fixture(params=["test-region"])
def region(request):
    return request.param


@pytest.fixture(params=["enc-puuid-val"])
def puuid(request):
    return request.param


@pytest.fixture(params=[None, "en-US"])
def locale(request):
    return request.param
