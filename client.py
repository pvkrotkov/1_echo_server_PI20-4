import socket

sock = socket.socket()
sock.connect(('localhost', 9090))
print('Подключение к серверу')

def master():
    while True:
        message = input()
        if message == 'exit':
            break
        print(f'Отправка данных серверу: "{message}"')
        sock.send(message.encode())
        data = sock.recv(1024)
        print(f'Прием данных от сервера: "{data.decode()}"')
    sock.close()
    print('ОТКЛЮЧЕНИЕ')

master()