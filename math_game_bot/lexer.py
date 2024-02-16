"""Lexer for the math game bot."""

from .tokens import TokenType

from enum import Enum


class Lexer:
    """Lexer class for the math game bot."""

    def __init__(self, equation):
        self.equation = equation.lower()
        self.current_char = self.equation[0]

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
