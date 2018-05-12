#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '
__author__ = 'LIUYI'

def application(environ,start_response):
    start_response('200 OK',[('content-Type','text/html')])
    return [b'<h1>hello web</h1>']