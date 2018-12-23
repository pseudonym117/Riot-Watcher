from . import HeaderBasedRateLimiter


class MethodRateLimiter(HeaderBasedRateLimiter):
    def __init__(self, loop=None):
        super().__init__("X-Method-Rate-Limit", "X-Method-Rate-Limit-Count", "Method", loop=loop)

    def _get_limit_scope(self, region, endpoint_name, method_name):
        return "{}:{}:{}".format(region, endpoint_name, method_name)