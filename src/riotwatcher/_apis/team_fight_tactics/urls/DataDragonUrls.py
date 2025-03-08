from ... import Endpoint


class DataDragonEndpoint(Endpoint):
    def __init__(self, url, **kwargs):
        nurl = f"https://ddragon.leagueoflegends.com{url}"
        super().__init__(nurl, **kwargs)


class DDragonVersionLocaleEndpoint(DataDragonEndpoint):
    def __init__(self, url, **kwargs):
        nurl = f"/cdn/{{version}}/data/{{locale}}{url}"
        super().__init__(nurl, **kwargs)


class DataDragonUrls:
    arenas = DDragonVersionLocaleEndpoint("/tft-arena.json")
    augments = DDragonVersionLocaleEndpoint("/tft-augments.json")
    champions = DDragonVersionLocaleEndpoint("/tft-champion.json")
    items = DDragonVersionLocaleEndpoint("/tft-item.json")
    queues = DDragonVersionLocaleEndpoint("/tft-queues.json")
    regalia = DDragonVersionLocaleEndpoint("/tft-regalia.json")
    tacticians = DDragonVersionLocaleEndpoint("/tft-tactician.json")
    traits = DDragonVersionLocaleEndpoint("/tft-trait.json")
    versions = DataDragonEndpoint("/realms/{region}.json")
    versions_all = DataDragonEndpoint("/api/versions.json")
