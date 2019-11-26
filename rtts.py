import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind(("0.0.0.0", 20001))
s.listen(5)
connection, address = s.accept()
print(connection)
for i in range(10):
    t1 = time.time()
    connection.send(b"testtesttesttesttest")
    connection.recv(1024)
    t2 = time.time()
    print("{} {} rtt:{}".format(t1, t1, t2-t1))
