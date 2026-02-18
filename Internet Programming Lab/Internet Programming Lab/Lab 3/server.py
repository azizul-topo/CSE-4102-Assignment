import socket

HOST = '127.0.0.1'
PORT = 65432

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print("Server is running and waiting for connection...")

while True:
    conn, addr = server_socket.accept()
    print("Connected by", addr)

    data = conn.recv(1024)
    if data:
        print("Received:", data.decode())
        conn.send("Message received by server".encode())

    conn.close()

