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

    def iterate_int_capability(self, x):
        """Validate a list of integers via int capability."""

        return all(self.int_capability(i) for i in x)

    def iterate_keys(self, x):
        """Validate a list of integers via keys."""

        return all(self.verify_key(i) for i in x)

    def iterate_values(self, x):
        """Validate a list of integers via values."""

        return all(self.verify_value(i) for i in x)

    def colon_count(self, x):
        """Return the count of colons in `x`."""

        return x.count(":")

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

            new_ints[f"{x}"] = split_ints.count(x)

        return new_ints

    def ints_to_dict(self):
        """Convert a string to the dict type."""

        split_ints = self.ints[1:-1]

        for i in split_ints.split(","):
            if self.colon_count(i) != 1:
                raise InvalidCharactersError(
                    "Int dictionary includes multiple colons for the same key-value pair."
                )

        split_ints = [i.strip() for i in split_ints.split(",")]

        dict_list = []

        for i in split_ints:
            dict_list.append([i.strip() for i in i.split(":")])

        for i in dict_list:
            if not self.iterate_int_capability(i):
                raise InvalidCharactersError(
                    "Int dictionary has values that are not numerical."
                )

        new_ints = {}

        for i in dict_list:
            new_ints[f"{i[0]}"] = int(i[1])

        if not self.iterate_keys([int(i) for i in new_ints]) or not self.iterate_values(
            [int(i) for i in new_ints.values()]
        ):
            raise InvalidCharactersError(
                "Keys or values in the dictionary are outside game limits."
            )

        return new_ints

    def validate(self):
        """Validate; raise an exception or return a verified dictionary."""

        ints = self.ints

        if self.int_capability(ints):

            ints = self.get_numerical_form(ints)

            if self.verify_key(self.get_numerical_form(ints)):
                return {f"{ints}": 1}

        elif ints[0] in "([" and ints[-1] in "])":
            if not (ints[0] == "[" and ints[-1] == "]") or (
                ints[0] == "(" and ints[-1] == ")"
            ):
                raise InvalidCharactersError(
                    "Int list has a different opening and closing character."
                )
            return self.ints_to_list()

        elif ints[0] == "{" and ints[-1] == "}":
            return self.ints_to_dict()

        else:
            raise InvalidCharactersError(
                "The program couldn't indentify the type of the input."
            )


@dataclass
class ValidateOperators:
    """Methods to validate user's operator list."""

    operators: str

    def __post_init__(self):
        """Strip `self.operators`."""

        self.operators = self.operators.strip()

    def str_to_list(self):
        """Convert a string to the list type."""

        operators = self.operators[1:-1]
        operators = [i.strip() for i in operators.split(",")]

        for i in operators:
            if len(i) != 1:
                raise InvalidCharactersError("Operator list is invalid")

        return operators

    def validate(self):
        """Validate; raise an exception or return a verified list."""

        operators = self.operators

        if operators[0] in "+-*/^%!" and len(operators) == 1:
            return [operators[0]]

        elif operators[0] in "[(" and operators[-1] in "])":

            if not (operators[0] == "[" and operators[-1] == "]") or (
                operators[0] == "(" and operators[-1] == ")"
            ):
                raise InvalidCharactersError(
                    "Operator list has a different opening and closing character."
                )

            operators = self.str_to_list()

            for i in operators:
                if i not in "+-*/^%!":
                    raise InvalidCharactersError(
                        "Operators in the operator list are not valid operators."
                    )

            return operators

        else:
            raise InvalidCharactersError(
                "The program couldn't indentify the type of the input."
            )


@dataclass
class ValidateNumbers:
    """Methods to validate the lexer generated NUM tokens."""

    numbers: list
    ints: dict

    def __post_init__(self):
        """Convert floats to ints, if possible."""

        self.numbers = [
            int(i.value) if i.value.is_integer() else i.value for i in self.numbers
        ]

    def validate(self):
        """Validate tokens to fit within `ints` guidelines"""

        str_numbers = [str(i) for i in self.numbers]
        str_str_numbers = "".join(str_numbers)

        for i in str_numbers:
            for x in i:
                if x not in self.ints:
                    raise InvalidCharactersError(
                        f'Invalid number. "{x}" is not allowed.'
                    )

                if str_str_numbers.count(x) > self.ints[x]:
                    raise InvalidCharactersError(
                        f'A number was used more times than allowed. "{x}" can only be used {self.ints[x]} times.'
                    )
