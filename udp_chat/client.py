import socket

from server import PORT


EXIT = 'exit'


def _main():
    """
    1. С помощью менеджера контекста, чтобы в случае ошибок сокет был точно
    закрыт, объявляем сокет типа UDP.
    3. В бесконечном цикле запрашиваем ввод нового сообщения. Проверяем, хочет
    ли пользователь выйти (совпадает ли его сообщение со строкой "exit").
    4. Если пользователь не хочет выйти, отправляем сообщение с помощью метода
    sendto, указывая сообщение, которое необходимо закодировать в байты методом
    encode, и кортеж с адресом и портом сервера.
    """
    with socket.socket(type=socket.SOCK_DGRAM) as sock:
        while True:
            message = input()
            if message == EXIT:
                break
            sock.sendto(message.encode(), ('localhost', PORT))


if __name__ == '__main__':
    _main()
