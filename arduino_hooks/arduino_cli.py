#!/usr/bin/env python3
"""Wrapper script for arduino_cli.

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


class ArduinoCLI(StaticAnalyzerCmd):
    """Class for calling the Arduino CLI tool."""

    command = "arduino-cli"

    def __init__(self, args: List[str]):
        """Construct the ArduinoCLI Static Analyzer."""
        parser = ArgumentParser()
        # arduino lint uses the project dir rather than filenames.
        parser.add_argument("--project-dir", type=Path, default=Path.cwd().resolve())
        parser.add_argument("action", nargs="*", default=["ArduinoCLI"])
        hook_args, cli_args = parser.parse_known_args(args)
        if len(hook_args.action) > 1:
            self.raise_error(
                "Positional arguments found.",
                "Manual use of positional arguments is not supported by the hook.",
            )
        cli_args.insert(0, hook_args.action[0])  # argv0 required for clipy_hooks
        cli_args.append("compile")
        cli_args.append(hook_args.project_dir.__str__())
        super().__init__(
            self.command,
            cli_args,
            help_url="https://github.com/CreatingNull/arduino-hooks",
        )

    def run(self):
        """Run arduino-cli."""
        self.run_command()


def main(argv=None):
    """Execute arduino_cli module when called as a script."""
    cmd = ArduinoCLI(sys.argv if argv is None else argv)
    cmd.run()


if __name__ == "__main__":
    main()
