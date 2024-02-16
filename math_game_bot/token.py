"""Token functionality for operators and keyword tokens utilized."""

from dataclasses import dataclass
from .token_type import TokenType


@dataclass
class Token:
    """Token functionality class for operators and keyword tokens utilized."""

    token_type: TokenType
    value: str

    def __str__(self):
        """Return string representation of token."""
        return self.value
