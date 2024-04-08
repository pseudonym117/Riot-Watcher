from .LeagueEndpoint import LeagueEndpoint


class SpecatorV5Endpoint(LeagueEndpoint):
    def __init__(self, url, **kwargs):
        nurl = f"/spectator/v5{url}"
        super().__init__(nurl, **kwargs)


class SpectatorApiV5Urls:
    by_summoner = SpecatorV5Endpoint(
        "/active-games/by-summoner/{encrypted_puuid}"
    )
    featured_games = SpecatorV5Endpoint("/featured-games")
