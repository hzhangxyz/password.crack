#!usr/bin/env python
import sys
import os
import subprocess

data       = subprocess.check_output('curl "127.0.0.1:2435/?query"',shell=True)
hash_type  = sys.argv[1] # "m" or "b"
work_dir   = sys.argv[2]
ans_file   = sys.argv[3]
hash_file  = data[:data.find(":")]
dict_file  = data[1+data.find(":"):]
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

this_hash = "this.hash"
this_dict = "this.dict"

ans_file_point  = open(ans_file,"r")
hash_file_point = open(hash_file,"r")
this_hash_point = open(this_hash,"w")

hash_file_point.seek(hash_slices[0]*(hash_length+1))

ans_file_point.seek((1+hash_ans_l)*hash_slices[0]+hash_length+1)
for i in range(hash_slices[1]-hash_slices[0]):
    to_write = hash_file_point.readline()
    if ans_file_point.read(1)==":":
        this_hash_point.write(to_write)
    ans_file_point.seek(hash_ans_l,1)

hash_file_point.close()
this_hash_point.close()

os.system("cp %s this.dict"%os.path.join(work_dir,"p%s"%dict_file[1:]))

to_run = "./hashcat -a 0 -m %d %s %s"%(hash_id,this_hash,this_dict)
print to_run
os.system(to_run)


