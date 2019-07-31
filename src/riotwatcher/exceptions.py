import requests

from .Handlers import ApiError as _ApiError

ApiError = _ApiError  # should silence code analysis warning
TimeoutError = requests.exceptions.Timeout
