import math
import statistics
from abc import ABC, abstractmethod
from .calculator import Calculator

class Command(ABC):
    @abstractmethod
    def execute(self):  # pragma: no cover
        pass  # pragma: no cover

class AddCommand(Command):
    def __init__(self, args):
        self.args = args
        self.calculator = Calculator()
    
    def execute(self):
        if len(self.args) != 2:
            raise ValueError("AddCommand requires exactly 2 arguments.")
        return self.calculator.add(self.args[0], self.args[1])

class SubtractCommand(Command):
    def __init__(self, args):
        self.args = args
        self.calculator = Calculator()
    
    def execute(self):
        if len(self.args) != 2:
            raise ValueError("SubtractCommand requires exactly 2 arguments.")
        return self.calculator.subtract(self.args[0], self.args[1])

class MultiplyCommand(Command):
    def __init__(self, args):
        self.args = args
        self.calculator = Calculator()
    
    def execute(self):
        if len(self.args) != 2:
            raise ValueError("MultiplyCommand requires exactly 2 arguments.")
        return self.calculator.multiply(self.args[0], self.args[1])

class DivideCommand(Command):
    def __init__(self, args):
        self.args = args
        self.calculator = Calculator()
    
    def execute(self):
        if len(self.args) != 2:
            raise ValueError("DivideCommand requires exactly 2 arguments.")
        return self.calculator.divide(self.args[0], self.args[1])

class SqrtCommand(Command):
    """Command to compute the square root of a number."""
    def __init__(self, args):
        self.args = args
    
    def execute(self):
        if len(self.args) != 1:
            raise ValueError("SqrtCommand requires exactly 1 argument.")
        if self.args[0] < 0:
            raise ValueError("Cannot take square root of a negative number.")
        return math.sqrt(self.args[0])

# Statistical Operations

class MeanCommand(Command):
    """Command to calculate the mean of a list of numbers."""
    def __init__(self, args):
        self.args = args

    def execute(self):
        if len(self.args) < 1:
            raise ValueError("MeanCommand requires at least 1 argument.")
        return statistics.mean(self.args)

class MedianCommand(Command):
    """Command to calculate the median of a list of numbers."""
    def __init__(self, args):
        self.args = args

    def execute(self):
        if len(self.args) < 1:
            raise ValueError("MedianCommand requires at least 1 argument.")
        return statistics.median(self.args)

class ModeCommand(Command):
    """Command to calculate the mode of a list of numbers."""
    def __init__(self, args):
        self.args = args

    def execute(self):
        if len(self.args) < 1:
            raise ValueError("ModeCommand requires at least 1 argument.")
        return statistics.mode(self.args)

class VarianceCommand(Command):
    """Command to calculate the variance of a list of numbers."""
    def __init__(self, args):
        self.args = args

    def execute(self):
        if len(self.args) < 2:
            raise ValueError("VarianceCommand requires at least 2 arguments.")
        return statistics.variance(self.args)

class CommandFactory:
    def __init__(self):
        self.commands = {
            "add": AddCommand,
            "subtract": SubtractCommand,
            "multiply": MultiplyCommand,
            "divide": DivideCommand,
            "sqrt": SqrtCommand,
            "mean": MeanCommand,
            "median": MedianCommand,
            "mode": ModeCommand,
            "variance": VarianceCommand
        }
    
    def create_command(self, command_name, args):
        command_class = self.commands.get(command_name.lower())
        if command_class:
            return command_class(args)
        return None
