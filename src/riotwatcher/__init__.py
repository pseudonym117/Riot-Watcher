from .exceptions import ApiError, TimeoutError
from .LolWatcher import LolWatcher
from .TftWatcher import TftWatcher

from .riotwatcher import RiotWatcher

__all__ = [
    "LolWatcher",
    "TftWatcher",
    "RiotWatcher",
    "Handlers",
    "ApiError",
    "TimeoutError",
]
