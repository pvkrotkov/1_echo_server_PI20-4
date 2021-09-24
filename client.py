import socket
sock = socket.socket()
sock.connect(('localhost', 9090))
print('Клиент подключен')
while True:
    msg = input('Введите, что вы хотите отправить ')
    sock.send(msg.encode('utf-8'))
    if msg=='' or msg=='exit':
        sock.close()
        break
    print('Отправляем данные серверу ', msg)
    data = sock.recv(1024)
    print('От сервера получено: ', msg)

print('Соединение прервано')