import pytest
from clipy_hooks.cli import Command

from arduino_hooks.arduino_cli import ArduinoCLI
from arduino_hooks.arduino_lint import ArduinoLint


@pytest.fixture(scope="function")
def arduino_lint() -> ArduinoLint:
    """Creates an arduino lint object fixture for testing withs."""
    return ArduinoLint(["ArduinoLint"])  # Parameter mimics pre-commit argv[0]


@pytest.fixture(scope="function")
def arduino_cli() -> ArduinoCLI:
    """Creates an arduino cli object fixture for testing withs."""
    return ArduinoCLI(["ArduinoCLI", "--fqbn=arduino:avr:nano"])


@pytest.fixture(params=["arduino_lint", "arduino_cli"])
def arduino_tool(request) -> Command:
    """Fixture defining all tools to test against common functionality."""
    return request.getfixturevalue(request.param)
