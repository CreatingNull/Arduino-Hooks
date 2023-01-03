# ![NullTek Documentation](https://raw.githubusercontent.com/CreatingNull/NullTek-Assets/main/img/logo/NullTekDocumentationLogo.png) Arduino Hooks

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/arduino-hooks?style=flat-square&logo=python&logoColor=white)](https://pypi.org/project/arduino-hooks/)
[![PyPI - Release Version](https://img.shields.io/pypi/v/arduino-hooks?style=flat-square&logo=pypi&logoColor=white)](https://pypi.org/project/arduino-hooks/)
[![Format](https://img.shields.io/github/actions/workflow/status/CreatingNull/arduino-hooks/run-pre-commit.yaml?branch=main&logo=pre-commit&style=flat-square&label=format)](https://github.com/CreatingNull/arduino-hooks/actions/workflows/run-pre-commit.yaml)
[![Tests](https://img.shields.io/github/actions/workflow/status/CreatingNull/arduino-hooks/run-tests.yaml?branch=main&logo=GitHub&style=flat-square&label=tests)](https://github.com/CreatingNull/arduino-hooks/actions/workflows/run-tests.yaml)
[![License](https://img.shields.io/github/license/CreatingNull/arduino-hooks?style=flat-square)](https://github.com/CreatingNull/arduino-hooks/blob/main/LICENSE.md)

This project provides [pre-commit](https://github.com/pre-commit/pre-commit) hooks for [arduino](https://github.com/arduino) command line tooling.
This is an un-official project.

Currently, this includes:

* [arduino-lint](https://github.com/arduino/arduino-lint) - Linter for checking arduino projects for problems and conformance to conventions.
* [arduino-cli](https://github.com/arduino/arduino-cli) - Limited to `compile` calls for verifying arduino code can be compiled.

This project uses [CliPy-Hooks](https://github.com/CreatingNull/clipy-hooks), to handle most of the cross-platform, sub-process nastiness.

---

## Getting Started

To configure pre-commit see [their official docs](https://pre-commit.com/) for instructions.

To use any of the arduino hooks below you must have the respective executables installed and **on path**.
If you are running in an environment where putting this on path is difficult, you may pass an `--install-dir` argument to define the absolute path to the arduino executable.

The hooked tools do not work with individual source files as is done with most pre-commit hooks, as these tools work against complete arduino projects.
By default, the hooks will treat the root directory as the project root, as is typical in arduino repositories.
In cases where this is not true, you can pass a `--project-dir` argument with the project root path to the hook.

Due to limitations in `argparse`, it is **highly** suggested that you pass all arguments with values using `--key=value` rather than `--key value`.

### Arduino Lint

Sample `.pre-commit-config.yaml`:

```yaml
-   repo: https://github.com/creatingnull/arduino-hooks
    rev: v0.2.0
    hooks:
    -   id: arduino-lint
```

You can find instructions on how to install `arduino-lint` and pre-compiled binaries in the [official docs](https://arduino.github.io/arduino-lint/latest/installation/).

For convenience this hook recognises the following arguments:

 * `--fail-on-warn` flag that will fail on any warning returned by arduino lint.
   Similar result to `compliance=strict` but even stricter.

You also may pass in supported `arduino-cli` [arguments](https://arduino.github.io/arduino-lint/latest/commands/arduino-lint/) which will be handed through to the executable.

```yaml
-   repo: https://github.com/creatingnull/arduino-hooks
    rev: v0.2.0
    hooks:
    -   id: arduino-lint
    -   args: ["--install-dir=/opt/arduino/", "--fail-on-warn", "--project-dir=src/"]
```

### Arduino CLI


Sample `.pre-commit-config.yaml`:

```yaml
-   repo: https://github.com/creatingnull/arduino-hooks
    rev: v0.2.0
    hooks:
    -   id: arduino-cli
        args: ["--fqbn=arduino:avr:nano"]
```
You can find instructions on how to install `arduino-cli` and pre-compiled binaries in the [official docs](https://arduino.github.io/arduino-cli/latest/installation/)


Must provide the full qualified board name for the target microcontroller, this parameter should be passed in `""` quotes due to yaml restrictions on `:` use.
You'll also need to have previously installed the [core](https://arduino.github.io/arduino-cli/latest/getting-started/#install-the-core-for-your-board) for this target and any [libs](https://arduino.github.io/arduino-cli/latest/getting-started/#add-libraries) required by your project.

---

## As a Github Action

You can add these hooks to your existing pre-commit workflow by adding a step to install the required dependencies.

See the following example step added to a `ubuntu-latest` pre-commit workflow:

```yaml
- name: Install Dependancies
  run: |
    curl -fsSL https://raw.githubusercontent.com/arduino/arduino-lint/main/etc/install.sh | sh
    curl -fsSL https://raw.githubusercontent.com/arduino/arduino-cli/master/install.sh | sh
    bin/arduino-cli core install arduino:avr
    bin/arduino-cli lib install NullPacketComms
    echo "${PWD}/bin/" >> $GITHUB_PATH
```

The process followed is to:

1. Install arduino-cli if used
2. Install arduino-lint if used
3. Install required cores for the arduino-cli hook(s)
4. Install required 3rd party libs for the arduino-cli hook(s)
5. Put arduino tooling on path

For more information you can check out [this project](https://github.com/CreatingNull/UOS-Arduino/blob/main/.github/workflows/run-pre-commit.yaml) implementing these hooks in a github workflow.

---

## Donations

I just do this stuff for fun in my spare time, but feel free to:

[![Support via buymeacoffee](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/nulltek)

---

## License

The source of this repo uses the MIT open-source license, for details on the current licensing see [LICENSE](https://github.com/CreatingNull/arduino-hooks/blob/main/LICENSE.md) or click the badge above.
