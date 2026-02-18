import socket

HOST = "127.0.0.2"
PORT = 8080   # safe lab port (reusable)

dns_records = {
    "csebatcheight1020.com": "127.0.0.2"
}

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Make port reusable
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((HOST, PORT))

print("Local DNS Server running...")
print(f"Listening on {HOST}:{PORT}")

while True:
    data, addr = server.recvfrom(1024)
    domain = data.decode().strip().lower()

    print("DNS Query:", domain)

    ip = dns_records.get(domain, "Domain not found")
    server.sendto(ip.encode(), addr)

