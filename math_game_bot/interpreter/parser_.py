"""Parser for the math game bot."""

from .token import TokenType
from .nodes import *
from ..exceptions import InvalidCharactersError


class Parser:
    """Parser class for the math game."""

    def __init__(self, tokens):
        self.tokens = iter(tokens)
        self.advance()

    def advance(self):
        """Advance to the next token."""

        try:
            self.current_token = next(self.tokens)
        except StopIteration:
            self.current_token = None

    def parse(self):
        """Parse the tokens and return the AST."""

        if self.current_token is None:
            return None

        result = self.expr()

        if self.current_token is not None:
            raise InvalidCharactersError("Invalid syntax")

        return result

    def expr(self):
        """Parse an expression."""

        result = self.term()

        while self.current_token is not None and self.current_token.type in (
            TokenType.ADD,
            TokenType.SUB,
        ):
            if self.current_token.type == TokenType.ADD:
                self.advance()
                result = AddNode(result, self.term())
            elif self.current_token.type == TokenType.SUB:
                self.advance()
                result = SubtractNode(result, self.term())

        return result

    def term(self):

        result = self.power()

        while self.current_token is not None and self.current_token.type in (
            TokenType.MUL,
            TokenType.DIV,
        ):
            if self.current_token.type == TokenType.MUL:
                self.advance()
                result = MultiplyNode(result, self.power())
            elif self.current_token.type == TokenType.DIV:
                self.advance()
                result = DivideNode(result, self.power())

        return result

    def power(self):

        result = self.factorial()

        while self.current_token is not None and self.current_token.type in (
            TokenType.EXP,
        ):
            if self.current_token.type == TokenType.EXP:
                self.advance()
                result = PowerNode(result, self.factorial())

        return result

    def factorial(self):
        result = self.factor()

        while self.current_token is not None and self.current_token.type in (
            TokenType.FACTORIAL,
        ):
            if self.current_token.type == TokenType.FACTORIAL:
                self.advance()
                result = FactorialNode(result)

        return result

    def factor(self):
        """Parse a factor."""

        token = self.current_token

        if token.type == TokenType.LPAREN:
            self.advance()
            result = self.expr()

            if self.current_token.type != TokenType.RPAREN:
                raise InvalidCharactersError("Invalid syntax")

            self.advance()

            return result

        elif token.type == TokenType.NUM:
            self.advance()

            return NumberNode(token.value)

        raise InvalidCharactersError("Invalid syntax")
