#!/usr/bin/env python
import os
import sys

hash_type    = sys.argv[1]
cracked_file = sys.argv[2]
port_num     = sys.argv[3]

def application(environ, start_response):
    file_name,start_id,end_id = environ["QUERY_STRING"].split(":")

    start_response('200 OK', [('Content-Type', 'text/plain')])
    return ""


from wsgiref.simple_server import make_server
httpd = make_server('', int(port_num), application)
httpd.serve_forever()
