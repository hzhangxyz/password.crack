#!/usr/bin/env python
import os
pool = os.path.join(os.environ["CLIENTDIR"],"pool")
pools = filter(lambda x:x[:7]=='client_', os.listdir(pool))
for i in pools:
    pid = os.path.join(pool,i,"pid")
    if os.path.isfile(pid):
        with open(pid,"r") as f:
            d = f.read().split("\n")
        if len(d) == 1:
            continue
        print i,"###CURL###",d[1]
        os.system("curl %s"%d[1])
