import socket
sock = socket.socket()
sock.connect(('localhost', 9090))
print("Произошло подключение клиента")
while True:
    msg = input('Напишите строку: ')
    sock.send(msg.encode())
    if msg == 'exit':
        sock.close()
        break
    print(f'Отправка данных серверу {msg}')
    data = sock.recv(1024)
    print(f"Получение данных от сервера: {data.decode()}")

print('Соединение разорвано')
