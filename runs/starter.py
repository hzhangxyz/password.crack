#!/usr/bin/env python

# parameter
dd = 300 # starter gate
dg = 200  # dangerous gate
totalpower = 3000
nodes = ["node1", "node2", ]
md5 = {"node1":200, "node2":200, "node3":200, "node4":200}
bcr = {"node1":200, "node2":200, "node3":200, "node4":200}
gpu_available = {"node1":[1,2,3,4,5], "node2":[1,2,3,4,5], "node3":[1,2,3,4], "node4":[1,2,3,4]}
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
    exit()

# get PDU
def p(n):
    global m
    m = sum(n)

def power_now():
    try:
        global m
        socketIO.wait(seconds=1)
        print "POWER new", m
        if m > dangerp:
            gpus = [[i,get_hashcat_now(i)] for i in nodes]
            gpus.reverse()
            while m > dangerp:
                for i in gpus:
                    if i[1]:
                        print "KILLING"
                        kill_hashcat(i[0],i[1].pop())
                        print "KILLED ONE in %s"%i[0]
                        socketIO.wait(seconds=0.2)
                        break
        return m
    except:
        return totalpower

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

if __name__=="__main__":
    global sockerIO
    socketIO = SocketIO('localhost', 8800, LoggingNamespace)
    socketIO.on('power', p)
    signal.signal(signal.SIGINT, handler)
    main()
