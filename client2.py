from socket import *
import sys

addr = ('localhost', 1025)
print("Succesful connection!")
sock  = socket(AF_INET, SOCK_DGRAM)
nick=''
while nick == '':
	nick = input('Enter a nickname: ')
while True:
    data = input("Send data to a server: ")
    if not data:
        print('connection has been lost')
        sock.close()
        sys.exit(1)
    if data == 'exit':
        print("User has left the chatroom")
        break
    data = nick + ': ' + data
    data = data.encode()
    sock.sendto(data, addr)
    data = sock.recvfrom(1024)
    print(f'Servers reply: {data[0].decode()}, {data[1]}')