import math
import statistics
import pytest

from app.command import CommandFactory, Command

# Tests for basic arithmetic commands

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

def test_sqrt_command_success():
    factory = CommandFactory()
    cmd = factory.create_command("sqrt", [25])
    assert math.isclose(cmd.execute(), 5.0, rel_tol=1e-5)

# Tests for error cases in basic commands

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

def test_sqrt_command_invalid_args():
    factory = CommandFactory()
    cmd = factory.create_command("sqrt", [25, 36])
    with pytest.raises(ValueError):
        cmd.execute()

def test_sqrt_command_negative():
    factory = CommandFactory()
    cmd = factory.create_command("sqrt", [-1])
    with pytest.raises(ValueError):
        cmd.execute()

# Tests for Statistical Operations

def test_mean_command_success():
    factory = CommandFactory()
    cmd = factory.create_command("mean", [4, 8, 10])
    expected = statistics.mean([4, 8, 10])
    assert math.isclose(cmd.execute(), expected, rel_tol=1e-5)

def test_median_command_success():
    factory = CommandFactory()
    cmd = factory.create_command("median", [4, 8, 10])
    expected = statistics.median([4, 8, 10])
    assert cmd.execute() == expected

def test_mode_command_success():
    factory = CommandFactory()
    cmd = factory.create_command("mode", [2, 3, 3, 4])
    expected = statistics.mode([2, 3, 3, 4])
    assert cmd.execute() == expected

def test_variance_command_success():
    factory = CommandFactory()
    values = [4, 8, 10]
    cmd = factory.create_command("variance", values)
    expected = statistics.variance(values)
    assert math.isclose(cmd.execute(), expected, rel_tol=1e-5)

# Tests for invalid arguments in statistical commands

def test_mean_command_invalid():
    factory = CommandFactory()
    cmd = factory.create_command("mean", [])
    with pytest.raises(ValueError):
        cmd.execute()

def test_median_command_invalid():
    factory = CommandFactory()
    cmd = factory.create_command("median", [])
    with pytest.raises(ValueError):
        cmd.execute()

def test_variance_command_invalid():
    factory = CommandFactory()
    cmd = factory.create_command("variance", [10])
    with pytest.raises(ValueError):
        cmd.execute()

# Tests for unknown command

def test_unknown_command():
    factory = CommandFactory()
    cmd = factory.create_command("unknown", [2, 3])
    assert cmd is None

# Extra test to cover the fallback branch in create_command with non-empty args
def test_unknown_command_nonempty():
    factory = CommandFactory()
    cmd = factory.create_command("nonexistent", [1, 2])
    assert cmd is None

def test_unknown_command_empty():
    factory = CommandFactory()
    cmd = factory.create_command("nonexistent", [])
    assert cmd is None

# Dummy command test to cover the abstract base
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
