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
        socket.setdefaulttimeout(5)
        try:
            host = url2ip(self.target)
            port = 6379
            s.connect((host, port))
            self.result['status'] = True
            self.result['info'] = '%s port [%s] is open' % (self.target,port)
        except Exception,e:
            pass
        s.close()
       