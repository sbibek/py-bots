import socket
import time
import _thread as thread
from secrets import token_bytes
import sys

listen_port = 20001
randomattackpayload = token_bytes(14)  
attack_interval = int(sys.argv[2]) if len(sys.argv)>2 else 5 
total_send = int(sys.argv[1]) if len(sys.argv)>1 else 10

bots = []


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind(("0.0.0.0", listen_port))
s.listen(5)
print("[cnc] started at {}:{}".format("0.0.0.0", listen_port))
print("[cnc] will use random attack payload '{}' of length {} bytes".format(randomattackpayload, len(randomattackpayload)))
print("[cnc] will use attack interval of {}s and will send {} packets in total".format(attack_interval, total_send))

def attack():
    for bot in bots:
        try:
            bot.send(randomattackpayload)
        except socket.error:
            # client has disconnected
            bots.remove(bot)
            print("[cnc] bot disconnected, attack interval:{}s total bots: {}".format(attack_interval, len(bots)))

def closeConnections():
    for bot in bots:
        try:
            bot.close()
        except:
            print("unable to close")

def runner():
    print("waiting 60s before sending attacks");
    time.sleep(60)
    count = 0
    while True:
        if count == total_send:
            print("[cnc] total send reached")
            break
        attack()
        count = count + 1
        print("[cnc] attacks sent "+str(count))
        time.sleep(attack_interval)

    # if we are here means that total send has completed
    closeConnections()

try:
    thread.start_new_thread(runner,())
    print('[cnc] runner thread started')
except:
    print("error launching thread")



while True:
    connection, address = s.accept()
    bots.append(connection)
    print("bot added {}:{}, attack interval:{}s total bots:{}".format(address[0], address[1], attack_interval, len(bots)))
