
from . import RequestHandler

class ConsoleLoggingHandler(RequestHandler):
    def __init__(self, log_start_message):
        super(ConsoleLoggingHandler, self).__init__()
        self._log_start_message = log_start_message

    def preview_request(self, url, query_params):
        print('{} - requesting url {}, query_params={}'.format(self._log_start_message, url, query_params))

    def after_request(self, url, response):
        print('{} - requested url {}, got response={}'.format(self._log_start_message, url, response))
