import socket

sock = socket.socket()
print('Запуск сервера')
sock.bind(('', 9090))
print('Начало прослушивания порта - 9090')
sock.listen(1)
conn, addr = sock.accept()
print('Соединение подключено')

while True:
    data = conn.recv(1024)
    if not data:
        print('Клиент был отключен')
        break
    print('Прием данных от клиента: ', data.decode('utf-8'))
    conn.send(data)
    print('Отправка данных клиенту: ', data.decode('utf-8'))
print('Соединение отключено')
conn.close()

