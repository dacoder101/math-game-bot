"""Lexer for the math game bot."""

# from .tokens import TokenType


class Lexer:
    """Lexer class for the math game bot."""

    def __init__(self, equation):
        self.equation = equation
        self.current_char = self.equation[0]