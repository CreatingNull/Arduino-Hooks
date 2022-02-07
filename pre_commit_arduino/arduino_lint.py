#!/usr/bin/env python3
"""Wrapper script for arduino_lint.

Script template based on https://github.com/pocc/pre-commit-hooks/
"""
import sys
from argparse import ArgumentParser
from pathlib import Path
from typing import List

from pre_commit_pycli.cli import StaticAnalyzerCmd


class ArduinoLint(StaticAnalyzerCmd):
    """Class for calling the Arduino Lint CLI tool."""

    command = "arduino-lint"
    fail_on_warn = False

    def __init__(self, args: List[str]):
        parser = ArgumentParser()
        parser.add_argument("--fail-on-warn", action="store_true")
        hook_args, cli_args = parser.parse_known_args(args)
        self.fail_on_warn = hook_args.fail_on_warn
        # arduino lint uses the project dir rather than filenames.
        cli_args.append(Path.cwd().resolve().__str__())
        super().__init__(
            self.command,
            cli_args,
            help_url="https://github.com/CreatingNull/Pre-Commit-Arduino",
        )

    def run(self):
        """Run arduino-lint."""
        self.run_command()
        if self.fail_on_warn and " 0 WARNINGS" not in str(self.stdout):
            print(str(self.stdout, encoding="UTF-8"))
            self.raise_error(
                "Failed due to arduino-lint warnings.",
                "If this behaviour was not expected remove the '--fail-on-warn' flag.",
            )


def main(argv=None):
    cmd = ArduinoLint(sys.argv if argv is None else argv)
    cmd.run()


if __name__ == "__main__":
    main()
