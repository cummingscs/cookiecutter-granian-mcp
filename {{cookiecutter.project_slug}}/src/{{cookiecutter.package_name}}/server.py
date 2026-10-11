"""MCP tools and the ASGI application served by Granian."""

from hashlib import sha256

from mcp.server.fastmcp import FastMCP


mcp = FastMCP(
    "{{ cookiecutter.server_name }}",
    instructions="{{ cookiecutter.description }}",
    json_response=True,
    stateless_http=True,
)


def build_greeting(name: str) -> str:
    """Return the greeting used by the example MCP tool."""
    clean_name = name.strip() or "world"
    return f"Hello, {clean_name}!"


def build_demo_receipt(message: str) -> dict[str, str | int]:
    """Create a deterministic receipt that makes an MCP call easy to verify."""
    normalized_message = " ".join(message.split()) or "empty message"
    digest = sha256(normalized_message.encode("utf-8")).hexdigest()
    return {
        "marker": "GRANIAN-MCP-DEMO-2026",
        "message": normalized_message,
        "character_count": len(normalized_message),
        "sha256": digest,
    }


@mcp.tool()
def greet(name: str = "world") -> str:
    """Return a friendly greeting. Replace this example with domain tools."""
    return build_greeting(name)


@mcp.tool()
def make_demo_receipt(message: str) -> dict[str, str | int]:
    """Return a deterministic receipt for text, proving this Granian MCP server handled the call."""
    return build_demo_receipt(message)


@mcp.tool()
def health() -> dict[str, str]:
    """Report that this MCP server is ready to receive requests."""
    return {"status": "ok"}


# Granian imports this ASGI application. It serves Streamable HTTP at /mcp.
app = mcp.streamable_http_app()


def main() -> None:
    """Explain how to run this ASGI application."""
    mcp.run(transport="streamable-http")


if __name__ == "__main__":
    main()
