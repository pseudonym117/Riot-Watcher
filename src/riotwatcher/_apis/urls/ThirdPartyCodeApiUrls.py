from . import RegionEndpoint


class ThirdPartyCodeApiV3Urls(object):
    by_summoner = RegionEndpoint(
        "/platform/v3/third-party-code/by-summoner/{summoner_id}"
    )


class ThirdPartyCodeApiV4Urls(object):
    by_summoner = RegionEndpoint(
        "/platform/v4/third-party-code/by-summoner/{encrypted_summoner_id}"
    )
