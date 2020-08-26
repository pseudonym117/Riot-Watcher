from .BaseApi import BaseApi
from .NamedEndpoint import NamedEndpoint

from .Endpoint import Endpoint
from .UrlConfig import UrlConfig

from . import (
    league_of_legends,
    legends_of_runeterra,
    riot,
    team_fight_tactics,
    valorant,
)

__all__ = [
    "BaseApi",
    "NamedEndpoint",
    "Endpoint",
    "UrlConfig",
    "league_of_legends",
    "legends_of_runeterra",
    "riot",
    "team_fight_tactics",
    "valorant",
]
