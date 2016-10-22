#!/usr/bin/env python
import os
import sys
import re

port_num = sys.argv[1]
lock_num = sys.argv[2]
fold_nam = sys.argv[3]

is_file = re.compile("^[tlpcb]:\d+:\d+:\d+$").match
is_tocr = re.compile("^t:\d+:\d+:\d+$").match
is_lock = re.compile("^l:\d+:\d+:\d+$").match

get_min = lambda x:int(x.split(":")[1])

def init():
    data = filter(is_file,os.listdir(fold_nam))
    data.sort(key=get_min)
    for i in data[:int(lock_num)]:
        os.rename("%s/%s"%(fold_nam,i),"%s/l%s"%(fold_nam,i[1:]))

def query_one():
    data = os.listdir(fold_nam)
    lock = filter(is_lock,data)
    tocr = filter(is_tocr,data)
    ltop = min(lock,key=get_min)
    ttol = min(tocr,key=get_min)
    os.rename("%s/%s"%(fold_nam,ttol),"%s/l%s"%(fold_nam,ttol[1:]))
    os.rename("%s/%s"%(fold_nam,ltop),"%s/p%s"%(fold_nam,ltop[1:]))
    return ltop

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    query = environ["QUERY_STRING"]
    if query == "query":
        return query_one()
    else:
        os.rename("%s/p%s"%(fold_nam,query[1:]),"%s/%s"%(fold_nam,query))
        return ""

init()
from wsgiref.simple_server import make_server
httpd = make_server('', int(port_num), application)
httpd.serve_forever()
