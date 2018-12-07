from . import HeaderBasedLimiter


class ApplicationRateLimiter(HeaderBasedLimiter):
    def __init__(self):
        super(ApplicationRateLimiter, self).__init__(
            "X-App-Rate-Limit", "X-App-Rate-Limit-Count", "Application"
        )

    def _get_limit_scope(self, region, endpoint_name, method_name):
        return "{}".format(region)
