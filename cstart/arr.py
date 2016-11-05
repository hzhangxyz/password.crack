#!/usr/bin/env python

# parameter
dd = 100 # sum of var and threshold
maximum = 3000 - dd
nodes = ["node2", "node3"]
md5 = {"node2":200, "node3":300}
bcr = {"node2":200, "node3":300}
gpu_available = {"node2":[1,2,3,4,5,6,7,8], "node3":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]}
sec = 5
runed = 25
hash_type = "b"

# import
import urllib
import subprocess
import time
import os
from socketIO_client import SocketIO, LoggingNamespace
import signal

# constant
ddd = 2*max(max(md5.values()),max(bcr.values()))
alert = maximum - ddd - dd
clientdir = os.environ["CLIENTDIR"]

# SIGINT
def handler(signal_num,frame):
    try:
        raw_input()
    except:
        os.system("pfornode killall -9 hashcat")
    exit()

signal.signal(signal.SIGINT, handler)

# get PDU
def p(n):
    global m
    m = 22.5*float(n)

socketIO = SocketIO('localhost', 8800, LoggingNamespace)
socketIO.on('power', p)

def power_now():
    global m
    socketIO.wait(seconds=1)
    print "POWER new", m
    return int(m)

# get hashcat
def get_hashcat_now(n):
    try:
        return map(lambda x:int(x)+1,subprocess.check_output("ssh %s nvidia-smi | awk '/hashcat/{printf $2\"\\n\"}'"%n,shell=True).split())
    except:
        return gpu_available[n]

# run hashcat
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

# main
def main():
    while True:
        power = [power_now() for i in range(sec)]
        power=max(power)
        delta = maximum - power
        print "STATE","max",maximum,"delta",delta
        for i in nodes:
            times = md5 if hash_type == "m" else bcr
            if delta > times[i]:
                print "STATE","delta",delta,">","times[",i,"]",times[i]
                try:
                    now_hashcat = get_hashcat_now(i)
                    empty = (set(gpu_available [i]) - set(now_hashcat)).pop()
                    print "FIND gpu",empty,"in",gpu_available[i],"-",now_hashcat
                except:
                    print "NO available gpu"
                    continue
                run_hashcat(i,empty,hash_type)
                if alert < power:
                    print "WAIT ",runed,"s since power >",alert
                    time.sleep(runed)
                break
            else:
                print "NO more power for",hash_type,"of",i,":",times[i]

if __name__=="__main__":
    main()