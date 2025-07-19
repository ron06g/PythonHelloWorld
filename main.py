import json
from http.server import BaseHTTPRequestHandler, HTTPServer

# Charger la config JSON
with open("config/config.json", "r") as f:
    config = json.load(f)

PORT = config.get("port", 80)
MESSAGE = config.get("message", "Hello World!")

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(MESSAGE.encode())

if __name__ == "__main__":
    print(f"[INFO] Serveur en écoute sur le port {PORT}")
    httpd = HTTPServer(('', PORT), Handler)
    httpd.serve_forever()
