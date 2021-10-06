import socket


SERVER_ADDRESS = ('', 9090)


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #  Создание объекта socket, указание его типа - UDP.
while True:
    message = input('Введите Ваше сообщение: ')
    if message == 'exit':
        break
    sock.sendto(message.encode(), SERVER_ADDRESS) #  Отправка данных серверу по адресу.

sock.close() #  Разрыв соединения с сервером.