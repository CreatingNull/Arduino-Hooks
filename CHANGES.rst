Version 0.4.0
-------------

:Date: TBC

* Officially Supporting python 3.12.
* Clipy-Hooks updated to 0.2.1.
* Arduino-CLI used tested in CI updated to 0.35.2.

Version 0.3.0
-------------

:Date: 4-January-2022

* Officially Supporting python 3.11.
* Fixing the GitHub workflow badges in the README.
* Updating clipy-hooks from 0.1.1 to 0.2.0.
* Renamed changelog to ``CHANGES.rst`` to be more consistent with newer projects.
* Shifting project to use ``isort`` in preference to ``reorder-python-imports``.
  This is for consistency with newer projects and ease of use.
* Adding dead code detection, static typing, and doc linting to pre-commit hooks.
* Updating pre-commit hooks to latest.
* Removing .pylintrc file as new versions of pylint don't really require this.
* Suppressed output from CLI tools during tests when the test intentionally triggers errors.
  This was producing confusing results where it look as though tests were silently failing.

Version 0.2.0
-------------

:Date: 5-March-2022

* Adding ``arduino-cli`` compile support.

Version 0.1.0
-------------

:Date: 9-February-2022

* Initial release with ``arduino-lint`` support.
