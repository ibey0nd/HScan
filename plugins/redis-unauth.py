# -*- coding: utf-8 -*-

"""
Copyright (c) 2017 hualala Security (https://www.hualala.com)
author wenzhaowei[at]hualala.com
"""

import socket
from core.utils.funs import url2ip
class Exploit:
    def __init__(self,target):
        self.target = target
        self.result = {
            "name": "Redis未授权访问",
            "author": "bey0nd",
            "type": "server",
            "status":False,
            "info":"",
            "target":target,
        }
    def verify(self):
        s = socket.socket()
        payload = '\x2a\x31\x0d\x0a\x24\x34\x0d\x0a\x69\x6e\x66\x6f\x0d\x0a'
        socket.setdefaulttimeout(5)
        try:
            host = url2ip(self.target)
            port = 6379
            s.connect((host, port))
            s.send(payload)
            recvdata = s.recv(1024)
            if recvdata and 'redis_version' in recvdata:
                self.result['status'] = True
                self.result['info'] = '%s redis [%s] is unauth' % (host,port)
        except Exception,e:
            pass
        s.close()
       