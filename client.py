from socket import *
import sys

host = 'localhost'
port = 9090
addr = (host, port)
print("Произошло подключение клиента")
sock  = socket(AF_INET, SOCK_DGRAM)
name =''
while name == '':
    name = input('Введите никнейм: ')
while True:
    data = input("Введите данные для сервера: ")
    if not data:
        print('Соединение разорвано')
        sock.close()
        sys.exit(1)
    if data == 'exit':
        print("участник чата завершил общение")
        break
    data = name + ': ' + data
    check_1 = name + ': ' + data
    data = data.encode()
    sock.sendto(data, addr)
    data = sock.recvfrom(1024)
    if name in data[0].decode():
        pass
    else:
        print(f'Данные от сервера: {data[0].decode()}, {data[1]}')
        print(check_1)