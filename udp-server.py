#!/usr/bin/env python3
# Модуль socket для сетевого программирования
from socket import *

# данные сервера
host = 'localhost'
port = 65432
addr = (host, port)

# socket - функция создания сокета
# первый параметр socket_family может быть AF_INET или AF_UNIX
# второй параметр socket_type может быть SOCK_STREAM(для TCP) или SOCK_DGRAM(для UDP)
udp_socket = socket(AF_INET, SOCK_DGRAM)
# bind - связывает адрес и порт с сокетом
udp_socket.bind(addr)

# Бесконечный цикл работы программы
while True:

    # Если мы захотели выйти из программы
    #question = input('Do you want to quit? y\\n: ')
    # if question == 'y':
    #    break

    print('...')

    # recvfrom - получает UDP сообщения
    conn, addr = udp_socket.recvfrom(1024)
    #print('client addr: ', addr)
    print(conn.decode())
    # sendto - передача сообщения UDP
    #udp_socket.sendto('message received by the server'.encode(), addr)
    udp_socket.sendto(conn, addr)


# udp_socket.close()
