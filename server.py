import socket

sock = socket.socket()
sock.bind(('', 9090))
print('Начало прослушивания порта 9090')

sock.listen(1)
conn, addr = sock.accept()
print('Соединение подключено:', *addr)

while True:
    data = conn.recv(1024)
    if not data:
        break
    print('Получено: ', data.decode('utf-8'))
    conn.send(data)
    print('Отправлено: ', data.decode('utf-8'))

conn.close()
print('Соединение отключено')
