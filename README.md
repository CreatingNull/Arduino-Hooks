# ![NullTek Documentation](https://raw.githubusercontent.com/CreatingNull/NullTek-Assets/main/img/logo/NullTekDocumentationLogo.png) Pre-Commit Arduino Hooks

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pre-commit-arduino?style=flat-square&logo=python&logoColor=white)](https://pypi.org/project/pre-commit-arduino/)
[![PyPI - Release Version](https://img.shields.io/pypi/v/pre-commit-arduino?style=flat-square&logo=pypi&logoColor=white)](https://pypi.org/project/pre-commit-arduino/)
[![Format](https://img.shields.io/github/workflow/status/CreatingNull/pre-commit-arduino/pre-commit?logo=pre-commit&style=flat-square&label=format)](https://github.com/CreatingNull/pre-commit-arduino/actions/workflows/run-pre-commit.yaml)
[![Tests](https://img.shields.io/github/workflow/status/CreatingNull/pre-commit-arduino/tests?logo=GitHub&style=flat-square&label=tests)](https://github.com/CreatingNull/pre-commit-arduino/actions/workflows/run-tests.yaml)
[![License](https://img.shields.io/github/license/CreatingNull/pre-commit-arduino?style=flat-square)](https://github.com/CreatingNull/Pre-Commit-Arduino/blob/master/LICENSE.md)
[![Code Style](https://img.shields.io/badge/style-black-000000.svg?style=flat-square)](https://github.com/psf/black)

This project provides [pre-commit](https://github.com/pre-commit/pre-commit) hooks for [arduino](https://github.com/arduino) command line tooling.

Currently, this includes:

* [arduino-lint](https://github.com/arduino/arduino-lint) - Linter for checking arduino projects for problems and conformance to conventions.

This project uses [pre-commit-pycli](https://github.com/CreatingNull/Pre-Commit-PyCLI), to handle most of the cross-platform, sub-process nastiness.

---

## Getting Started

To configure pre-commit see [pre-commit](https://github.com/pre-commit/pre-commit) for instructions

This project requires the `.ino` extension is comprehended by pre-commit, this extension only exists in [identify](https://github.com/pre-commit/identify) >= `2.4.3`.
If you are running an older version you either need a fresh pre-commit environment, or run `pip install --upgrade identify`.

### Arduino Lint

Sample `.pre-commit-config.yaml`:

```yaml
-   repo: https://github.com/creatingnull/pre-commit-arduino
    rev: v0.1.1
    hooks:
    -   id: arduino-lint
```

To use the arduino lint hook you must already have the `arduino-lint` executable installed and **on path**.
You can find instructions on how to install this and pre-compiled binaries in the [official docs](https://arduino.github.io/arduino-lint/latest/installation/).

To test you have this installed correctly on your system, run `arduino-lint --help` in your shell and verify this returns the help information.
If you are running in an environment where putting this on path is difficult, you may pass an `--install-dir` argument to define the absolute path to the arduino-lint executable.

For convenience this hook recognises the following arguments:

 * `--fail-on-warn` flag that will fail on any warning returned by arduino lint.
   Similar result to `compliance=strict` but even stricter.
 * `--project-dir` if your project doesn't exist at the root directory and you don't want to waste time with `--recurse=true`.

Due to limitations in `pre-commit-pycli` it is **highly** suggested that you pass all arguments with values using `--key=value` rather than `--key value`.

You also may pass in supported `arduino-cli` [arguments](https://arduino.github.io/arduino-lint/latest/commands/arduino-lint/) which will be handed through to the executable.

```yaml
-   repo: https://github.com/creatingnull/pre-commit-arduino
    rev: v0.1.1
    hooks:
    -   id: arduino-lint
    -   args: ["--install-dir=/opt/arduino/", "--fail-on-warn", "--project-dir=src/"]
```

---

## Donations

I just do this stuff for fun in my spare time, but feel free to:

[![Support via buymeacoffee](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/nulltek)

---

## License

The source of this repo uses the MIT open-source license, for details on the current licensing see [LICENSE](https://github.com/CreatingNull/Pre-Commit-Arduino/blob/master/LICENSE.md) or click the badge above.
