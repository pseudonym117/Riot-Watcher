from . import HeaderBasedLimiter


class MethodRateLimiter(HeaderBasedLimiter):
    def __init__(self):
        super(MethodRateLimiter, self).__init__(
            "X-Method-Rate-Limit", "X-Method-Rate-Limit-Count", "Method"
        )

    def _get_limit_scope(self, region, endpoint_name, method_name):
        return "{}/{}/{}".format(region, endpoint_name, method_name)
