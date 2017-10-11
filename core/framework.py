# -*- coding: utf-8 -*-

"""
Copyright (c) 2017 hualala Security (https://www.hualala.com)
author wenzhaowei[at]hualala.com
"""
import Queue
import threading
import glob
import sys
sys.path.append('plugins')
from core.utils.logging import logging
logging = logging()

class framework():
    def __init__(self,targets,plugins=''):
        self.thread = 10
        self.targets = targets
        self.plugins = plugins
        self.result = list()

    def exploit(self):
        # 插件导入
        self.plugins = glob.glob('plugins/*.py') if (self.plugins=='') else ["plugins\\"+self.plugins+'.py']
        for tar in self.targets:
            for p in self.plugins:
                try:
                    pname = p[8:-3]
                    logging.INFO('check target [%s] with plugins [%s]' % (tar,pname))
                    plugin_item = getattr(__import__(pname), "Exploit")
                    rs = plugin_item(tar)
                    rs.verify()
                    if rs.result['status']:
                        logging.WARNING(rs.result['info'])
                        self.result.append([tar,pname,rs.result['status'],rs.result['info']])
                except Exception as identifier:
                    logging.ERROR('import plugins [ %s ] error' % pname)
                    logging.ERROR('Hscan will exit thread[s] , please check plugins')
                    print identifier
                    exit()

        logging.INFO('all target[s] is done , check result with output')
