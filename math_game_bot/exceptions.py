"""Exceptions for various class checks and functionality."""


class InvalidArgumentError(Exception):
    """Exception for invalid class arguments."""

    def __init__(self, message="An invalid argument was passed."):
        self.message = message


class InvalidCharactersError(Exception):
    """Exception for invalid equation characters."""

    def __init__(self, message="The equation includes invalid characters, integers, or operations"):
        self.message = message


class InvalidSolutionError(Exception):
    """Exception for invalid equation solutions."""

    def __init__(self, message="The equation solution is invalid"):
        self.message = message
