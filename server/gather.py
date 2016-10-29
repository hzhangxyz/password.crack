#!/usr/bin/env python
import os
import sys

hash_type    = sys.argv[1]

dict_length  = 36

if hash_type[0] == "m":
    hash_id     = 500
    hash_length = 34
    port_num    = os.environ["MD5GATHER"]
    cracked_file = "%s.md5.cracked"%os.environ["$HASH"]
else:
    hash_id     = 3200
    hash_length = 60
    port_num    = os.environ["BCRGATHER"]
    cracked_file = "%s.bcr.cracked"%os.environ["$HASH"]

hash_ans_l = hash_length + dict_length + 1

def insert_single(ans_file,to_insert,start_id,end_id):
    ans_pointer = open(ans_file,"r+")
    ans_pointer.seek((1+hash_ans_l)*start_id)
    for i in xrange(end_id-start_id):
        to_check = ans_pointer.readline()
        if to_check[:hash_length] == to_insert[:hash_length]:
            ans_pointer.seek(-hash_ans_l-1,1)
            ans_pointer.write(to_insert[:-1])
            ans_pointer.close()
            break
    ans_pointer.close()

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    file_name,start_id,end_id = environ["QUERY_STRING"].split(":")
    start_id = int(start_id)
    end_id   = int(end_id)
    pot = open(file_name,"r")
    for i in pot.xreadlines():
        if i != "":
            insert_single(cracked_file,i,start_id,end_id)
    return ""


from wsgiref.simple_server import make_server
httpd = make_server('', int(port_num), application)
httpd.serve_forever()
