"""Token functionality for operators and keyword tokens utilized."""

from dataclasses import dataclass
from .token_type import TokenType


@dataclass
class Token:
    """Token functionality class for operators and keyword tokens utilized."""

    token_type: TokenType
    value: any = None

    def __repr__(self):
        return f"{self.token_type.name}:{self.value if self.value is not None else ''}"
