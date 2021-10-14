import socket


sock = socket.socket()
sock.connect('', 9090)
print('Соединение с сервером')
while True:
    message = input()
    if message == 'exit':
        break
    sock.send(message.encode())
    print('Отправка данных серверу')
    data = sock.recv(1024)
    data_decode = data.decode()
    print('Прием данных от сервера')
    print(data_decode)

sock.close()
print ('Разрыв соединения с сервером')
