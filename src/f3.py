#!usr/bin/env python
import sys
import os

hash_type  = sys.argv[1] # "m" or "b"
hash_file  = sys.argv[2] # file name
hash_slice = sys.argv[3] # sth like 0:1000
dict_file  = sys.argv[4]
dict_slice = sys.argv[5]

hash_slices = map(int,hash_slice.split(":"))
dict_slices = map(int,dict_slice.split(":"))

if hash_type[0] == "m":
    hash_id     = 500
    hash_length = 35
else:
    hash_id     = 3200
    hash_length = 61

hash_position = [i*hash_length for i in hash_slices]
dict_position = [i*dict_legnth for i in dict_slices]

#get the file based on slice

this_hash = "this.hash"
this_dict = "this.dict"

os.system("./hashcat -m %d %s %s"%(hash_id,this_hash,this_dict))
