import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 20001)) 

while True:
    print(s.recv(1024))
    s.send(b"yayasdfssdfasdfad")

s.close()
