#!/usr/bin/env python3
"""Wrapper script for arduino_lint.

Script template based on https://github.com/pocc/pre-commit-hooks/
"""
import sys
from typing import List

from pre_commit_pycli.cli import StaticAnalyzerCmd


class ArduinoLint(StaticAnalyzerCmd):
    """Class for calling the Arduino Lint CLI tool."""

    command = "arduino-lint"
    lookbehind = "arduino-lint "

    def __init__(self, args: List[str]):
        super().__init__(
            self.command,
            args,
            help_url="https://github.com/CreatingNull/Pre-Commit-Arduino"
        )

    def run(self):
        """Run arduino-lint."""
        self.run_command()


def main(argv=None):
    cmd = ArduinoLint(sys.argv if argv is None else argv)
    cmd.run()


if __name__ == "__main__":
    main()
