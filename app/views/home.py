from fastapi import APIRouter
from fastapi.responses import HTMLResponse

from app import __version__

router = APIRouter()

DEMO_KEY = "demo-key-123"

ROUTES = [
    ("GET", "/quote", "Featured quote"),
    ("GET", "/quotes", "All quotes (optional ?tag=)"),
    ("GET", "/quotes/search?q=code", "Search quotes"),
    ("GET", "/quotes/random", "A random quote"),
    ("GET", "/quotes/{id}", "A quote by id"),
    ("GET", "/authors", "All authors"),
    ("GET", "/authors/{id}/quotes", "Quotes by author"),
    ("GET", "/tags", "Tags with counts"),
    ("GET", "/health", "Service health (no key needed)"),
]


def _render() -> str:
    rows = "\n".join(
        f'<tr><td class="m">{method}</td><td><code>{path}</code></td><td>{desc}</td></tr>'
        for method, path, desc in ROUTES
    )
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Quotes API</title>
<style>
  :root {{ color-scheme: light dark; }}
  body {{ font-family: system-ui, sans-serif; max-width: 760px; margin: 3rem auto; padding: 0 1rem; line-height: 1.5; }}
  h1 {{ margin-bottom: 0; }}
  .sub {{ color: #888; margin-top: .25rem; }}
  table {{ border-collapse: collapse; width: 100%; margin: 1.5rem 0; }}
  td {{ padding: .4rem .6rem; border-bottom: 1px solid #8884; }}
  .m {{ color: #2a7; font-weight: 600; width: 3rem; }}
  code {{ background: #8882; padding: .1rem .35rem; border-radius: 4px; }}
  pre {{ background: #8882; padding: 1rem; border-radius: 8px; overflow-x: auto; }}
  a {{ color: #4a9eff; }}
</style>
</head>
<body>
  <h1>Quotes API</h1>
  <p class="sub">v{__version__} &middot; all endpoints need an <code>X-API-Key</code> header</p>

  <h2>Endpoints</h2>
  <table>{rows}</table>

  <h2>Try it</h2>
  <pre>curl -H "X-API-Key: {DEMO_KEY}" http://localhost:8000/quote</pre>

  <p>Interactive docs: <a href="/docs">/docs</a></p>
</body>
</html>"""


@router.get("/", response_class=HTMLResponse, include_in_schema=False)
async def home():
    return _render()
