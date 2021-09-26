import socket

from server import PORT


EXIT = 'exit'


def _main():
    with socket.socket(type=socket.SOCK_DGRAM) as sock:
        while True:
            message = input()
            if message == EXIT:
                break
            sock.sendto(message.encode(), ('localhost', PORT))


if __name__ == '__main__':
    _main()
