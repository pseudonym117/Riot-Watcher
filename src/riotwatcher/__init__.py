from .exceptions import ApiError, TimeoutError
from .LolWatcher import LolWatcher
from .LorWatcher import LorWatcher
from .TftWatcher import TftWatcher

from .riotwatcher import RiotWatcher

__all__ = [
    "LolWatcher",
    "LorWatcher",
    "TftWatcher",
    "RiotWatcher",
    "Handlers",
    "ApiError",
    "TimeoutError",
]
