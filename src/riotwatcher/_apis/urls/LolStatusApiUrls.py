from .Endpoint import LeagueEndpoint


class LolStatusApiV3Urls(object):
    shard_data = LeagueEndpoint("/status/v3/shard-data")
