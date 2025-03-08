from .LeagueEndpoint import LeagueEndpoint


class LeagueV4Endpoint(LeagueEndpoint):
    def __init__(self, url, **kwargs):
        nurl = f"/league/v4{url}"
        super().__init__(nurl, **kwargs)


class LeagueApiV4Urls:
    challenger_by_queue = LeagueV4Endpoint("/challengerleagues/by-queue/{queue}")
    grandmaster_by_queue = LeagueV4Endpoint("/grandmasterleagues/by-queue/{queue}")
    by_id = LeagueV4Endpoint("/leagues/{league_id}")
    master_by_queue = LeagueV4Endpoint("/masterleagues/by-queue/{queue}")
    by_summoner = LeagueV4Endpoint("/entries/by-summoner/{encrypted_summoner_id}")
    by_puuid = LeagueV4Endpoint("/entries/by-puuid/{puuid}")
    entries = LeagueV4Endpoint("/entries/{queue}/{tier}/{division}", page=int)
