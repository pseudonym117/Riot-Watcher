from .RiotEndpoint import RiotEndpoint


class AccountEndpoint(RiotEndpoint):
    def __init__(self, url: str, **kwargs):
        super().__init__(f"/account/v1{url}", **kwargs)


class AccountApiUrls:
    by_puuid = AccountEndpoint("/accounts/by-puuid/{puuid}")
    by_riot_id = AccountEndpoint("/accounts/by-riot-id/{game_name}/{tag_line}")
    active_shard = AccountEndpoint("/active-shards/by-game/{game}/by-puuid/{puuid}")
