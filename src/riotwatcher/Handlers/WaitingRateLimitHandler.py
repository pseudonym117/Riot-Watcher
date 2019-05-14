import logging

from riotwatcher.Handlers.RateLimit import RateLimitHandler


class WaitingRateLimitHandler(RateLimitHandler):
    def __init__(self):
        super(WaitingRateLimitHandler, self).__init__()
        logging.warning(
            "class WaitingRateLimitHandler is deprecated! "
            + "please use riotwatcher.Handlers.RateLimit.RateLimitHandler."
        )
