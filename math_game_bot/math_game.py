"""Math game functionality for the bot."""


class MathGame:
    """Math functionality for the bot."""

    def __init__(self, ints, game_max=20):
        self.ints = self.validate_ints(ints)
        self.max = game_max

    def validate_ints(self, ints):
        """Validate `ints` parameter to only accept integers, and sort them."""

        if not all(isinstance(i, int) for i in ints):
            raise ValueError("All elements in ints must be integers")
        return sorted(ints)

    def __str__(self):
        return f"""
        Math Game

        Allowed Numbers: {", ".join(str(i) for i in self.ints)}
        Complete all numbers from 1 to {self.max} using the allowed numbers and basic operations.
        """
