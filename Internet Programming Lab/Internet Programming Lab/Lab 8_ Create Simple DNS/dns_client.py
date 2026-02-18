import socket

HOST = "127.0.0.1"
PORT = 5353

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

domain = input("Enter domain name: ")

client.sendto(domain.encode(), (HOST, PORT))
ip, _ = client.recvfrom(1024)

print("IP Address:", ip.decode())

client.close()

