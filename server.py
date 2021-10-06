from socket import *

addr = ('localhost', 1025)
connections = []
sock = socket(AF_INET, SOCK_DGRAM)

sock.bind(addr)
print('Server is running')
while True:
    print("clients data...")

    conn, addr = sock.recvfrom(1024)
    data = conn.decode()
    print(conn.decode())

    out = input('Reply: ')
    out = out.encode()
    sock.sendto(out,addr)
print('Connection has been lost')
conn.close()