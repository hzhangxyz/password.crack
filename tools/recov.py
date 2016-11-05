#!/usr/bin/env python
nodes = ["node2","node3"]

import os
pool = os.path.join(os.environ["CLIENTDIR"],"pool")
pools = filter(lambda x:x[0]=='p', os.listdir(pool))
for i in pools:
    pid = os.path.join(pool,i,"pid")
    if os.path.isfile(pid):
        with open(pid,"r") as f:
            d = f.read().split("\n")
        flag = True
        for j in nodes:
            if os.system("ssh %s ps -p %s"%(j,d[0]))==0:
                flag = False
        if flag:
            os.system(d[1])


