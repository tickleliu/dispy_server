# -*- coding:utf-8 -*-
""" 
@author:mlliu
@file: host.py 
@time: 2018/07/17 
"""

import sys
import os
import socket

myname = socket.getfqdn(socket.gethostname())
myaddr = socket.gethostbyname(myname)
shell = "/home/liuml/anaconda3/envs/tfgpu/bin/python /home/liuml/anaconda3/envs/tfgpu/bin/dispynode.py -c 2 -i %s -s secret --clean --daemon"
os.system(shell % myaddr)
