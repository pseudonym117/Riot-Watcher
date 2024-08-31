from ...league_of_legends.urls.DataDragonUrls import DataDragonEndpoint, DDragonVersionLocaleEndpoint


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