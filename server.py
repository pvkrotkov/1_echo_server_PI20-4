import socket


SERVER_ADDRESS = ('', 9090)


def _main():
    sock = socket.socket()
    sock.bind(SERVER_ADDRESS)
    print('Запуск сервера')
    sock.listen()
    print('Начало прослушивания порта', SERVER_ADDRESS[0])
    conn, addr = sock.accept()
    print('Подключение клиента', addr)

    while True:
        data = conn.recv(1024)
        if not data:
            break
        decoded = data.decode()
        print(f'Прием данных "{decoded}" от клиента', addr)
        conn.send(data)
        print(f'Отправка данных "{decoded}" клиенту', addr)

    conn.close()
    print('Отключание клиента', addr)
    sock.close()
    print('Отключение сервера')


if __name__ == '__main__':
    _main()
