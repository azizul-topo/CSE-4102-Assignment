import socket
import threading

HOST = '127.0.0.1'
PORT = 65432

def handle_client(conn, addr):
    print("Client connected:", addr)
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break

            print(f"Received from {addr}: {data.decode()}")

            # Echo back the same data
            conn.send(data)

    except socket.error as e:
        print("Client error:", e)

    finally:
        conn.close()
        print("Client disconnected:", addr)

try:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print("Multi-Client Echo Server running...")

    while True:
        conn, addr = server_socket.accept()

        # Create a new thread for each client
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

except socket.error as e:
    print("Server error:", e)

finally:
    server_socket.close()

