from http.server import HTTPServer, SimpleHTTPRequestHandler

class ReusableHTTPServer(HTTPServer):
    allow_reuse_address = True

HOST = ""        # or "0.0.0.0"
PORT = 8080

server = ReusableHTTPServer((HOST, PORT), SimpleHTTPRequestHandler)

print(f"Server running on port {PORT}")
server.serve_forever()

