import pytest


@pytest.fixture(params=["EUROPE", "ASIA", "AMERICAS"])
def region(request):
    return request.param


@pytest.fixture(params=["pseudonym", "Tuxedo"])
def game_name(request):
    return request.param


@pytest.fixture(params=["sudo", "riot"])
def tag_line(request):
    return request.param


@pytest.fixture(params=["val", "lor"])
def game(request):
    return request.param


@pytest.mark.riot
@pytest.mark.integration
class TestAccountApi:
    def test_by_puuid(self, riot_context, region, puuid):
        actual_response = riot_context.watcher.account.by_puuid(region, puuid)

        riot_context.verify_api_call(
            region, f"/riot/account/v1/accounts/by-puuid/{puuid}", {}, actual_response
        )

    def test_by_riot_id(self, riot_context, region, game_name, tag_line):
        actual_response = riot_context.watcher.account.by_riot_id(
            region, game_name, tag_line
        )

        riot_context.verify_api_call(
            region,
            f"/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}",
            {},
            actual_response,
        )

    def test_active_shard(self, riot_context, region, game, puuid):
        actual_response = riot_context.watcher.account.active_shard(region, game, puuid)

        riot_context.verify_api_call(
            region,
            f"/riot/account/v1/active-shards/by-game/{game}/by-puuid/{puuid}",
            {},
            actual_response,
        )
