import sys
import subprocess
import time
import sys

total_bots = int(sys.argv[1]) if len(sys.argv)>1 else 10

print("RUNP will start {} bots".format(total_bots));
procs = []
for i in range(total_bots):
    proc = subprocess.Popen([sys.executable, 'client.py'])
    procs.append(proc)
    time.sleep(0.2)

for proc in procs:
    proc.wait()
