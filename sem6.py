import socket
import threading
from time import sleep
ip = "51.250.16.220"
port = 55555

sock = socket.socket()
addr = (ip, port)
sock.connect(addr)
data_out = input()
sock.send(data_out.encode('ascii'))

# ya_sock = socket.socket()
# addr = ("87.250.250.242", 443)
# ya_sock.connect(addr)
# data_out = b"GET / HTTP/1.1\r\nHost:ya.ru\r\n\r\n"
# ya_sock.send(data_out)
# data_in = b""

def recieving():
    # global data_in
    while True:
        data_chunk = sock.recv(1024)
        # data_in = data_in + data_chunk
        if data_chunk:
            print(data_chunk)

def send():
    data_out = input("\n")
    sock.send(data_out.encode('ascii'))
    # if data_out == "exit":
        # return False
    return data_out

rec_thread = threading.Thread(target=recieving)
rec_thread.start()

while True:
    # stop_word = ''
    if send() == "exit":
        break

sock.close()

# s = threading.Thread(target=send)
# s.start()

# sleep(4)
# print(data_in)
# ya_sock.close()