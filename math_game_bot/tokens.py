"""Tokens for equations in the math game."""

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
