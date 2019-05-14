from . import RequestHandler


class JsonifyHandler(RequestHandler):
    async def after_request(self, region, endpoint_name, method_name, url, response):
        return await response.json()

    async def after_static_request(self, url, response):
        return await response.json()
