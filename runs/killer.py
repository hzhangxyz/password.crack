#!/usr/bin/env python
VERYDANGER = 1500

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
    return max(m)

def main():
    n = power_now()
    if flag:
        if n > VERYDANGER:
            killer = "kill -2 `ps aux | grep starter.py | grep -v grep | awk '{printf $2}'` &"
            print killer
            os.system(killer)
            os.system(killer)
            os.system("ssh node1 killall -9 hashcat &")
            os.system("ssh node2 killall -9 hashcat &")
            os.system("ssh node3 killall -9 hashcat &")
            os.system("ssh node4 killall -9 hashcat &")
        a = len(check_output("ssh node1 nvidia-smi | awk '/hashcat/{printf $2\" \"}'",shell=True).split())
        b = len(check_output("ssh node2 nvidia-smi | awk '/hashcat/{printf $2\" \"}'",shell=True).split())
        c = len(check_output("ssh node3 nvidia-smi | awk '/hashcat/{printf $2\" \"}'",shell=True).split())
        d = len(check_output("ssh node4 nvidia-smi | awk '/hashcat/{printf $2\" \"}'",shell=True).split())
        print n,a,b,c,d
    else:
        with open(argv[1],"a") as f:
            f.write("%s %s\n"%(check_output("date +%s",shell=True)[:-1], n))

while True:
    main()
