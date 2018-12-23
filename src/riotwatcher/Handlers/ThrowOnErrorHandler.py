from . import RequestHandler


class ThrowOnErrorHandler(RequestHandler):
    async def after_request(self, region, endpoint_name, method_name, url, response):
        response.raise_for_status()

    async def after_static_request(self, url, response):
        response.raise_for_status()
