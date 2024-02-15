"""Tokens for equations in the math game."""

from enum import Enum


class TokenType(Enum):
    """Types of tokens."""

    NUMBER = 1
    OPERATOR = 2
    LEFT_PAREN = 3
    RIGHT_PAREN = 4
    FACTORIAL = 5
    SQRT = 6
    LOGARITHM = 7
