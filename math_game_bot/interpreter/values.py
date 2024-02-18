from dataclasses import dataclass


@dataclass
class Number:
    "Number dataclass to represent a numerical value."

    value: float

    def __repr__(self):
        return f"{self.value}"
