import socket
import threading

HOST = '127.0.0.1'
PORT = 65432

def handle_client(conn, addr):
    print(f"[CONNECTED] Client {addr[0]}:{addr[1]}")
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break

            message = data.decode()
            print(f"[RECEIVED] From {addr[0]}:{addr[1]} → {message}")

            response = "Message received"
            conn.send(response.encode())

    except socket.error as e:
        print("Client error:", e)

    finally:
        conn.close()
        print(f"[DISCONNECTED] Client {addr[0]}:{addr[1]}")

try:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Allow port reuse (important for labs)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print(f"Multi-Client Server running on {HOST}:{PORT}")

    while True:
        conn, addr = server_socket.accept()
        thread = threading.Thread(
            target=handle_client,
            args=(conn, addr),
            daemon=True
        )
        thread.start()

except socket.error as e:
    print("Server error:", e)

finally:
    server_socket.close()

