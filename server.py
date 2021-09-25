import socket

HOST = "127.0.0.1"  # стандартный адрес
PORT = 9090  # порт
clients = dict()  # словарь вида "адрес: логин"

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server:  # открытие сокета
    server.bind((HOST, PORT))  # установка хоста и порта
    while True:
        try:
            data, address = server.recvfrom(1024)  # получение данных
            if address not in clients.keys():  # проверка на наличие логина у полученного адреса
                clients.update({address: data.decode()})  # обновление словаря логинов
                continue
            print(f"{clients[address]}: {data.decode()}")  # вывод сообщения
        except Exception as e:
            print("warning " + str(e))  # вывод служебного сообщения о возможной ошибке
