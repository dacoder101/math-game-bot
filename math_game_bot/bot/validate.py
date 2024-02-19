"""Functionality to validate user integer dictionary, raising an exception or supplying a verified dictionary."""

from dataclasses import dataclass
from ..exceptions import InvalidCharactersError


class ValidateIntegers:
    """Methods to validate an expression."""

    ints: str
    
    def get_numerical_form(self, x):
        """Return `x` as integer, or raise an error if impossible."""

        try:
            return int(x)
        except ValueError as e:
            raise InvalidCharactersError("Int dictionary is invalid") from e
    
    def verify_key(self, x):
        """Verify keys in the dictionary."""

        return x >= 0 and x <= 9
    
    def verify_value(self, x):
        """Verify values in the dictionary."""

        return x > 0