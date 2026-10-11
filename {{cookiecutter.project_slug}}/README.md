# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

This project exposes an MCP Streamable HTTP endpoint at `http://127.0.0.1:8000/mcp` and uses [Granian](https://github.com/emmett-framework/granian) as its ASGI server.

## Quick start

```bash
uv sync --all-groups
uv run granian --interface asgi {{ cookiecutter.package_name }}.server:app --reload
```

Connect an MCP client to `http://127.0.0.1:8000/mcp`. The starter server provides `greet`, `health`, and `make_demo_receipt` tools. `make_demo_receipt` normalizes a phrase and returns its character count plus SHA-256 digest, making a successful MCP call easy to verify in an agent chat. Replace these starter tools with your own tools in `src/{{ cookiecutter.package_name }}/server.py`.

## Development

```bash
uv run ruff check .
uv run pytest
```

## Deployment notes

`app` is an ASGI application, so Granian can run it directly:

```bash
granian --interface asgi --host 0.0.0.0 --port 8000 {{ cookiecutter.package_name }}.server:app
```

The MCP SDK defaults to accepting localhost hosts only, which is appropriate for local development. Before exposing this server behind a real hostname, configure the SDK's transport security allowlist and authentication for that hostname. Do not treat the example tools as authorization.

{% if cookiecutter.include_docker == 'yes' -%}
## Container image

```bash
docker build -t {{ cookiecutter.project_slug }} .
docker run --rm -p 8000:8000 {{ cookiecutter.project_slug }}
```
{% endif %}
