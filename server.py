import socket
print ('создаем сокет')
sock=socket.socket()
print('берем сокет с хостом и портом')
sock.bind(('localhost',8083))
print('связываем сокет с данным хостом и портом')
print('запускаем режим прослушивания')
sock.listen()
print('принимаем подключение клиента к серверу')
conn,addr=sock.accept()
print(addr)
msg=''
print('считываем данные от клиента небольшими порциями')
while True:
    print('отправка данных клиенту')
    data=conn.recv(1024)
    if not data:
        break
    msg += data.decode()
    conn.send(data) 
    print(msg)
    msg=''
print('отключение клиента')
print('остановка сервера')
conn.close()
