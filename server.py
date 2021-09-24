import socket

sock = socket.socket()
print('Запуск сервера')
sock.bind(('', 9090))
print('Начало прослушивания порта')
sock.listen(1)
conn, addr = sock.accept()
print('Подключение клиента')
print(addr)
print('Соединение подключено')

msg = ''

while True:
	data = conn.recv(1024)
	if not data:
		break
	print('Прием данных от клиента', data.decode())
	msg += data.decode()
	conn.send(data)
	print('Отправка данных клиенту', data.decode())

print(msg)
print('Остановка клиента')
conn.close()
print('Остановка сервера')