#!/usr/bin/env python3
"""Minimal HTTP server for ngrok CLI quickstart."""
from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        html = (
            "<!DOCTYPE html><html><head><title>Echo ngrok quickstart</title></head>"
            "<body><h1>Hello from Python HTTP Server on pinto!</h1>"
            "<p>Port 8080 - secured by ngrok Google OAuth.</p></body></html>"
        )
        self.wfile.write(html.encode("utf-8"))

    def log_message(self, fmt, *args):
        print(f"[quickstart:8080] {self.address_string()} - {fmt % args}")


if __name__ == "__main__":
    port = 8080
    print(f"Serving at http://localhost:{port}")
    HTTPServer(("", port), Handler).serve_forever()