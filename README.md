# Cookiecutter Granian MCP server

A Cookiecutter template for Python MCP servers deployed as ASGI applications with Granian. It uses the official MCP Python SDK's Streamable HTTP transport, with an endpoint at `/mcp`.

## Use it locally

Install [Cookiecutter](https://cookiecutter.readthedocs.io/) and generate a project from this directory:

```bash
cookiecutter /path/to/cookiecutter-granian-mcp
```

For a non-interactive invocation:

```bash
cookiecutter /path/to/cookiecutter-granian-mcp --no-input project_name="Inventory MCP"
```

The generated project includes a `src/` package, example tools, pytest and Ruff configuration, and an optional Dockerfile. Start it with the command in its README, then connect an MCP client to `http://127.0.0.1:8000/mcp`.

## Publish and use from GitHub

This template does **not** need to be published to PyPI. Create a Git repository whose root contains `cookiecutter.json`, `hooks/`, and `{{cookiecutter.project_slug}}/`, then push it to GitHub. Users can invoke Cookiecutter directly against that repository.

One-off use without installing Cookiecutter persistently:

```bash
cd /where/you/want/the-new-project
uvx cookiecutter gh:cummingscs/cookiecutter-granian-mcp
```

Or install the Cookiecutter command once with uv:

```bash
uv tool install cookiecutter
cookiecutter gh:cummingscs/cookiecutter-granian-mcp
```

For this public template, the equivalent full Git URL is `https://github.com/cummingscs/cookiecutter-granian-mcp.git`.

Tag releases (for example, `v0.1.0`) and recommend a tag in production documentation to keep generated projects reproducible:

```bash
cookiecutter gh:cummingscs/cookiecutter-granian-mcp --checkout v0.1.0
```

When the template is the repository root, do not pass `--directory`; that option is only needed when a template lives in a subdirectory of a larger repository.
