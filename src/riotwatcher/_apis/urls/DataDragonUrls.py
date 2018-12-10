from . import Endpoint


class DataDragonEndpoint(Endpoint):
    def __init__(self, url, **kwargs):
        nurl = "https://ddragon.leagueoflegends.com" + url
        super(DataDragonEndpoint, self).__init__(nurl, **kwargs)


class DDragonVersionLocaleEndpoint(DataDragonEndpoint):
    def __init__(self, url, **kwargs):
        nurl = "/cdn/{version}/data/{locale}" + url
        super(DDragonVersionLocaleEndpoint, self).__init__(nurl, **kwargs)


class DataDragonUrls(object):
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
