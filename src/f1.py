#!/usr/bin/env python
import os
import sys
import re

port_num = sys.argv[1]
lock_num = sys.argv[2]

is_file = re.compile("^[tlpcb]:\d+:\d+:\d+:\d+$").match
is_tocr = re.compile("^t:\d+:\d+:\d+:\d+$").match
is_lock = re.compile("^l:\d+:\d+:\d+:\d+$").match

get_min = lambda x:int(x.split(":")[1])

def init():
    data = os.listdir("pool")
    data.sort(key=get_min)
    for i in data[:lock_num]:
        os.rename("pool/%s"i,"pool/l%s"i[1:])

def query_one():
    data = os.listdir("pool")
    lock = filter(is_lock,data)
    tocr = filter(is_tocr,data)
    ltop = min(lock,key=get_min)
    ttol = min(tocr,key=get_min)
    os.rename("pool/%s"%ttol,"pool/l%s"%ttol[1:])
    os.rename("pool/%s"%ltop,"pool/p%s"%ltop[1:])
    return ltop

def application(environ, start_response):
    query = environ["QUERY_STRING"]
    if query == "query":
        return query_one()
    else:
        os.rename("pool/p%s"%query[1:],"pool/%s"query)
        return ""

init()
from wsgiref.simple_server import make_server
httpd = make_server('', int(port_num), application)
httpd.serve_forever()
