def filter(inf,f):
    outf=inf
    with open(inf,"r") as f:
        d=f.read()
    d=d.split('\n')
    d=filter(f,d)
    d="\n".join(d)
    with open(outf,"w") as f:
        f.write(d)

def minus(a,b):
    c=a
    with open(a,"r") as aaa,open(b,"r") as bbb:
        aa=aaa.read().split("\n")
        bb=bbb.read().split("\n")
    aa=set(aa)
    bb=set(bb)
    cc=aa-bb
    dd="\n".join(map(str,cc))
    with open(c,"w") as f:
        f.write(dd)

def sort(inf):
    outf=inf
    with open(inf,"r") as f:
        d=f.read().split("\n")
    d=list(set(d))
    d.sort(key=len)
    d="\n".join(d)
    with open(outf,"w") as f:
        f.write(d)

def split(inf,outf):
    if isinstance(outf, int):
        outf = ["%s.%d"%(inf,i) for i in range(outf)]
    with open(inf,"r") as f:
        d=f.read().split("\n")
    outff = [open(i,"w") for i in outf]
    m = len(outf)
    n = len(d)
    for i in xrange(n):
        outff[i%m].write(d[i])
        outff[i%m].write("\n")
    [i.close() for i in outff]

import os
def copy(intf,num,startid,beginner,ender):
    length = (ender - beginner)/num
    for i in range(num):
        n = "t:%d:%d:%d"%((i+startid),(beginner + length*i),(beginner + length*(i+1)))
        os.system("ln -s %s %s"%(intf,n))

#

