import socket

HOST = "127.0.0.2"
PORT = 8080

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

domain = input("Enter domain name: ")
client.sendto(domain.encode(), (HOST, PORT))

ip, _ = client.recvfrom(1024)
print("Resolved IP:", ip.decode())

client.close()

