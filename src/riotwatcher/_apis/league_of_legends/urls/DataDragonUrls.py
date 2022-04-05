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
    champions = DDragonVersionLocaleEndpoint("/champion.json")
    champions_full = DDragonVersionLocaleEndpoint("/championFull.json")
    items = DDragonVersionLocaleEndpoint("/item.json")
    languages = DDragonVersionLocaleEndpoint("/language.json")
    maps = DDragonVersionLocaleEndpoint("/map.json")
    masteries = DDragonVersionLocaleEndpoint("/mastery.json")
    profile_icons = DDragonVersionLocaleEndpoint("/profileicon.json")
    runes = DDragonVersionLocaleEndpoint("/rune.json")
    runes_reforged = DDragonVersionLocaleEndpoint("/runesReforged.json")
    summoner_spells = DDragonVersionLocaleEndpoint("/summoner.json")
    versions = DataDragonEndpoint("/realms/{region}.json")
    versions_all = DataDragonEndpoint("/api/versions.json")
