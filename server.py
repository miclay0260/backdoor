import socket

sock = socket.socket()
sock.bind(("", 9696))
sock.listen(3)
conn, addr = sock.accept()
print ('connected:', addr)
while True:
    try:
        comm = input("-> ")
        if comm != "refuse":
            conn.send(comm.encode())  
            data = conn.recv(1024).decode()  
            print (data)
        else:
            print ("Refused")
            conn.close()
            exit()
    except:
         break
print("Connection refused")  
conn.close()
