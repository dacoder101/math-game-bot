"""Functionality to validate user integer dictionary, raising an exception or supplying a verified dictionary."""

from dataclasses import dataclass
from .exceptions import InvalidCharactersError


@dataclass
class ValidateIntegers:
    """Methods to validate an expression."""

    ints: str

    def __post_init__(self):
        """Remove trailing comma from string."""

        self.ints = self.ints.strip()

        self.ints = self.remove_trailing_comma()

    def int_capability(self, x):
        """Return True if `x` is an integer, False otherwise."""
        try:
            int(x)
            return True
        except ValueError:
            return False

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

    def remove_trailing_comma(self):
        """Remove trailing comma from string."""

        if self.ints[-1] == ",":
            return self.ints[:-1]

        return self.ints

    def ints_to_list(self):
        """Convert a string to the list type."""

        pass

    def ints_to_dict(self):
        """Convert a string to the dict type."""

        pass

    def iterate_keys(self, x):
        """Validate a list of integers via keys."""

        return all(self.verify_key(i) for i in x)

    def iterate_values(self, x):
        """Validate a list of integers via values."""

        return all(self.verify_value(i) for i in x)

    def validate(self):
        """Validate; raise an exception or return a verified dictionary."""

        ints = self.ints

        if self.int_capability(ints):

            ints = self.get_numerical_form(ints)

            if self.verify_key(self.get_numerical_form(ints)):
                return {ints: 1}

        elif ints[0] in "([":
            self.ints_to_list()

        elif ints[0] == "{":
            self.ints_to_dict()

        else:
            raise InvalidCharactersError("Int dictionary is invalid")
