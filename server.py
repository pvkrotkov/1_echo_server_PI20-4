import socket

def ser_ver():
    sock = socket.socket() #Создаём сокет
    sock.bind(('', 9090))   #Берём сокет с хостом и портом и связываем сокет с данным хостом и портом
    print('Запуск сервера')
    sock.listen() #Запускаем прослушивание
    print('Начало прослушивания порта', 9090)
    conn, addr = sock.accept()   #Приём подключения клиента к серверу
    print('Подключение клиента', addr)

    while True:               #Производим считывание данных клиента небольшими порциями
        data = conn.recv(1024)
        if not data:              #Производим отправку данных клиенту
            break
        dec = data.decode()
        print(f'Прием данных "{dec}" от клиента', addr)
        conn.send(data)
        print(f'Отправка данных "{dec}" клиенту', addr)

    conn.close()
    print('Отключение клиента', addr) #Производим отключение клиента и остановку сервера
    sock.close()
    print('Отключение сервера')
    
ser_ver()
