#!/usr/bin/env python
import os
import sys
import re

port_num  = sys.argv[1]
lock_num  = sys.argv[2]
fold_name = sys.argv[3]
hash_file = sys.argv[4]

is_file    = re.compile("^[tlpcb]:\d+:\d+:\d+$").match
is_tocrack = re.compile("^t:\d+:\d+:\d+$").match
is_locked  = re.compile("^l:\d+:\d+:\d+$").match

get_min = lambda x:int(x.split(":")[1])

def change_status(fold_name,name,status):
    os.rename(os.path.join(fold_name,name),os.path.join(fold_name,"%s%s"%(to_status,name[1:])))

def init():
    data    = filter(is_file,os.listdir(fold_name))
    tocrack = filter(is_tocrack,data)
    locked  = filter(is_locked,data)
    tocrack.sort(key=get_min)
    to_add_num = int(lock_num)-len(locked)
    if to_add_num > 0:
        for i in tocrack[:int(lock_num)-len(locked)]:
            change_status(fold_name,i,"l")

def query_one():
    init()
    locked = filter(is_locked,os.listdir(fold_name))
    to_run = min(locked,key=get_min)
    change_status(fold_name,ltop,"p")
    init()
    return to_run

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    query = environ["QUERY_STRING"]
    if query == "query":
        return "%s:%s"%(hash_file,query_one())
    else:
        os.rename("%s/p%s"%(fold_name,query[1:]),"%s/%s"%(fold_name,query))
        return ""

init()
from wsgiref.simple_server import make_server
httpd = make_server('', int(port_num), application)
httpd.serve_forever()
