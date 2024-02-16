"""Equation functionality for the math game bot."""

from .exceptions import InvalidCharactersError, InvalidSolutionError


class Equation:
    """Equation functionality class for the math game."""

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

        return eval(self.equation)

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
            solution >= 0 and solution <= self.game.game_max
        )  # Temporary, will create a custom interpreter later
