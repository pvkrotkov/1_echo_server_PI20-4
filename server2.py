import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('localhost', 23618))
print('Начало диалога: ')


while True:
    data, addr = sock.recvfrom(1024)
    msg = data.decode('utf-8')
    if 'exit' in msg:
        print("Участник чата завершил диалог: ")
        sock.close()
        break
    print(msg)
    replymsg = input('Ответить: ')
    sock.sendto(replymsg.encode('utf-8'), addr)

sock.close()