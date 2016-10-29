#!/usr/bin/env python
import os
import sys

src = open(sys.argv[1],"r")
md5 = open(sys.argv[2],"r")
bcr = open(sys.argv[3],"r")
dst = open(sys.argv[4],"w")

md5_t = md5.readline()
bcr_t = bcr.readline()
for i in src.readlines():
    if i[1] != "2":
        #md5
        dst.write(md5_t[:md5_t.find(":",35)])
        dst.write("\n")
        md5_t = md5.readline()
    else:
        #bcr
        dst.write(bcr_t[:bcr_t.find(":",61)])
        dst.write("\n")
        bcr_t = bcr.readline()


