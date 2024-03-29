"""Contains value classes for the interpreter."""

from dataclasses import dataclass


@dataclass
class Number:
    "Number class to represent a numerical value."

    value: float

    def __repr__(self):
        return f"{self.value}"
