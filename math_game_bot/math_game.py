"""Math game functionality for the bot."""

from dataclasses import dataclass

from .lexer import Lexer
from .parser_ import Parser
from .interpreter import Interpreter


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

        tokens = Lexer(equation).generate_tokens()

        parser = Parser(tokens)

        tree = parser.parse()

        result = Interpreter().visit(tree).value

        if result in self.game_equations:
            self.game_equations[result] = equation

        return result

    def get_equations(self):
        """Return all the equations in the game in as an formatted string."""

        formatted_equations = []

        for k, v in self.game_equations.items():
            if v == "":
                formatted_equations.append(f"{k}: Not Solved")
            else:
                formatted_equations.append(f"{k}: {v}")

        return "\n".join(formatted_equations)
