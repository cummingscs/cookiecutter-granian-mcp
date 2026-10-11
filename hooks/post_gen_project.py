"""Remove optional generated files that Cookiecutter cannot omit by path alone."""

from pathlib import Path


if "{{ cookiecutter.include_docker }}" != "yes":
    Path("Dockerfile").unlink(missing_ok=True)
