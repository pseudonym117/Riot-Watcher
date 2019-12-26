import logging

log = logging.getLogger(__name__)

from riotwatcher.Handlers.RateLimit import RateLimitHandler


class WaitingRateLimitHandler(RateLimitHandler):
    def __init__(self):
        super(WaitingRateLimitHandler, self).__init__()
        log.warning(
            "class WaitingRateLimitHandler is deprecated! "
            + "please use riotwatcher.Handlers.RateLimit.RateLimitHandler."
        )
