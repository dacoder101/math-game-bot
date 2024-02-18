"""Math game functionality for the bot."""

from .exceptions import InvalidArgumentError, InvalidSolutionError
from .equation import Equation


class MathGame:
    """Math game functionality class for the bot. If `operations` is None, the default operations are used."""

    def __init__(self, ints, game_max=20, operations=None):
        self.ints = self.validate_ints(ints)
        self.game_max = self.validate_max(game_max)

        self.operations = self.validate_operations(operations)

        self.game_equations = {i: "" for i in range(0, self.game_max + 1)}

    def __str__(self):
        return f"""
        Math Game

        Allowed Numbers: {", ".join(str(i) for i in self.ints)}
        Write equations to complete all numbers from 0 to {self.game_max} using the allowed numbers and basic operations.

        Current equations:

        {self.get_equations()}
        """

    def validate_ints(self, ints):
        """Validate `ints` parameter to only accept integers, then sort them."""

        if isinstance(ints, int):
            ints = [ints]

        if not (all(isinstance(i, int) for i in ints) and len(ints) > 0):
            raise InvalidArgumentError("Elements in argument ints are not of type int")

        if not all(i < 10 for i in ints):
            raise InvalidArgumentError("Elements in argument ints are greater than 9")

        return [str(i) for i in sorted(ints)]

    def validate_max(self, game_max):
        """Validate `max` parameter to only accept integers."""

        if not isinstance(game_max, int):
            raise InvalidArgumentError("Game max argument is not of type int")

        return game_max

    def validate_operations(self, operations):
        """Validate `operations` parameter to only accept a list of valid mathematical operations."""

        default_operations = [
            "+",
            "-",
            "*",
            "/",
        ]

        if operations is None:
            return default_operations

        if not all(i in default_operations for i in operations):
            raise InvalidArgumentError(
                "Elements in argument operations are invalid mathematical operations"
            )

        return operations

    def add_equation(self, equation):
        """Check if the solution to the equation is valid."""

        solution = Equation(equation, self).test_equation()

        if self.game_equations[solution] == "":
            self.game_equations[solution] = equation
            return True

        raise InvalidSolutionError(
            "A solution for the submitted equation already exists"
        )

    def get_equations(self):
        """Return all the equations in the game in as an formatted string."""

        formatted_equations = []

        for k, v in self.game_equations.items():
            if v == "":
                formatted_equations.append(f"{k}: Not Solved")
            else:
                formatted_equations.append(f"{k}: {v}")

        return "\n".join(formatted_equations)