"""
Module: calculator
Provides basic arithmetic operations.
"""

class Calculator:
    """A simple calculator that performs basic arithmetic operations."""

    def add(self, a, b):
        """Return the sum of a and b."""
        return a + b

    def subtract(self, a, b):
        """Return the difference between a and b."""
        return a - b

    def multiply(self, a, b):
        """Return the product of a and b."""
        return a * b

    def divide(self, a, b):
        """Return the quotient of a divided by b. Raises ValueError for division by zero."""
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b
