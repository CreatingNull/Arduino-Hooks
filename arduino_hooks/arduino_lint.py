#!/usr/bin/env python3
"""Wrapper script for arduino_lint.

Script template based on https://github.com/pocc/pre-commit-hooks/
"""
import sys
from argparse import ArgumentParser
from pathlib import Path
from typing import List

from clipy_hooks.cli import StaticAnalyzerCmd

# Ignore duplication here as this is boilerplate for
# instantiating the base class.
# pylint: disable=R0801


class ArduinoLint(StaticAnalyzerCmd):
    """Class for calling the Arduino Lint CLI tool."""

    command = "arduino-lint"
    fail_on_warn = False

    def __init__(self, args: List[str]):
        """Construct the ArduinoLint Static Analyzer."""
        parser = ArgumentParser()
        parser.add_argument("--fail-on-warn", action="store_true")
        # arduino lint uses the project dir rather than filenames.
        parser.add_argument("--project-dir", type=Path, default=Path.cwd().resolve())
        hook_args, cli_args = parser.parse_known_args(args)
        self.fail_on_warn = hook_args.fail_on_warn
        cli_args.append(hook_args.project_dir.__str__())
        super().__init__(
            self.command,
            cli_args,
            help_url="https://github.com/CreatingNull/arduino-hooks",
        )

    def run(self):
        """Run arduino-lint."""
        self.run_command()
        if self.fail_on_warn and "no errors or warnings" not in str(self.stdout):
            print(str(self.stdout, encoding="UTF-8"))
            self.raise_error(
                "Failed due to arduino-lint warnings.",
                "If this behaviour was not expected remove the '--fail-on-warn' flag.",
            )


def main(argv=None):
    """Execute arduino_lint module when called as a script."""
    cmd = ArduinoLint(sys.argv if argv is None else argv)
    cmd.run()


if __name__ == "__main__":
    main()
