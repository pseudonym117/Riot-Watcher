import logging

from .LolWatcher import LolWatcher

log = logging.getLogger(__name__)


class RiotWatcher(LolWatcher):
    def __init__(self, *args, **kwargs):
        log.warning(
            "DEPRECATION: RiotWatcher class has been renamed to LolWatcher. Please use LolWatcher."
        )
        super().__init__(*args, **kwargs)
