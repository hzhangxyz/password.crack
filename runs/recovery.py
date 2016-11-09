#!/usr/bin/env python
import os
nodes = ["node2","node3"]
pool = os.path.join(os.environ["CLIENTDIR"],"pool")
pools = filter(lambda x:x[:7]=='client_', os.listdir(pool))
for i in pools:
    pid = os.path.join(pool,i,"pid")
    if os.path.isfile(pid):
        with open(pid,"r") as f:
            d = f.read().split("\n")
        try:
            print "PID",d[0]
            print "URLS",d[1]
        except:
            print ""
            continue
        j = d[0].split(" ")
        if os.system("ssh %s ps -p %s 1>/dev/null 2>/dev/null"%(j[0],j[1]))
            print "Process Exist"
        else:
            print "Process Not Exist"
            print "###CURL###",d[1]
            os.system("curl %s"%d[1])
