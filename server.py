import socket

def master():
    sock = socket.socket()
    sock.bind(('', 9090))
    sock.listen()
    conn, msg = sock.accept()
    print('Подключение usera', msg)

    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(f'Прием данных от user: {data.decode()}', msg)
        conn.send(data)
        print(f'Отправка данных к user: {data.decode()}', msg)

    conn.close()
    sock.close()
    print('ОТКЛЮЧЕНИЕ')

master()
