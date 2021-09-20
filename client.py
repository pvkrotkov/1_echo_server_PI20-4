import socket

from server import PORT


EXIT = 'exit'


def _main():
    sock = socket.socket()
    sock.connect(('localhost', PORT))
    print('Соединение с сервером')

    while True:
        message = input()
        if message == EXIT:
            break
        print(f'Отправка данных "{message}" серверу')
        sock.send(message.encode())
        data = sock.recv(1024).decode()
        print(f'Прием данных "{data}" от сервера')
        print(data)

    sock.close()
    print('Разрыв соединения с сервером')


if __name__ == '__main__':
    _main()