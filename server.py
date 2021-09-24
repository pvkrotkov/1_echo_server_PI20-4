import socket

sock = socket.socket()
print('Запускаем сервер')
sock.bind(('', 9090))
print('Начинаем прослушивание порта 9090')
sock.listen(1)
conn, addr = sock.accept()
print('Соединение налажено')

while True:
    data = conn.recv(1024)
    if not data:
        print('Клиент отключен')
        break
    print('От клиента получено: ', data.decode('utf-8'))
    conn.send(data)
    print('Клиенту отправлено: ', data.decode('utf-8'))

print('Остановка сервера')
conn.close()