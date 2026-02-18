from http.server import HTTPServer, SimpleHTTPRequestHandler

class ReusableHTTPServer(HTTPServer):
    allow_reuse_address = True

HOST = "127.0.0.1"
PORT = 8080

server = ReusableHTTPServer((HOST, PORT), SimpleHTTPRequestHandler)

print(f"Server running at http://{HOST}:{PORT}")
server.serve_forever()

