"""Tests the upstream sketch examples against applicable cli tools."""
import contextlib
import os
from pathlib import Path

import pytest


def test_invalid_sketch_errors(arduino_tool):
    """Checks for a non-zero exit code when run on errored source."""
    arduino_tool.paths[0] = str(Path("InvalidSketch/").resolve())
    # Suppress the CLI response, is confusing when viewing test results.
    with contextlib.redirect_stderr(open(os.devnull, "w", encoding="utf-8")):
        with pytest.raises(SystemExit):
            arduino_tool.run()


def test_cli_good_code(arduino_tool):
    """Checks for zero exit code when run on valid source."""
    arduino_tool.paths[0] = str(Path("ValidSketch/").resolve())
    assert arduino_tool.run() is None


def test_lint_no_project_fails(arduino_tool):
    """Checks when a project can't be resolved non-zero exit."""
    # Suppress the CLI response, is confusing when viewing test results.
    with contextlib.redirect_stderr(open(os.devnull, "w", encoding="utf-8")):
        with pytest.raises(SystemExit):
            arduino_tool.run()
