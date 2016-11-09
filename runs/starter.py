#!/usr/bin/env python

# parameter
dd = 100 # starter gate
dg = 70  # dangerous gate
totalpower = 3000
nodes = ["node2", "node3"]
md5 = {"node2":200, "node3":300}
bcr = {"node2":150, "node3":200}
gpu_available = {"node2":[1,2,3,4,5,6,7,8], "node3":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]}
sec = 5
runed = 25
hash_type = "m"

# import
import urllib
import subprocess
import time
import os
from socketIO_client import SocketIO, LoggingNamespace
import signal
import threading

# constant
ddd = 2*max(max(md5.values()),max(bcr.values()))
maximum = totalpower - dd
dangerp = totalpower - dg
alert = maximum - ddd
clientdir = os.environ["CLIENTDIR"]
tooldir = os.environ["TOOLDIR"]

# SIGINT
def handler(signal_num,frame):
    try:
        raw_input()
    except:
        for i in nodes:
            os.system("ssh %s killall -9 hashcat &"%i)
    exit()

# get PDU
def p(n):
    global m
    m = 22.5*float(n)

def power_now():
    global m
    socketIO.wait(seconds=1)
    print "POWER new", m
    return int(m)

# get hashcat
def get_hashcat_now(node):
    try:
        return map(lambda x:int(x)+1,subprocess.check_output("ssh %s nvidia-smi | awk '/hashcat/{printf $2\"\\n\"}'"%node,shell=True).split())
    except:
        return gpu_available[node]

# kill hashcat

def kill_hashcat(nodes,gpu):
    to_run = "ssh %s nvidia-smi | awk '/hashcat/{printf $2 \" \" $3 \"\\n\"}'"%nodes
    s = subprocess.check_output(to_run,shell=True).split()
    d = {s[2*i]:s[2*i+1] for i in range(len(s)/2)}[str(gpu-1)]
    to_run = "ssh %s kill -9 %s"%(nodes,d)
    print "KILL",to_run
    os.system(to_run)

# run hashcat
def run_hashcat(node,gpu,hash_type):
    to_run = "ssh %s 'source %s; export DEVICEFLAG=\"-d %s\";%s %s' 1>/dev/null 2>&1&"%(\
        node,\
        os.path.join(tooldir,"env.conf"),\
        str(gpu),\
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
                    print "WAIT",runed,"s since power >",alert
                    time.sleep(runed)
                break
            else:
                print "NO more power for",hash_type,"of",i,":",times[i]

def  mon():
    while True:
        if power_now() > dangerp:
            gpus = [[i,get_hashcat_now(i)] for i in nodes]
            gpus.reverse()
            while power_now() > dangerp:
                for i in gpus:
                    if i[1]:
                        kill_hashcat(i[0],i[1].pop())
                        break
            continue

if __name__=="__main__":
    global sockerIO
    socketIO = SocketIO('localhost', 8800, LoggingNamespace)
    socketIO.on('power', p)
    signal.signal(signal.SIGINT, handler)
    t1 = threading.Thread(target=main)
    t2 = threading.Thread(target=mon)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
