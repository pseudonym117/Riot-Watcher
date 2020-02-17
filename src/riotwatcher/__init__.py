from .exceptions import ApiError, TimeoutError
from .LolWatcher import LolWatcher
from .TftWatcher import TftWatcher

from .RiotWatcher import RiotWatcher

__all__ = [
    "RiotWatcher",
    "LolWatcher",
    "TftWatcher",
    "Handlers",
    "ApiError",
    "TimeoutError",
]
