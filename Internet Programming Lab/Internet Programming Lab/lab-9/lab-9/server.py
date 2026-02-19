import socket

LISTEN_HOST = '0.0.0.0'
LISTEN_PORT = 53
GOOGLE_DNS = ('8.8.8.8', 53)

def Faysal_run_dns_proxy():
    print(f"--- Faysal's DNS Proxy Server Started ---")
    print(f"1. Listening for Mobile requests on {LISTEN_HOST}:{LISTEN_PORT}")
    print(f"2. Forwarding them to Google DNS {GOOGLE_DNS}")
    print(f"------------------------------------------------")

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
            server_socket.bind((LISTEN_HOST, LISTEN_PORT))
            
            while True:
                data, client_address = server_socket.recvfrom(512)
                
                print(f"[Log] Phone {client_address} requested a website...", end="")
                with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as proxy_socket:
                    proxy_socket.sendto(data, GOOGLE_DNS)
                    response_data, _ = proxy_socket.recvfrom(512)

                server_socket.sendto(response_data, client_address)
                print(f" Forwarded & Sent back! (Success)")

    except PermissionError:
        print("\n[ERROR] Permission Denied! Run as Administrator/Root.")
    except Exception as e:
        print(f"\n[ERROR] {e}")

if __name__ == "__main__":
    Faysal_run_dns_proxy()