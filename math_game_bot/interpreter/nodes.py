"""Nodes for the AST of the math game bot's interpreter."""

from dataclasses import dataclass


@dataclass
class NumberNode:
    """
    Represents a node that holds a numerical value.
    """

    value: float

    def __repr__(self):
        return f"{self.value}"


@dataclass
class AddNode:
    """
    Represents a node that performs addition operation between two nodes.
    """

    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a} + {self.node_b})"


@dataclass
class SubtractNode:
    """
    Represents a node that performs subtraction operation between two nodes.
    """

    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a} - {self.node_b})"


@dataclass
class MultiplyNode:
    """
    Represents a node that performs multiplication operation between two nodes.
    """

    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a} * {self.node_b})"


@dataclass
class DivideNode:
    """
    Represents a node that performs division operation between two nodes.
    """

    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a} / {self.node_b})"


@dataclass
class ModuloNode:
    """
    Represents a node that performs modulo operation between two nodes.
    """

    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a} % {self.node_b})"


@dataclass
class PowerNode:
    """
    Represents a node that performs exponentiation operation between two nodes.
    """

    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a} ^ {self.node_b})"


@dataclass
class FactorialNode:
    """
    Represents a node that performs factorial operation on a single node.
    """

    node: any

    def __repr__(self):
        return f"({self.node}!)"
