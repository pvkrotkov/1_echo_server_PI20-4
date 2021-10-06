import socket


SERVER_ADDRESS = ('', 9090)


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #  Создание объекта socket, указание его типа - UDP.
sock.bind(SERVER_ADDRESS) #  Cвязывает адрес и порт с сокетом.

while True:
    data, addr = sock.recvfrom(1024) #  Возвращает данные от клиента размером 1 кБ и адрес клиента.
    print(f'Получено сообщение: {data.decode()} от клиента', addr)