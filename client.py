import socket
import time

host = "134.197.42.83"
port = 20001


def tryconnect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port)) 
    return s

def recvloop(s):
    while True:
        try:
            r = s.recv(1024)
            if len(r) == 0:
                print("[bot] got disconnected")    
                break

            print("[bot] received payload {}".format(len(r)))
        except:
            print("[bot] got disconnected")
            break


def loop():
    try:
        s = tryconnect()
        # if this doesnt throw any exception then we are good
        print("[bot] connected to {}:{}".format(host,port))
        recvloop(s)
    except:
        print("[bot] unable to connect to {}:{}".format(host,port))

loop()
print("EOL")
