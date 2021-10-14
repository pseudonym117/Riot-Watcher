class IllegalArgumentError(RuntimeError):
    def __init__(
        self, argument_name: str, argument_value: str, extra_message: str = None
    ):
        message = (
            f"Illegal value provided for argument '{argument_name}': '{argument_value}'"
        )
        if extra_message:
            message += f" - {extra_message}"

        super().__init__(message)
