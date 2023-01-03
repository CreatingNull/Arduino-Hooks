"""Module for checking the functionality of the arduino-lint hook."""
from pathlib import Path

import pytest

from arduino_hooks.arduino_lint import ArduinoLint


def test_constructor(arduino_lint: ArduinoLint):
    """Check a normal creation of the object is set up as expected."""
    assert not arduino_lint.fail_on_warn
    assert len(arduino_lint.args) == 0
    assert len(arduino_lint.paths) == 1


def test_project_dir_arg():
    """Checks passing a project directory argument to the hook works."""
    arduino_lint = ArduinoLint(["arduino-lint", "--project-dir=ValidSketch/"])
    assert len(arduino_lint.args) == 0
    assert arduino_lint.run() is None


def test_fail_on_warn_arg():
    """Checks failing on all warning flag works."""
    arduino_lint = ArduinoLint(["arduino-lint", "--fail-on-warn"])
    arduino_lint.paths[0] = str(Path("WarningSketch/").resolve())
    with pytest.raises(SystemExit):
        arduino_lint.run()
    # Sanity check doesn't fail when flag is disabled
    arduino_lint.fail_on_warn = False
    assert arduino_lint.run() is None


def test_fail_on_warn_pass(arduino_lint: ArduinoLint):
    """Just verify fail on warn doesn't trigger a failure with a perfect
    pass."""
    arduino_lint.paths[0] = str(Path("ValidSketch/").resolve())
    arduino_lint.fail_on_warn = True
    assert arduino_lint.run() is None
