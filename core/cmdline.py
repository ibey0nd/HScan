# -*- coding: utf-8 -*-

"""
Copyright (c) 2017 hualala Security (https://www.hualala.com)
author wenzhaowei[at]hualala.com
"""
import sys
import argparse


def parse_args():
    parser = argparse.ArgumentParser(prog='HScan',
                                     formatter_class=argparse.RawTextHelpFormatter,
                                     description='* A plugins weB vulnerability Scanner. *\n'
                                                 'Author : bey0nd [at] (http://www.itwzw.cn)',
                                     usage='HScan.py [options]')

    parser.add_argument('-u', metavar='HOST [HOST2 HOST3 ...]', type=str, default='', nargs='*',
                        help='Scan several url from command line')

    parser.add_argument('-f', metavar='TargetFile', type=str, default='',
                        help='Load new line delimited targets from TargetFile')

    parser.add_argument('-p',"--plugins", metavar='', type=str, default='', help='Load plugins from TargetDirectory')

    parser.add_argument("-cookie", metavar='name=value', type=str, default='', help='HTTP cookies for Target')

    if(len(sys.argv))==1:
        sys.argv.append('-h')
    argv = parser.parse_args()
    return argv

def banner():
    banner = ''' _    _   _____                    
| |  | | / ____|                   
| |__| || (___    ___  __ _  _ __  
|  __  | \___ \  / __|/ _` || '_ \ 
| |  | | ____) || (__| (_| || | | |
|_|  |_||_____/  \___|\__,_||_| |_|
                                plugins weB vulnerability Scanner 
                          bey0nd [at] (http://www.itwzw.cn)
'''
    print banner