from . import HeaderBasedLimiter


class ApplicationRateLimiter(HeaderBasedLimiter):
    def __init__(self):
        super().__init__("X-App-Rate-Limit", "X-App-Rate-Limit-Count", "Application")

    def _get_limit_scope(
        self, region: str, endpoint_name: str, method_name: str
    ) -> str:
        return f"{region}"
