import socket

sock = socket.socket()
sock.bind(('', 25565))
sock.listen(1)
conn, addr = sock.accept()

print ('connected:', addr)
while True:
    try:
        comm = input("-> ")
        if comm == "refuse":
            conn.send(comm.encode())
            conn.close()
        else:
             conn.send(comm.encode())  # отправляем команду
             data = conn.recv(1024).decode()  # получаем результат
             print (data)
    except:
         break
print("Connection refused")  # в случае, если соединение разорванно
conn.close()
