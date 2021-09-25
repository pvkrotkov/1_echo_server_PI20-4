import socket

PORT = 9090  # порт

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:  # открытие сокета
    client.connect(("localhost", PORT))  # соединение с сервером
    client.send(input("type in your login: ").encode())  # запрос логина
    while True:
        try:
            message = input("send message: ")  # запрос сообщения
            client.send(message.encode())  # отправка сообщение
        except Exception as e:
            print("warning " + str(e))  # вывод служебного сообщения о возможной ошибке
