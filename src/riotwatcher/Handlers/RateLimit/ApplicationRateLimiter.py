from . import HeaderBasedRateLimiter


class ApplicationRateLimiter(HeaderBasedRateLimiter):
    def __init__(self, loop=None):
        super().__init__("X-App-Rate-Limit", "X-App-Rate-Limit-Count", "Application", loop=loop)

    def _get_limit_scope(self, region, endpoint_name, method_name):
        return "{}".format(region)