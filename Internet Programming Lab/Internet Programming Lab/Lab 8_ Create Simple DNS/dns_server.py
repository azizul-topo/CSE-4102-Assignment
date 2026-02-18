import socket

HOST = "127.0.0.1"
PORT = 5353   # Safe port for lab

# Simple DNS records
dns = {
    "google.com": "142.250.190.14",
    "facebook.com": "157.240.229.35",
    "localhost": "127.0.0.1"
}

# Create UDP socket
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Make port reusable
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((HOST, PORT))

print("Simple DNS Server running...")
print(f"Listening on {HOST}:{PORT}")

while True:
    data, addr = server.recvfrom(1024)
    domain = data.decode()

    print("Query:", domain)

    ip = dns.get(domain, "Domain not found")
    server.sendto(ip.encode(), addr)

