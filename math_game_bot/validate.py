"""Functionality to validate user integer dictionary, raising an exception or supplying a verified dictionary."""

from dataclasses import dataclass
from .exceptions import InvalidCharactersError


@dataclass
class ValidateIntegers:
    """Methods to validate user's integer dictionary."""

    ints: str

    def __post_init__(self):
        """Strip `self.ints`."""

        self.ints = self.ints.strip()

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

    def ints_to_list(self):
        """Convert a string to the list type."""

        split_ints = self.ints[1:-1]

        split_ints = [i.strip() for i in split_ints.split(",")]

        for i in split_ints:
            if not self.int_capability(i):
                raise InvalidCharactersError("Int dictionary is invalid")

        split_ints = [int(i) for i in split_ints]

        if not self.iterate_keys(split_ints):
            raise InvalidCharactersError("Int dictionary is invalid")

        new_ints = {}
        used_ints = []

        for x in split_ints:

            if x in used_ints:
                continue

            new_ints[x] = split_ints.count(x)

        return new_ints

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
            return self.ints_to_list()

        elif ints[0] == "{":
            return self.ints_to_dict()

        else:
            raise InvalidCharactersError("Int dictionary is invalid")
