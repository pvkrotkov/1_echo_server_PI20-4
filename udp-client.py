#!/usr/bin/env python3
from socket import *
import sys

host = 'localhost'
port = 65432
addr = (host, port)

udp_socket = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input('write to server: ')
    if not data:
        udp_socket.close()
        sys.exit(1)

    # encode - перекодирует введенные данные в байты, decode - обратно
    data = data.encode()
    udp_socket.sendto(data, addr)
    data = udp_socket.recvfrom(1024)
    #data = data.decode()
    print(data[0].decode(), data[1])
