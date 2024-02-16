"""Lexer for the math game bot."""

from .token_type import TokenType


class Lexer:
    """Lexer class for the math game bot."""

    def __init__(self, equation):
        self.equation = iter(equation.lower())

        self.operations = {
            "+": TokenType.ADD,
            "-": TokenType.SUB,
            "*": TokenType.MUL,
            "x": TokenType.MUL,
            "/": TokenType.DIV,
            "%": TokenType.MOD,
            "^": TokenType.EXP,
            "!": TokenType.FACTORIAL,
            "(": TokenType.LPAREN,
            ")": TokenType.RPAREN,
            "[": TokenType.LPAREN,
            "]": TokenType.RPAREN,
        }

        self.keywords = {"sqrt": TokenType.EXP, "log": TokenType.LOG}

    def advance(self):
        """Advance the iterator and return the next character."""

        try:
            return next(self.equation)
        except StopIteration:
            return None

    def generate_tokens(self):
        """Generate tokens from the equation."""

        pass
