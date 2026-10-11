from {{ cookiecutter.package_name }}.server import app, build_demo_receipt, build_greeting


def test_build_greeting() -> None:
    assert build_greeting("Ada") == "Hello, Ada!"
    assert build_greeting("  ") == "Hello, world!"


def test_build_demo_receipt() -> None:
    assert build_demo_receipt("  Codex   MCP demo ") == {
        "marker": "GRANIAN-MCP-DEMO-2026",
        "message": "Codex MCP demo",
        "character_count": 14,
        "sha256": "9ef30c12d301684e36c0ec5e6be21f70a680d8dc9365e21056e8f4f18b17072c",
    }


def test_asgi_app_is_available() -> None:
    assert callable(app)
