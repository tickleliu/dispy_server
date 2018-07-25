# -*- coding:utf-8 -*-
""" 
@author:mlliu
@file: fabfile.py.py 
@time: 2018/07/17 
"""

from fabric.api import env
from fabric.api import sudo, run

ip = "10.0.0.243, 10.0.0.241"
port = [22, 22]
env.hosts = [

    "liuml@10.0.0.227:22",
    "liuml@10.0.0.228:22",
    "liuml@10.0.0.229:22",
    "liuml@10.0.0.232:22",
    "liuml@10.0.0.233:22",
    "liuml@10.0.0.243", "liuml@10.0.0.241", "liuml@10.0.0.242", "liuml@10.0.0.244"]
env.passwords = {
    "liuml@10.0.0.227:22": "123456",
    "liuml@10.0.0.228:22": "123456",
    "liuml@10.0.0.229:22": "123456",
    "liuml@10.0.0.232:22": "123456",
    "liuml@10.0.0.233:22": "123456",
    "liuml@10.0.0.241:22": "123456",
    "liuml@10.0.0.242:22": "1234",
    "liuml@10.0.0.243:22": "123456",
    "liuml@10.0.0.244:22": "1234",
}

env.user = "liuml"


def dispynode():
    run("/home/liuml/anaconda3/envs/tfgpu/bin/python /home/liuml/workspace/dispydemo/host.py")
