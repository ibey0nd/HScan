# -*- coding: utf-8 -*-

"""
Copyright (c) 2017 hualala Security (https://www.hualala.com)
author wenzhaowei[at]hualala.com
"""
from core.framework import framework
from core.utils.PrettyTable import PrettyTable
from core.cmdline import parse_args, banner

if __name__ == '__main__':
    banner()
    argv = parse_args()
    
    h = framework(argv.u,plugins=argv.plugins)
    h.exploit()
    x = PrettyTable(["url", "plugins", "success",'info'])
    for item in h.result:
        x.add_row(item)
    print(x)
    print 'success : %s' % len(h.result)
    