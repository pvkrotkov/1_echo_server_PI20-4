from socket import *

host = 'localhost'
port = 9090
addr = (host, port)
connections = []
sock = socket(AF_INET, SOCK_DGRAM)

sock.bind(addr)
print('Соединение установлено')
while True:
    print("Данные клиентов...")

    conn, addr = sock.recvfrom(1024)
    data = conn.decode()
    print(conn.decode())

    out = input('Ответить: ')
    out = out.encode()
    sock.sendto(out,addr)
print('Соединение отключено')
conn.close()
