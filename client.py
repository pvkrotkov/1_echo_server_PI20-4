import socket
SERVER_ADDRESS = ('127.0.0.1', 9090)
sock = socket.socket()
sock.connect(SERVER_ADDRESS)
print('Соединение с сервером', SERVER_ADDRESS)
while True:
    message = input()
    if message == 'exit':
        break
    sock.send(message.encode())
    print(f'Отправка данных {message} серверу', SERVER_ADDRESS)
    data = sock.recv(1024)
    data_decode = data.decode()
    print(f'Прием данных {data_decode} от сервера', SERVER_ADDRESS)
    print(data_decode)

print(data.decode())
sock.close()
print ('Разрыв соединения с сервером', SERVER_ADDRESS)
