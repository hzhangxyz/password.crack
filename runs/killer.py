#!/usr/bin/env python
VERYDANGER = 2950
VERYDANGER = 1100

from socketIO_client import SocketIO, LoggingNamespace
from subprocess import check_output
from time import sleep
from sys import argv, stdout
import os

flag = len(argv) == 1

def p(n):
    global m
    m = n

socketIO = SocketIO('localhost', 8800, LoggingNamespace)
socketIO.on('power', p)

def power_now():
    socketIO.wait(seconds=1)
    global m
    return sum(m)

def main():
    n = power_now()
    if flag:
        if n > VERYDANGER:
            killer = "kill -2 `ps aux | grep auto.py | grep -v grep | awk '{printf $2}'` &"
            print killer
            os.system(killer)
            os.system(killer)
            os.system("ssh node1 killall -9 hashcat &")
            os.system("ssh node2 killall -9 hashcat &")
        a = len(check_output("ssh node1 nvidia-smi | awk '/hashcat/{printf $2\" \"}'",shell=True).split())
        b = len(check_output("ssh node2 nvidia-smi | awk '/hashcat/{printf $2\" \"}'",shell=True).split())
        print "%s\t%d\t%d"%(n,a,b)
    else:
        with open(argv[1],"a") as f:
            f.write("%s %s\n"%(check_output("date +%s",shell=True)[:-1], n))

while True:
    main()
