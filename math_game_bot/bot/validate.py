"""Functionality to validate user integer dictionary, raising an exception or supplying a verified dictionary."""

from dataclasses import dataclass
from ..exceptions import InvalidCharactersError

@dataclass
class ValidateIntegers:
    """Methods to validate an expression."""

    ints: str

    def int_capability(self, x):
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
    
    def validate(self):
        """Validate; raise an exception or return a verified dictionary."""

        ints = self.ints

        if self.int_capability(ints):

            ints = self.get_numerical_form(ints)

            if self.verify_key(self.get_numerical_form(ints)):
                return {ints: 1}