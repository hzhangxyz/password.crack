def readfile(filename):
    with open(filename,"r") as f:
        d=set(f.read().split("\n"))
    return d

def writefile(filename,data):
    date = sortlist(data)
    with open(filename,"w") as f:
        for i in data:
            f.write(i)
            f.write("\n")
    return 0

def sortlist(n):
    d=list(n)
    d.sort(key=len)
    return d

def split(inl,nums):
    l = sortlist(inl)
    d = []
    ll = len(l)
    for i in range(nums):
        d.append(l[i*ll/nums:(i+1)*ll/nums])
    return d

def spliter(inf,nums):
    i = readfile(inf)
    d = split(i,nums)
    for i,j in enumerate(d):
        writefile("%s.%d"%(inf,i),j)

import re
def filt(x,y):
    xx = re.compile(x)
    return filter(xx.match,y)

patterns = [
        "^[a-z]+$",
        "^[A-Z]+$",
        "^[A-Z][a-z]+$",
        "^[A-Z][a-z]+[A-Z][a-z]+$",

        "^[0-9]+$",
        "^[A-Z]+[0-9]$",
        "^[a-z]+[0-9]$",
        "^[A-Z][a-z]+[0-9]$",
        "^[a-z]+[0-9]{2}$",
        "^[A-Z][a-z]+[0-9]{2}",
        "^[a-z]+[0-9]{3}$",
        "^[A-Z][a-z]+[0-9]{3}",
        "^[a-z]+[0-9]{4}$",
        "^[A-Z][a-z]+[0-9]{4}",
        "^[a-z]+[0-9]{5}$",

        "^[0-9][a-z]+$",
        "^[0-9]{2}[a-z]+$",
        "^[0-9]{4}[a-z]+$",

        "^[a-z]+ [a-z]+$",
        "^[A-Z][a-z]+ [A-Z][a-z]+$",
        "^[A-Z]+ [A-Z]+$",

        "^[a-z]+_[a-z]+$",
        "^[A-Z][a-z]+_[A-Z][a-z]+$",
        "^[A-Z]+_[A-Z]+$",

        "^[a-z]+'[a-z]+$",
        "^[a-z]+,[a-z]+$",
        "^[a-z]+'$",
        "^[a-z]+ [a-z]+ [a-z]+$",
        "^[a-z]+-[a-z]+$",
        "^[a-z]+\.[a-z]+$",

        "^[a-z]+!$",
        "^[A-Z]+!$",
        "^[a-z]+!!$",
        "^[A-Z]+!!$",
        "^[A-Z][a-z]+!$",
        "^[A-Z][a-z]+!!$",

        "^[a-z][0-9]+$",
        "^[a-z]{2}[0-9]+$",
        "^[A-Z][0-9]+$",
        "^[A-Z]{2}[0-9]+$",

        "^[0-9]+[a-z]$",
        "^[0-9]+[a-z]{2}$",
        "^[0-9]+[A-Z]$",
        "^[0-9]+[A-Z]{2}$",

]


def ana(filename):
    print("[%s]"%filename)
    d = readfile(filename) - set([""])
    print("%d\ttotal"%len(d))
    nums = [filt(i,d) for i in patterns]
    for i in range(len(patterns)):
        print("%d\t%s"%(len(nums[i]),patterns[i]))
        d -= set(nums[i])
    print("%d\tother"%len(d))
    print("")
    return d

import sys

if __name__ == "__main__":
    writefile("%s.other"%sys.argv[1],ana(sys.argv[1]))
