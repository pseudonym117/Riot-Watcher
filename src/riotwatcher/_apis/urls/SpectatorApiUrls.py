from .Endpoint import RegionEndpoint


class SpecatorV4Endpoint(RegionEndpoint):
    def __init__(self, url, **kwargs):
        nurl = "/spectator/v4" + url
        super(SpecatorV4Endpoint, self).__init__(nurl, **kwargs)


class SpectatorApiV4Urls(object):
    by_summoner = SpecatorV4Endpoint(
        "/active-games/by-summoner/{encrypted_summoner_id}"
    )
    featured_games = SpecatorV4Endpoint("/featured-games")
