import socket
import threading

HOST = '127.0.0.1'
PORT = 65432

def client_task(thread_id, message):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOST, PORT))

        client_socket.send(message.encode())

        data = client_socket.recv(1024)
        print(f"[Thread {thread_id}] Server reply:", data.decode())

        client_socket.close()

    except socket.error as e:
        print(f"[Thread {thread_id}] Error:", e)


num_threads = int(input("Enter number of client threads: "))

threads = []

for i in range(num_threads):
    msg = input(f"Enter message for Thread {i}: ")

    thread = threading.Thread(
        target=client_task,
        args=(i, msg)
    )
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

