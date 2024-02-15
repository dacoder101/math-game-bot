"""Tokens for equations in the math game."""


class Number:
    """Number token for the math game."""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Number({self.value})"


class Operator:
    """Operator token for the math game."""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Operator({self.value})"
