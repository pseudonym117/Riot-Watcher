from . import RegionEndpoint


class ThirdPartyCodeEndpoint(RegionEndpoint):
    def __init__(self, url, **kwargs):
        nurl = "/platform/v3/third-party-code" + url
        super(ThirdPartyCodeEndpoint, self).__init__(nurl, **kwargs)


class ThirdPartyCodeApiV3Urls(object):
    by_summoner = ThirdPartyCodeEndpoint("/by-summoner/{summoner_id}")
