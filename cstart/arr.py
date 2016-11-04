#!/usr/bin/env python

dd = 0
maximum = 2800 - dd
nodes = ["node2", "node3"]
md5 = {"node2":200, "node3":300}
bcr = {"node2":200, "node3":300}
gpu_available = {"node2":[1,2,3,4,5,6,7,8], "node3":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]}
sec = 5
runed = 25
alert = 2400 - dd
auto = True
hash_type = "b"

import urllib
import subprocess
import time
import os
from socketIO_client import SocketIO, LoggingNamespace
import signal

def handler(signal_num,frame):
    raw_input()
    os.system("pfornode killall -9 hashcat")
    exit()

signal.signal(signal.SIGINT, handler)

clientdir = os.environ["CLIENTDIR"]

def p(n):
    global m
    m = 22.5*float(n)

socketIO = SocketIO('localhost', 8800, LoggingNamespace)
socketIO.on('power', p)

def power_now():
    global m
    socketIO.wait(seconds=1)
    print "new power", m
    return int(m)

def get_hashcat_now(n):
    try:
        return map(lambda x:int(x)+1,subprocess.check_output("ssh %s nvidia-smi | awk '/hashcat/{printf $2\"\\n\"}'"%n,shell=True).split())
    except:
        return gpu_available[n]

def run_hashcat(node,gpu,hash_type):
    to_run = "ssh %s 'source %s; export DEVICEFLAG=\"-d %d\";%s %s' 1>/dev/null 2>&1&"%(\
        node,\
        os.path.join(clientdir,"..","env.conf"),\
        gpu,\
        os.path.join(clientdir,"client.py"),\
        hash_type,\
    )
    print "RUN", to_run
    os.system(to_run)

def main():
    while True:
        if not auto:
            continue
        power = [power_now() for i in range(sec)]
        power=max(power)
        delta = maximum - power
        print "delta:\t",delta
        for i in nodes:
            times = md5 if hash_type == "m" else bcr
            print hash_type,i,times[i]
            if delta > times[i]:
                try:
                    empty = (set(gpu_available [i]) - set(get_hashcat_now(i))).pop()
                    print empty,"in",gpu_available[i],"-",get_hashcat_now(i)
                except:
                    continue
                run_hashcat(i,empty,hash_type)
                if alert < power:
                    time.sleep(runed)
                break

if __name__=="__main__":
    main()
