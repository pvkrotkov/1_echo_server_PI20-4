from socket import *

host = 'localhost'
port = 9090
addr = (host, port)
sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(addr)
print('Соединение установлено')
while True:
    conn, addr = sock.recvfrom(1024)
    data = conn.decode()
    print("Сообщение клиента")
    print(conn.decode())
    out = input('Ответ: ')
    out = out.encode()
    sock.sendto(out, addr)
print('Соединение прервано')
conn.close()
