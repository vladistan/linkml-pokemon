#!/usr/bin/env python3
"""
Markdown server with full Mermaid diagram support.
Converts markdown to HTML and renders Mermaid diagrams client-side.
"""

import http.server
import socketserver
import sys
import re
from pathlib import Path
import markdown
import html

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>LinkML Pokemon Data Dictionary</title>
    <script type="module">
        import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
        mermaid.initialize({{
            startOnLoad: true,
            theme: 'default',
            themeVariables: {{
                primaryColor: '#f8f9fa',
                primaryTextColor: '#24292f',
                primaryBorderColor: '#d0d7de',
                lineColor: '#24292f',
                secondaryColor: '#ffffff',
                tertiaryColor: '#f6f8fa',
                background: '#ffffff',
                mainBkg: '#ffffff',
                secondBkg: '#f6f8fa'
            }},
            flowchart: {{
                useMaxWidth: true,
                htmlLabels: true
            }},
            classDiagram: {{
                useMaxWidth: true
            }}
        }});
    </script>
    <script>
        // Fix hash navigation for case mismatch between links and IDs
        window.addEventListener('load', function() {{
            function scrollToHash() {{
                const hash = window.location.hash.substring(1);
                if (hash) {{
                    // Try exact match first
                    let element = document.getElementById(hash);
                    if (!element) {{
                        // Try lowercase version
                        element = document.getElementById(hash.toLowerCase());
                    }}
                    if (element) {{
                        element.scrollIntoView({{ behavior: 'smooth' }});
                    }}
                }}
            }}

            // Handle initial page load
            scrollToHash();

            // Handle hash changes
            window.addEventListener('hashchange', scrollToHash);
        }});
    </script>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif;
            line-height: 1.6;
            color: #24292f;
            background-color: #ffffff;
            max-width: 1200px;
            margin: 0 auto;
            padding: 32px;
        }}

        h1, h2, h3, h4, h5, h6 {{
            margin-top: 24px;
            margin-bottom: 16px;
            font-weight: 600;
            line-height: 1.25;
        }}

        h1 {{
            font-size: 2em;
            border-bottom: 1px solid #d0d7de;
            padding-bottom: 0.3em;
        }}

        h2 {{
            font-size: 1.5em;
            border-bottom: 1px solid #d0d7de;
            padding-bottom: 0.3em;
        }}

        h3 {{ font-size: 1.25em; }}

        p {{
            margin-top: 0;
            margin-bottom: 16px;
        }}

        code {{
            padding: 0.2em 0.4em;
            margin: 0;
            font-size: 85%;
            background-color: rgba(175,184,193,0.2);
            border-radius: 6px;
            font-family: ui-monospace, SFMono-Regular, SF Mono, Consolas, Liberation Mono, Menlo, monospace;
        }}

        pre {{
            padding: 16px;
            overflow: auto;
            font-size: 85%;
            line-height: 1.45;
            background-color: #f6f8fa;
            border-radius: 6px;
            margin-bottom: 16px;
        }}

        pre code {{
            background: none;
            padding: 0;
        }}

        table {{
            border-spacing: 0;
            border-collapse: collapse;
            width: 100%;
            margin-top: 0;
            margin-bottom: 16px;
        }}

        table th, table td {{
            padding: 6px 13px;
            border: 1px solid #d0d7de;
            text-align: left;
        }}

        table th {{
            font-weight: 600;
            background-color: #f6f8fa;
        }}

        table tr:nth-child(2n) {{
            background-color: #f6f8fa;
        }}

        .mermaid {{
            text-align: center;
            margin: 24px 0;
            background: #ffffff;
            border: 1px solid #d0d7de;
            border-radius: 6px;
            padding: 16px;
        }}

        .mermaid-error {{
            background-color: #fff5f5;
            border: 1px solid #fd6c6c;
            border-radius: 6px;
            padding: 16px;
            margin: 16px 0;
            color: #d73a49;
        }}

        blockquote {{
            padding: 0 1em;
            color: #656d76;
            border-left: 0.25em solid #d0d7de;
            margin: 0 0 16px 0;
        }}

        ul, ol {{
            padding-left: 2em;
            margin-top: 0;
            margin-bottom: 16px;
        }}

        li {{
            margin: 0.25em 0;
        }}

        a {{
            color: #0969da;
            text-decoration: none;
        }}

        a:hover {{
            text-decoration: underline;
        }}

        .highlight {{
            background: #f6f8fa;
            border-radius: 6px;
            padding: 16px;
            margin-bottom: 16px;
        }}
    </style>
</head>
<body>
{content}
</body>
</html>"""


def process_mermaid_blocks(html_content):
    """Convert code blocks with mermaid language to mermaid divs."""
    # Patterns to match both classDiagram and erDiagram blocks
    patterns = [
        (
            r'<div class="highlight"><pre><span></span><code><span class="n">classDiagram</span>(.*?)</code></pre></div>',
            "classDiagram",
        ),
        (
            r'<div class="highlight"><pre><span></span><code>erDiagram\n(.*?)</code></pre></div>',
            "erDiagram",
        ),
    ]

    def replace_mermaid(match, diagram_type):
        mermaid_code = match.group(1).strip()
        # Clean up all HTML tags and spans
        mermaid_code = re.sub(r"<[^>]*>", "", mermaid_code)
        # Clean up extra whitespace but preserve line breaks
        mermaid_code = re.sub(r"\n\s*\n", "\n", mermaid_code)
        # Decode HTML entities
        mermaid_code = html.unescape(mermaid_code)
        # Rebuild the full diagram
        full_diagram = f"{diagram_type}\n{mermaid_code}"
        return f'<div class="mermaid">\n{full_diagram}\n</div>'

    result = html_content
    for pattern, diagram_type in patterns:
        result = re.sub(
            pattern, lambda m: replace_mermaid(m, diagram_type), result, flags=re.DOTALL
        )

    return result


class MermaidMarkdownHandler(http.server.SimpleHTTPRequestHandler):
    """HTTP handler that serves markdown files as HTML with Mermaid support."""

    def do_GET(self):
        # Always serve the markdown content since it's a single-page document
        # Hash fragments like #Species are handled client-side by the browser
        self.serve_markdown()

    def serve_markdown(self):
        """Serve the datadict.md file as HTML with Mermaid support."""
        try:
            # Find the datadict.md file
            datadict_path = Path("project/datadict.md")
            if not datadict_path.exists():
                datadict_path = Path("datadict.md")

            if not datadict_path.exists():
                self.send_error(
                    404, "datadict.md not found. Run 'just gen-project' first."
                )
                return

            # Read markdown content
            with open(datadict_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Convert markdown to HTML with extensions
            md = markdown.Markdown(
                extensions=["fenced_code", "tables", "codehilite", "toc", "attr_list"],
                extension_configs={"codehilite": {"css_class": "highlight"}},
            )

            html_content = md.convert(content)

            # Process Mermaid code blocks
            html_content = process_mermaid_blocks(html_content)

            # Wrap in template
            full_html = HTML_TEMPLATE.format(content=html_content)

            # Send response
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.send_header("Cache-Control", "no-cache")
            self.end_headers()
            self.wfile.write(full_html.encode("utf-8"))

        except Exception as e:
            self.send_error(500, f"Error serving markdown: {str(e)}")

    def log_message(self, format, *args):
        """Custom log message."""
        print(f"[{self.log_date_time_string()}] {format % args}")


def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000

    print("🚀 LinkML Pokemon Data Dictionary Server")
    print(f"📊 Server running at: http://localhost:{port}")
    print("📈 Full Mermaid diagram support enabled!")
    print("📁 Serving: project/datadict.md")
    print("⚡ Press Ctrl+C to stop\n")

    # Enable socket reuse
    socketserver.TCPServer.allow_reuse_address = True

    try:
        with socketserver.TCPServer(
            ("localhost", port), MermaidMarkdownHandler
        ) as httpd:
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n👋 Server stopped.")
    except OSError as e:
        if "Address already in use" in str(e):
            print(f"❌ Error: Port {port} is already in use.")
            print(
                f"💡 Try a different port: uv run --group dev python mermaid_server.py {port + 1}"
            )
        else:
            print(f"❌ Server error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
