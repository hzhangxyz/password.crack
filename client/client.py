#!/usr/bin/env python
import sys
import os
import urllib
import shutil
import tempfile

hash_type = sys.argv[1]

if hash_type[0] == "m":
    scatter  = os.environ["MD5SCATTER"]
    gather   = os.environ["MD5GATHER"]
    dict_dir = os.environ["MD5POOL"]
    ans_file = "%s.md5.cracked"%os.environ["HASH"]
else:
    scatter  = os.environ["BCRSCATTER"]
    gather   = os.environ["BCRGATHER"]
    dict_dir = os.environ["BCRPOOL"]
    ans_file = "%s.bcr.cracked"%os.environ["HASH"]

server     = os.environ["PASSWDSERVER"]
hashcat    = os.environ["HASHCATADDR"]
hcflag     = os.environ["HASHCATFLAG"]
dvcflag    = os.environ["DEVICEFLAG"]

def urlget(n):
    c = urllib.urlopen(n)
    d = c.readline()
    c.close()
    return d

query      = urlget("http://%s:%s/?query"%(server,scatter))

prefix = tempfile.mkdtemp(prefix="crack_",dir=os.path.curdir)

with open(os.path.join(prefix,'pid'),'w') as pid:
    pid.write(str(os.getpid()))
    pid.write('\n')
    pid.write(query)

hash_file  = query[:query.find(":")]
dict_file  = query[1+query.find(":"):]
hash_slice = dict_file[1+dict_file.find(":",1+dict_file.find(":")):]

hash_slices = map(int,hash_slice.split(":"))

dict_length = 36

if hash_type[0] == "m":
    hash_id     = 500
    hash_length = 34
else:
    hash_id     = 3200
    hash_length = 60

hash_ans_l = hash_length + dict_length + 1

this_hash = os.path.join(prefix,"hash")
this_dict = os.path.join(prefix,"this.dict")
this_pot  = os.path.join(prefix,"this.pot")

ans_file_point  = open(ans_file,"r")
hash_file_point = open(hash_file,"r")
this_hash_point = open(this_hash,"w")

hash_file_point.seek(hash_slices[0]*(1+hash_length))
ans_file_point.seek(hash_slices[0]*(1+hash_ans_l)+hash_length+1)

for i in range(hash_slices[1]-hash_slices[0]):
    to_write = hash_file_point.readline()
    if ans_file_point.read(1)==":":
        this_hash_point.write(to_write)
    ans_file_point.seek(hash_ans_l,1)

ans_file_point.close()
hash_file_point.close()
this_hash_point.close()

shutil.copyfile(os.path.join(dict_dir,"p%s"%dict_file[1:]),this_dict)

hashcat_run = "%s %s %s --hash-type %d --potfile-path %s %s %s"%(hashcat,hcflag,dvcflag,hash_id,this_pot,this_hash,this_dict)
print hashcat_run
os.system(hashcat_run)

urlget("http://%s:%s/?c%s"%(server,scatter,dict_file[1:]))
urlget("http://%s:%s/?%s:%s"%(server,gather,os.path.join(os.path.abspath(os.curdir),this_pot),hash_slice))

os.remove(os.path.join(prefix,'pid'))

