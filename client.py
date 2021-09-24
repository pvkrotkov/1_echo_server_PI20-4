import socket
from time import sleep

sock = socket.socket()
sock.connect(('localhost', 9090))
print('Произошло сединение с сервером')
while True:
    msg = str(input('Введите строку или "выход" чтобы выйти: '))
    sock.send(msg.encode())
    if msg == 'выход':
        break
    print(f'Отправка данных серверу {msg}')
    data = sock.recv(1024)
    print(f'Прием данных сервером: {data.decode()}')

sock.close()
print('Разрыв соединения с сервером')
