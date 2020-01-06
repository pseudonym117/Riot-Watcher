from .Endpoint import RegionEndpoint


class ThirdPartyCodeApiV4Urls:
    by_summoner = RegionEndpoint(
        "/platform/v4/third-party-code/by-summoner/{encrypted_summoner_id}"
    )
