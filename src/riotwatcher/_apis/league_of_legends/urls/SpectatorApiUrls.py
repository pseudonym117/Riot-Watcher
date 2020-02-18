from .LeagueEndpoint import LeagueEndpoint


class SpecatorV4Endpoint(LeagueEndpoint):
    def __init__(self, url, **kwargs):
        nurl = f"/spectator/v4{url}"
        super().__init__(nurl, **kwargs)


class SpectatorApiV4Urls:
    by_summoner = SpecatorV4Endpoint(
        "/active-games/by-summoner/{encrypted_summoner_id}"
    )
    featured_games = SpecatorV4Endpoint("/featured-games")
