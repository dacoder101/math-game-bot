"""Lexer for the math game bot."""

from .token_type import TokenType
from .token import Token
from .exceptions import InvalidCharactersError


WHITESPACE = " \n\t"
OPERATIONS = {
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

"""KEYWORDS = {
    "sqrt": TokenType.SQRT,
    "log": TokenType.LOG,
}"""


class Lexer:
    """Lexer class for the math game bot."""

    def __init__(self, equation):
        self.equation = iter(equation.lower())
        self.advance()

    def is_digit(self, char):
        """Check if a character is a digit, or decimal point."""
        return char.isdigit() or char == "."

    def is_operator(self, char):
        """Check if a character is an operator."""
        return char in OPERATIONS

    """def is_alpha(self, char):
        """"""Check if a character is a letter."""""""
        return char.isalpha()"""

    def generate_tokens(self):
        """Generate tokens from the equation."""

        while self.current_char is not None:

            if self.current_char in WHITESPACE:
                self.advance()

            elif self.is_digit(self.current_char):
                yield self.generate_number()

            elif self.is_operator(self.current_char):
                yield self.generate_operator()

            #elif self.is_alpha(self.current_char):
            #    yield self.generate_keyword()

            else:
                raise InvalidCharactersError(f"Invalid character: {self.current_char}")

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

        if number.startswith("."):
            number = "0" + number

        if number.endswith("."):
            number += "0"

        return Token(TokenType.NUM, float(number))

    def generate_operator(self):
        """Generate an operation token from the equation."""

        operation = self.current_char
        self.advance()

        return Token(OPERATIONS[operation])

    """def generate_keyword(self):
        """"""Generate a keyword token from the equation.""""""""
        keyword = self.current_char
        self.advance()

        while self.current_char is not None and self.is_alpha(self.current_char):
            keyword += self.current_char
            self.advance()

        if keyword in KEYWORDS:
            return Token(KEYWORDS[keyword])
        else:
            raise InvalidCharactersError(f"Invalid keyword: {keyword}")"""
