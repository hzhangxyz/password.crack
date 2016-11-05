#!/usr/bin/env python
from socketIO_client import SocketIO, LoggingNamespace
from subprocess import check_output
from time import sleep
from sys import argv, stdout
import os

m = "0"

def p(n):
    global m
    m = n

flag = len(argv) == 1

socketIO = SocketIO('localhost', 8800, LoggingNamespace)
socketIO.on('power', p)

def power_now():
    socketIO.wait(seconds=1)
    global m
    return m

def main():
    if flag:
        n = 22.5*float(power_now())
        if n > 2950:
            os.system("kill -2 `ps aux | grep arr | grep -v grep | awk '{printf $2}'`")
            os.system("kill -2 `ps aux | grep arr | grep -v grep | awk '{printf $2}'`")
            os.system("pfornode killall -9 hashcat")
        a = len(check_output("ssh node2 nvidia-smi | awk '/hashcat/{printf $2\" \"}'",shell=True).split())
        b = len(check_output("ssh node3 nvidia-smi | awk '/hashcat/{printf $2\" \"}'",shell=True).split())
        print "%f\t%d\t%d"%(n,a,b)
    else:
        with open(argv[1],"a") as f:
            f.write("%s %f\n"%(check_output("date +%s",shell=True)[:-1], 22.5*float(m)))

while True:
    main()
