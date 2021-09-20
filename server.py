import socket


SERVER_ADDRESS = ('', 9090)


def _main():
    sock = socket.socket()
    sock.bind(SERVER_ADDRESS)
    sock.listen()
    conn, address = sock.accept()

    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.send(data)

    conn.close()
    sock.close()


if __name__ == '__main__':
    _main()
