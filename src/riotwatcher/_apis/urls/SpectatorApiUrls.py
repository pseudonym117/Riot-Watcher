from .Endpoint import LeagueEndpoint


class SpecatorV4Endpoint(LeagueEndpoint):
    def __init__(self, url, **kwargs):
        nurl = "/spectator/v4" + url
        super(SpecatorV4Endpoint, self).__init__(nurl, **kwargs)


class SpectatorApiV4Urls(object):
    by_summoner = SpecatorV4Endpoint(
        "/active-games/by-summoner/{encrypted_summoner_id}"
    )
    featured_games = SpecatorV4Endpoint("/featured-games")
