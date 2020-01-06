from . import HeaderBasedLimiter


class MethodRateLimiter(HeaderBasedLimiter):
    def __init__(self):
        super().__init__("X-Method-Rate-Limit", "X-Method-Rate-Limit-Count", "Method")

    def _get_limit_scope(
        self, region: str, endpoint_name: str, method_name: str
    ) -> str:
        return f"{region}/{endpoint_name}/{method_name}"
