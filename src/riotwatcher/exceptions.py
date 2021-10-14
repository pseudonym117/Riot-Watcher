import requests

from .Handlers import (
    ApiError as _ApiError,
    IllegalArgumentError as _IllegalArgumentError,
)

ApiError = _ApiError  # should silence code analysis warning
IllegalArgumentError = _IllegalArgumentError
TimeoutError = requests.exceptions.Timeout
