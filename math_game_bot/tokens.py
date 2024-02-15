"""Tokens for equations in the math game."""

from enum import Enum


class TokenType(Enum):
    """Types of tokens."""

    INT = 1
    ADD = 2
    SUB = 3
    MUL = 4
    DIV = 5
    MOD = 7
    EXP = 8
    LOG = 9
    LPAREN = 10
    RPAREN = 11
