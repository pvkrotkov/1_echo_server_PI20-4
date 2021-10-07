import socket
import sys
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
name =''
while name == '':
	name = input('Введите никнейм: ')
while True:
    data = input("Ваше сообщение: ")
    data = name + ': ' + data
    client.sendto(data.encode('utf-8'), ('localhost', 23618))
    if 'exit' in data:
        client.close()
        sys.exit(1)
        break
    back_msg = client.recv(1024).decode('utf-8')
    print('Ответ от сервера: ', back_msg)

client.close() 

