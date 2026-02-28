# Base PC connection via http
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import math

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        data = json.loads(body)

        start = data["start"]
        end = data["end"]

        total = 0
        for i in range(start, end):
            total += math.sqrt(i)

        response = json.dumps({"result": total}).encode()

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(response)

server = HTTPServer(("0.0.0.0", 8000), Handler)
server.serve_forever()
