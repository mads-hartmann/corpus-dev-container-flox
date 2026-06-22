import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/healthz":
            self._write_json({"ok": True})
            return

        if self.path == "/":
            self._write_json({"message": "hello from flox corpus"})
            return

        self.send_error(404, "not found")

    def log_message(self, format, *args):
        return

    def _write_json(self, body):
        data = json.dumps(body).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)


def main():
    host = os.environ.get("HOST", "0.0.0.0")
    port = int(os.environ.get("PORT", "8000"))
    server = ThreadingHTTPServer((host, port), Handler)
    print(f"listening on http://{host}:{port}", flush=True)
    server.serve_forever()


if __name__ == "__main__":
    main()

