import sys
import subprocess

procs = []
for i in range(200):
    proc = subprocess.Popen([sys.executable, 'client.py'])
    procs.append(proc)

for proc in procs:
    proc.wait()