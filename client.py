mport socket

def ser_ver():
    sock = socket.socket()  #Создание сокета и соединение с сервером        
    sock.connect(('localhost', 9090))
    print('Соединение с сервером')

    while True:         #Если выход происходит не через "exit", то клиент продолжает считывание строк
        mess = input()
        if mess == 'exit':
            break
        print(f'Отправка данных "{mess}" серверу')
        sock.send(mess.encode())
        data = sock.recv(1024).decode()               #Отправка и приём данных от сервера
        print(f'Прием данных "{data}" от сервера')
        print(data)

    sock.close()
    print('Разрыв соединения с сервером')

ser_ver()
