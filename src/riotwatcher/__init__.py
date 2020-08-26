from .__version__ import __author__, __title__, __version__

from .exceptions import ApiError, TimeoutError
from .Deserializer import Deserializer
from .RateLimiter import RateLimiter
from .LolWatcher import LolWatcher
from .LorWatcher import LorWatcher
from .TftWatcher import TftWatcher
from .ValWatcher import ValWatcher

from .riotwatcher import RiotWatcher

__all__ = [
    "Deserializer",
    "RateLimiter",
    "LolWatcher",
    "LorWatcher",
    "TftWatcher",
    "RiotWatcher",
    "ValWatcher",
    "Handlers",
    "ApiError",
    "TimeoutError",
]
