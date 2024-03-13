"""Math game functionality for the bot."""

from dataclasses import dataclass

from .exceptions import InvalidSolutionError, InvalidArgumentError

from .lexer import Lexer
from .parser_ import Parser
from .interpreter import Interpreter

from .validate import ValidateNumbers


@dataclass
class MathGame:
    """Math game functionality class for the bot."""

    ints: dict
    game_max: int
    disallowed_operations: list = None

    def __post_init__(self):
        if self.disallowed_operations is None:
            self.disallowed_operations = []

        self.game_equations = {i: "" for i in range(0, self.game_max + 1)}

    def __str__(self):
        return f"""Equations:
        
        {self.get_equations()}"""

    def submit_equation(self, equation):
        """Submit an equation to the game."""

        tokens = list(Lexer(equation).generate_tokens(self.disallowed_operations))

        numbers = [token for token in tokens if isinstance(token.value, float)]

        ValidateNumbers(numbers, self.ints).validate()

        parser = Parser(tokens)

        tree = parser.parse()

        result = Interpreter().visit(tree).value

        if result in self.game_equations:
            if self.game_equations[result] != "":
                raise InvalidSolutionError(
                    "The result of the equation is already in the game."
                )

            self.game_equations[result] = equation
        else:
            raise ValueError("The result of the equation is not in the game.")

    def remove_equation(self, result):
        """Remove an equation from the game."""

        if result in self.game_equations and self.game_equations[result] != "":
            self.game_equations[result] = ""
        else:
            raise InvalidArgumentError(
                "The result of the equation is not in the game, or does not yet have a solution."
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
