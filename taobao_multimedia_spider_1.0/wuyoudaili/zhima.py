# coding=utf-8
import re
import time
import json
import random
import requests
from multiprocessing.dummy import Pool
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


# def change_ip(self):
#     new_sec = time.time()
#     self.sec = new_sec - self.old_sec
#     if self.sec > 5:
#         # 获取IP的API接口
#         apiUrl = "http://webapi.http.zhimacangku.com/getip?num=1&type=1&pro=440000&city=0&yys=0&port=1&time=1&ts=0&ys=0&cs=0&lb=4&sb=0&pb=4&mr=2&regions="
#         self.old_sec = time.time()
#         res = requests.get(apiUrl).text
#         ips = res.split("\n")[0]
#         self.proxy = {"http": ips}
#         print self.proxy
#     else:
#         self.proxy = self.proxy


def change_ip():

    # 获取IP的API接口
    apiUrl = "http://webapi.http.zhimacangku.com/getip?num=1&type=1&pro=440000&city=0&yys=0&port=1&time=1&ts=0&ys=0&cs=0&lb=4&sb=0&pb=4&mr=2&regions="
    old_sec = time.time()
    res = requests.get(apiUrl).text
    ips = res.split("\n")[0]
    proxy = {"http": ips}
    print proxy


change_ip()