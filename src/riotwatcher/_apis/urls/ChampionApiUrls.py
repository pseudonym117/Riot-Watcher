from .Endpoint import LeagueEndpoint


class ChampionApiV3Urls(object):
    rotations = LeagueEndpoint("/platform/v3/champion-rotations")
