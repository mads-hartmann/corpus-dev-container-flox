import json
import threading
from http.client import HTTPConnection
from http.server import ThreadingHTTPServer

from app import Handler


def fetch_json(port, path):
    connection = HTTPConnection("127.0.0.1", port, timeout=5)
    try:
        connection.request("GET", path)
        response = connection.getresponse()
        body = response.read()
    finally:
        connection.close()

    return response.status, json.loads(body)


def main():
    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    port = server.server_address[1]
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()

    try:
        status, body = fetch_json(port, "/healthz")
        if status != 200 or body != {"ok": True}:
            raise SystemExit(f"unexpected health response: {status} {body}")

        status, body = fetch_json(port, "/")
        if status != 200 or body.get("message") != "hello from flox corpus":
            raise SystemExit(f"unexpected root response: {status} {body}")
    finally:
        server.shutdown()
        thread.join(timeout=5)


if __name__ == "__main__":
    main()

