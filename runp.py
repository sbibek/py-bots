import sys
import subprocess
import time

procs = []
for i in range(10):
    proc = subprocess.Popen([sys.executable, 'client.py'])
    procs.append(proc)
    time.sleep(0.2)

for proc in procs:
    proc.wait()
