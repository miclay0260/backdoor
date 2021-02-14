import socket

sock = socket.socket()
sock.bind(('', 8080))
sock.listen(3)
conn, addr = sock.accept()

print ('connected:', addr)
while True:
    try:
        comm = input("-> ")
        if comm != "refuse":
            conn.send(comm.encode())  # отправляем команду
            data = conn.recv(1024).decode()  # получаем результат
            print (data)
        else:
            print ("Refused")
            conn.close()
            exit()
    except:
         break
print("Connection refused")  # в случае, если соединение разорванно
conn.close()