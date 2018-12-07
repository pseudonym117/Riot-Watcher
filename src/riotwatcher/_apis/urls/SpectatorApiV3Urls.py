from . import RegionEndpoint


class SpecatorEndpoint(RegionEndpoint):
    def __init__(self, url, **kwargs):
        nurl = "/spectator/v3" + url
        super(SpecatorEndpoint, self).__init__(nurl, **kwargs)


class SpectatorApiV3Urls(object):
    by_summoner = SpecatorEndpoint("/active-games/by-summoner/{summoner_id}")
    featured_games = SpecatorEndpoint("/featured-games")
