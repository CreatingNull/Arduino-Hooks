import pytest

from pre_commit_arduino.arduino_lint import ArduinoLint


@pytest.fixture(scope="function")
def arduino_lint() -> ArduinoLint:
    """Creates an arduino lint object fixture for testing withs."""
    return ArduinoLint(["ArduinoLint"])
