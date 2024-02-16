"""Lexer for the math game bot."""

from .token_type import TokenType
from .token import Token


WHITESPACE = " \n\t"


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

    def is_digit(self, char):
        """Check if a character is a digit, or decimal point."""
        return char.isdigit() or char == "."

    def generate_tokens(self):
        """Generate tokens from the equation."""

        while self.current_char is not None:

            if self.current_char in WHITESPACE:
                self.advance()

            elif self.current_char.isdigit() or self.current_char == ".":
                yield self.generate_number()

    def advance(self):
        """Advance the iterator and return the next character."""

        try:
            self.current_char = next(self.equation)
        except StopIteration:
            self.current_char = None

    def generate_number(self):
        """Generate a number token from the equation."""

        number = self.current_char
        self.advance()

        while self.current_char is not None and self.is_digit(self.current_char):
            number += self.current_char
            self.advance()

            if number.count(".") > 1:
                break

        number += self.current_char
        self.advance()

        if number.startswith("."):
            number = "0" + number

        if number.endswith("."):
            number += "0"

        return Token(TokenType.NUM, float(number))
