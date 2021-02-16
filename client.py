import socket
import time
while True:
	try:
		sock = socket.socket()
		sock.connect("0.0.0.0", 8080)
		print("SUCESSFUL!")
	except:
		print("EXCEPTED!")
		time.sleep(5)
		continue
