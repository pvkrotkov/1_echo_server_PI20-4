import socket

sock = socket.socket()
sock.bind(('',2000))
print('Запуск сервера...')

sock.listen(0)
print('Начало прослушивания порта')

conn, addr = sock.accept()
print(addr)

message = 'Hello!! '
print('Подключение клиента' + addr)

while True:
	data = conn.recv(1024)
	if not data:
		break
    
    	print('Прием данных от клиента' + addr)
	message += data.decode()
	conn.send(data)
	print(f'Отправка данных клиенту' + addr)
    
print('Отключение клиента' + addr)

print(message)

conn.close()
sock.close()

print('Остановка сервера')
