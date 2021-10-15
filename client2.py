from socket import *
import sys

host = 'localhost'
port = 9090
addr = (host, port)
print("Вы подключены")
sock = socket(AF_INET, SOCK_DGRAM)
name = ''
while name == '':
    name = input('Ваш логин: ')
while True:
    data = input("Введите сообщение для сервера: ")
    if not data:
        print('Соединение прервано')
        sock.close()
        sys.exit(1)
    if data == 'exit':
        print(f'{name} вышел из чата')
        break
    data = name + ': ' + data
    data = data.encode()
    sock.sendto(data, addr)
    data = sock.recvfrom(1024)
    print(f'{data[0].decode()}, {data[1]}')
