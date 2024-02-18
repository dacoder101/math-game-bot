"""Math game functionality for the bot."""

from dataclasses import dataclass

from ..exceptions import InvalidArgumentError, InvalidSolutionError


@dataclass
class MathGame:
    """Math game functionality class for the bot. If `operations` is None, the default operations are used."""

    ints: dict
    game_max: int
    disallowed_operations: list = None

    def __post_init__(self):
        if self.disallowed_operations is None:
            self.disallowed_operations = []

        self.game_equations = {i: "" for i in range(0, self.game_max + 1)}

    def get_equations(self):
        """Return all the equations in the game in as an formatted string."""

        formatted_equations = []

        for k, v in self.game_equations.items():
            if v == "":
                formatted_equations.append(f"{k}: Not Solved")
            else:
                formatted_equations.append(f"{k}: {v}")

        return "\n".join(formatted_equations)
