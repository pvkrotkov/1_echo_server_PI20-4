import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()
print('Соединение подключено')

while True:
    data = conn.recv(1024)
    if not data:
        print('Клиент был отключен')
        break
    print('Прием данных от клиента: ', data.decode())
    conn.send(data)
    print('Отправка данных клиенту: ', data.decode())
print('Соединение отключено')
conn.close()