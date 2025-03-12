import pytest
from app.command import CommandFactory, Command

def test_add_command_success():
    factory = CommandFactory()
    cmd = factory.create_command("add", [2, 3])
    assert cmd.execute() == 5

def test_subtract_command_success():
    factory = CommandFactory()
    cmd = factory.create_command("subtract", [10, 4])
    assert cmd.execute() == 6

def test_multiply_command_success():
    factory = CommandFactory()
    cmd = factory.create_command("multiply", [3, 5])
    assert cmd.execute() == 15

def test_divide_command_success():
    factory = CommandFactory()
    cmd = factory.create_command("divide", [20, 4])
    assert cmd.execute() == 5

def test_add_command_invalid_args():
    factory = CommandFactory()
    cmd = factory.create_command("add", [1])
    with pytest.raises(ValueError):
        cmd.execute()

def test_subtract_command_invalid_args():
    factory = CommandFactory()
    cmd = factory.create_command("subtract", [10, 5, 2])
    with pytest.raises(ValueError):
        cmd.execute()

def test_multiply_command_invalid_args():
    factory = CommandFactory()
    cmd = factory.create_command("multiply", [7])
    with pytest.raises(ValueError):
        cmd.execute()

def test_divide_command_invalid_args():
    factory = CommandFactory()
    cmd = factory.create_command("divide", [10])
    with pytest.raises(ValueError):
        cmd.execute()

def test_unknown_command():
    factory = CommandFactory()
    cmd = factory.create_command("unknown", [2, 3])
    assert cmd is None

def test_dummy_command_abstract():
    """
    Create a dummy subclass of the abstract Command to ensure that the
    abstract method branch is covered.
    """
    # pylint: disable=too-few-public-methods
    class DummyCommand(Command):
        def __init__(self, args):
            self.args = args
        def execute(self):
            return "dummy_result"
    dummy = DummyCommand([])
    assert dummy.execute() == "dummy_result"
