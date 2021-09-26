import socket


PORT = 9090


def _main():
    """
    1. С помощью менеджера контекста, чтобы в случае ошибок сокет был точно
    закрыт, объявляем сокет типа UDP.
    2. Привязываем адрес и порт методом bind.
    3. В бесконечном цикле принимаем сообщения методом recvfrom с буфером 1 кБ.
    Метод возвращает кортеж, состоящий из байт и адреса клиента.
    4. Печатаем на экран адрес клиента и его декодированное методом decode
    сообщение.
    """
    with socket.socket(type=socket.SOCK_DGRAM) as sock:
        sock.bind(('', PORT))
        while True:
            data, addr = sock.recvfrom(1024)
            print(f'{addr}:', data.decode())


if __name__ == '__main__':
    _main()
