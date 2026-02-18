import socket

HOST = '127.0.0.1'
PORT = 65432

try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    print("Connected to Echo Server")

    while True:
        msg = input("Enter message (type exit to stop): ")

        if msg.lower() == "exit":
            break

        client_socket.send(msg.encode())
        data = client_socket.recv(1024)
        print("Echo from server:", data.decode())

except ConnectionRefusedError:
    print("Error: Server not running")

except socket.error as e:
    print("Socket error:", e)

finally:
    client_socket.close()

