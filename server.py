import socket
SERVER_ADDRESS = ('127.0.0.1', 9090)
sock = socket.socket()
sock.bind(SERVER_ADDRESS)
print('Запуск сервера', SERVER_ADDRESS)
sock.listen()
print('Начало прослушивания порта', SERVER_ADDRESS[1])
conn, addr = sock.accept()
print('Подключение клиента', addr)
while True:
    data = conn.recv(1024)
    if not data:
        break
    print(f'Прием данных {data.decode()} от клиента', addr)
    conn.send(data)
    print(f'Отправка данных {data.decode()} клиенту', addr)
print('Отключение клиента', addr)

conn.close()
sock.close()
print('Остановка сервера', SERVER_ADDRESS)
