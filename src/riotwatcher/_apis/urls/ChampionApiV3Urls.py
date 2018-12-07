from . import RegionEndpoint


class ChampionEndpoint(RegionEndpoint):
    def __init__(self, url, **kwargs):
        nurl = "/platform/v3" + url
        super(ChampionEndpoint, self).__init__(nurl, **kwargs)


class ChampionApiV3Urls(object):
    rotations = ChampionEndpoint("/champion-rotations")
