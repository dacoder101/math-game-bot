"""Lexer for the math game bot."""

# from .token_type import TokenType

from enum import Enum


class TokenType(Enum):
    """Mathematical token types."""

    NUM = 1
    ADD = 2
    SUB = 3
    MUL = 4
    DIV = 5
    MOD = 7
    EXP = 8
    FACTORIAL = 9
    SQRT = 10
    LOG = 11
    LPAREN = 12
    RPAREN = 13


class Lexer:
    """Lexer class for the math game bot."""

    def __init__(self, equation):
        self.equation = iter(equation.lower())
        self.advance()

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
            self.current_char = next(self.equation)
        except StopIteration:
            self.current_char = None

    def generate_tokens(self):
        """Generate tokens from the equation."""

        while self.current_char is not None:
            
            pass