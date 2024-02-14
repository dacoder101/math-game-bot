"""Math game functionality for the bot."""

# from .parser import Parser
from .exceptions import *


class MathGame:
    """Math game functionality for the bot. `operations` is a list of valid mathematical operations. If `operations` is None, the default operations are used."""

    def __init__(self, ints, game_max=20, operations=None):
        self.ints = self.validate_ints(ints)
        self.game_max = self.validate_max(game_max)

        self.operations = self.validate_operations(operations)

    def __str__(self):
        return f"""
        Math Game

        Allowed Numbers: {", ".join(str(i) for i in self.ints)}
        Write equations to complete all numbers from 0 to {self.game_max} using the allowed numbers and basic operations.
        """

    def validate_ints(self, ints):
        """Validate `ints` parameter to only accept integers, then sort them."""

        if isinstance(ints, int):
            ints = [ints]

        if not (all(isinstance(i, int) for i in ints) and len(ints) > 0):
            raise InvalidArgumentError("Elements in argument ints are not of type int")

        if not (all(i < 10 for i in ints)):
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

    def test_equation(self, equation):
        """Check if the solution to the equation is valid."""

        return Equation(equation, self).test_equation()


class Equation:
    """Equation class for the math game."""

    def __init__(self, equation, math_game):
        self.equation = equation
        self.game = math_game

    def __str__(self):
        return self.equation

    def test_equation(self):
        """Check if the equation is equal to self.max."""

        if not self.is_valid_equation():
            raise InvalidCharactersError()

        if not self.is_solution():
            raise InvalidSolutionError()

        return True

    def is_valid_equation(self):
        """Check if an equation is valid."""

        print(self.game.ints, self.game.operations, self.equation)

        return all(
            c in self.game.ints or c in self.game.operations for c in self.equation
        )

    def is_solution(self):
        """Check if the solution to the equation is valid."""

        solution = eval(self.equation)

        return (
            solution >= 0 and solution <= 20
        )  # Temporary, will create a custom parser later
