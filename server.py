# server.py
from http.server import HTTPServer, SimpleHTTPRequestHandler

class CORSAndThreadsHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # Allow cross-origin resource sharing
        self.send_header('Access-Control-Allow-Origin', '*')
        # Crucial headers required to unlock SharedArrayBuffer performance
        self.send_header('Cross-Origin-Opener-Policy', 'same-origin')
        self.send_header('Cross-Origin-Embedder-Policy', 'require-corp')
        super().end_headers()

if __name__ == '__main__':
    print("Launching advanced multi-threaded asset server on http://localhost:8000 ...")
    HTTPServer(('localhost', 8000), CORSAndThreadsHandler).serve_forever()