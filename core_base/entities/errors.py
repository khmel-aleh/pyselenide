"""
Implements different errors

Implemented errors:
FatalError - stops robot execution
"""


class FatalError(AssertionError):
    """
    Implements error to stop robot execution
    """
    ROBOT_EXIT_ON_FAILURE = True


class ControlNotFoundException(Exception):
    def __init__(self, message):

        # Call the base class constructor with the parameters it needs
        super(ControlNotFoundException, self).__init__(message)


class TextNotFound(Exception):
    def __init__(self, message="Text was not found"):
        super(TextNotFound, self).__init__(message)


class ConfigurationError(Exception):
    ROBOT_EXIT_ON_FAILURE = True
    def __init__(self, message):
        super(ConfigurationError, self).__init__(message)


class ParameterError(Exception):
    def __init__(self, message):
        super(ParameterError, self).__init__(message)


class UndefinedExpandTableButtonState(Exception):
    def __init__(self, message):
        super(UndefinedExpandTableButtonState, self).__init__(message)