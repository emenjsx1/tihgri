import http.server
import socketserver
import os

PORT = 8080

class SPA_Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Serve the actual file if it exists (e.g. assets)
        if os.path.exists(self.translate_path(self.path)) and not self.path.endswith('/'):
            super().do_GET()
        else:
            # Otherwise route everything to index.html (React Router will handle the URL)
            self.path = '/index.html'
            super().do_GET()

with socketserver.TCPServer(("", PORT), SPA_Handler) as httpd:
    print("SPA Server running at port", PORT)
    httpd.serve_forever()
