def f_filter(inf,outf,f):
    with open(inf,"r") as f:
        d=f.read()
    d=d.split('\n')
    d=filter(f,d)
    d="\n".join(d)
    with open(outf,"w") as f:
        f.write(d)

def f_minus(a,b,c):
    with open(a,"r") as aaa,open(b,"r") as bbb:
        aa=aaa.read().split("\n")
        bb=bbb.read().split("\n")
    aa=set(aa)
    bb=set(bb)
    cc=aa-bb
    dd="\n".join(map(str,cc))
    with open(c,"w") as f:
        f.write(dd)

def f_sort(inf,outf):
    with open(inf,"r") as f:
        d=f.read().split("\n")
    d=list(set(d))
    d.sort(key=len)
    d="\n".join(d)
    with open(outf,"w") as f:
        f.write(d)

def f_split(inf,outf):
    with open(inf,"r") as f:
        d=f.read().split("\n")
    outff = [open(i,"w") for i in outf]
    m = len(outf)
    n = len(d)
    for i in xrange(n):
        outff[i%m].write(d[i])
        outff[i%m].write("\n")
    [i.close() for i in outff]

