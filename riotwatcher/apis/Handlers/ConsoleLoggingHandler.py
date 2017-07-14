
from . import RequestHandler

class ConsoleLoggingHandler(RequestHandler):
    def __init__(self, log_start_message):
        super(ConsoleLoggingHandler, self).__init__()
        self._log_start_message = log_start_message

    def preview_request(self, endpoint_name, method_name, url, query_params):
        print(
            '{} - requesting endpoint {}, method {}, url {}, query_params={}'.format(
                self._log_start_message,
                endpoint_name,
                method_name,
                url,
                query_params
            )
        )

    def after_request(self, endpoint_name, method_name, url, response):
        print(
            '{} - requesting endpoint {}, method {}, url {}, query_params={}'.format(
                self._log_start_message,
                endpoint_name,
                method_name,
                url,
                response
            )
        )
