import socket
sock = socket.socket()
sock.connect(('localhost', 9090))
print("Произошло подключение клиента")
while True:
    msg = input()
    sock.send(msg.encode("utf-8"))
    if msg == 'exit' or msg == '':
        sock.close()
        break
    print(f'Отправка данных серверу {msg}')
    data = sock.recv(1024)
    print(f"Получение данных от сервера: {data.decode('utf-8')}")

print('Соединение разорвано')