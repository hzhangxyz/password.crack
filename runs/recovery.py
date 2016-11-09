#!/usr/bin/env python
import os
nodes = ["node2","node3"]
pool = os.path.join(os.environ["CLIENTDIR"],"pool")
pools = filter(lambda x:x[0]=='p', os.listdir(pool))
for i in pools:
    pid = os.path.join(pool,i,"pid")
    if os.path.isfile(pid):
        with open(pid,"r") as f:
            d = f.read().split("\n")
        flag = True
        try:
            print "PID",d[0]
            print "URLS",d[1]
        except:
            print ""
            continue
        for j in nodes:
            if os.system("ssh %s ps -p %s 1>/dev/null 2>/dev/null"%(j,d[0]))==0:
                print "Process Exist"
                flag = False
        if flag:
            print "Process Not Exist"
            print "###CURL###",d[1]
            os.system("curl %s"%d[1])
