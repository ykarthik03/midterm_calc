from abc import ABC, abstractmethod
from .calculator import Calculator

class Command(ABC):
    @abstractmethod
    def execute(self):  # pragma: no cover
        pass

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

class CommandFactory:
    def __init__(self):
        self.commands = {
            "add": AddCommand,
            "subtract": SubtractCommand,
            "multiply": MultiplyCommand,
            "divide": DivideCommand
        }
    
    def create_command(self, command_name, args):
        command_class = self.commands.get(command_name.lower())
        if command_class:
            return command_class(args)
        return None
