#!/usr/bin/env python3
"""Wrapper script for arduino_lint.

Script template based on https://github.com/pocc/pre-commit-hooks/
"""
import sys
from typing import List

from hooks.utils import StaticAnalyzerCmd


class ArduinoLint(StaticAnalyzerCmd):
    """Class for calling the Arduino Lint CLI tool."""

    command = "arduino-lint"
    lookbehind = "arduino-lint "

    def __init__(self, args: List[str]):
        super().__init__(self.command, self.lookbehind, args)
        self.parse_args(args)

    def run(self):
        """Run arduino-lint."""
        print(self.files)
        for filename in self.files:
            self.run_command(self.args + [filename])
            self.exit_on_error()


def main(argv=None):
    if argv is None:
        argv = sys.argv
    cmd = ArduinoLint(argv)
    cmd.run()


if __name__ == "__main__":
    main()
