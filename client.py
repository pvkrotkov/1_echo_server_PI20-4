import socket
from server import SERVER_ADDRESS


EXIT = 'exit'


def _main():
    sock = socket.socket()
    sock.connect(SERVER_ADDRESS)

    while True:
        message = input()
        if message == EXIT:
            break
        sock.send(message.encode())
        data = sock.recv(1024).decode()
        print(data)

    sock.close()


if __name__ == '__main__':
    _main()