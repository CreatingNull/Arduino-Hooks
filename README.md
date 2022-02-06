# ![NullTek Documentation](https://raw.githubusercontent.com/CreatingNull/NullTek-Assets/main/img/logo/NullTekDocumentationLogo.png) Pre-Commit Arduino Hooks

[![License](https://img.shields.io/:license-mit-blue.svg?style=flat-square)](LICENSE.md)

This project provides [pre-commit](https://github.com/pre-commit/pre-commit) hooks for [official arduino](https://github.com/arduino) command line tooling.

Currently, this includes:

* [arduino-lint](https://github.com/arduino/arduino-lint) - Linter for checking arduino projects for problems and conventions.

This project uses the pre-commit-pycli [clinters](https://github.com/CreatingNull/Pre-Commit-PyCLI), to handle most of the cross-platform, sub-process nastiness.

---

## Getting Started

To configure pre-commit see [pre-commit](https://github.com/pre-commit/pre-commit) for instructions

This project requires the `.ino` extension is comprehended by pre-commit, this extension only exists in [identify](https://github.com/pre-commit/identify) >= `2.4.3`.
If you are running an older version you either need a fresh pre-commit environment, or run `pip install --upgrade identify`.

### Arduino Lint 

Sample `.pre-commit-config.yaml`:

```yaml
-   repo: https://github.com/creatingnull/pre-commit-arduino
    rev: v0.2.0
    hooks:
    -   id: arduino-lint
```

To use the arduino lint hook you must already have the `arduino-lint` executable installed and **on path**.
You can find instructions on how to install this and pre-compiled binaries in the [offical docs](https://arduino.github.io/arduino-lint/latest/installation/).

To test you have this installed correctly on your system, run `arduino-lint --help` in your shell and verify this returns the help information.
If you are running in an environment where putting this on path is difficult, you may pass an `--install-path` argument to define the absolute path to the arduino-lint executable.

```yaml
-   repo: https://github.com/creatingnull/pre-commit-arduino
    rev: v0.2.0
    hooks:
    -   id: arduino-lint
    -   args: ["--install-path","/opt/arduino/"] 
```

---

## Donations

I just do this stuff for fun in my spare time, but feel free to:

[![Support via buymeacoffee](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/nulltek)

---

## License

The source of this repo uses the MIT open-source license, for details on the current licensing see [LICENSE](LICENSE.md) or click the badge above.
