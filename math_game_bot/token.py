"""Token functionality for operators and keyword tokens utilized."""

from dataclasses import dataclass
from .token_type import TokenType


@dataclass
class Token:
    """Token functionality class for operators and keyword tokens utilized."""

    type: TokenType
    value: any = None

    def __repr__(self):
        return self.type.name + (f":{self.value}" if self.value is not None else "")
