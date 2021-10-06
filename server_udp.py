import socket


SERVER_ADDRESS = ('', 9090)


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(SERVER_ADDRESS)

while True:
    data, addr = sock.recvfrom(1024)
    print(f'Получено сообщение: {data.decode()} от клиента', addr)