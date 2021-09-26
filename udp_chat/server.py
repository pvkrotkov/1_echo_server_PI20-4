import socket


PORT = 9090


def _main():
    with socket.socket(type=socket.SOCK_DGRAM) as sock:
        sock.bind(('', PORT))
        while True:
            data, addr = sock.recvfrom(1024)
            print(f'{addr}:', data.decode())


if __name__ == '__main__':
    _main()
