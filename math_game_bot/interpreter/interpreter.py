"""Interpreter for the math game bot."""

from .nodes import *
from .values import Number


class Interpreter:
    """Interpreter class for the math game bot."""

    def visit(self, node):
        """Visit a node and return the result."""

        method_name = f"visit_{type(node).__name__}"
        method = getattr(self, method_name)
        return method(node)

    def visit_NumberNode(self, node):
        """Return a Number object."""

        return Number(node.value)

    def visit_AddNode(self, node):
        """Return the Number object of two nodes added together."""

        return Number(self.visit(node.node_a).value + self.visit(node.node_b).value)

    def visit_SubtractNode(self, node):
        """Return the Number object of two nodes subtracted from each other."""

        return Number(self.visit(node.node_a).value - self.visit(node.node_b).value)

    def visit_MultiplyNode(self, node):
        """Return the Number object of two nodes multiplied together."""

        return Number(self.visit(node.node_a).value * self.visit(node.node_b).value)

    def visit_DivideNode(self, node):
        """Return the Number object of two nodes divided by each other."""

        return Number(self.visit(node.node_a).value / self.visit(node.node_b).value)

    def visit_PowerNode(self, node):
        """Return the Number object of two nodes exponentially."""

        return Number(self.visit(node.node_a).value ** self.visit(node.node_b).value)

    def visit_FactorialNode(self, node):
        """Return the Number object of the factorial of a node."""

        def factorial(n):
            if n == 0:
                return 1
            return n * factorial(n - 1)

        return Number(factorial(self.visit(node.node).value))

    def visit_PositiveNode(self, node):
        """Return the Number object of a positive node."""

        return self.visit(node.node)

    def visit_NegativeNode(self, node):
        """Return the Number object negative node."""

        return Number(-self.visit(node.node).value)
