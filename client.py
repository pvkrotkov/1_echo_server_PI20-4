import socket
print('создаем сокет ')
sock = socket.socket()
print(' соединяем с сервером')
sock.connect(('localhost', 8083))
print('если выход осуществляется не через exit,тогда клиент продолжает считывать строки')
while True:  
    msg =input()
    if msg=="exit":
        print('разрыв соединения с сервером')
        break
    print('посылаем данные серверу')
    sock.send(msg.encode())  
    print('принимаем данные от сервера')
    data = sock.recv(1024)
    print(data.decode())
sock.close() 
