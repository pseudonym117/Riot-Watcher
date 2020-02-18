from .LeagueEndpoint import LeagueEndpoint


class ThirdPartyCodeApiV4Urls:
    by_summoner = LeagueEndpoint(
        "/platform/v4/third-party-code/by-summoner/{encrypted_summoner_id}"
    )
