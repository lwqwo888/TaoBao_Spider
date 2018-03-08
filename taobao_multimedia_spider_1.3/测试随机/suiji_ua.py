# coding=utf-8
# 免责声明: 此代码是为快捷查询由刘文强编写的
import re
import json
import time
import random
import datetime
import requests
import linecache
from lxml import etree
import sys
reload(sys)
sys.setdefaultencoding('utf-8')



s_time = time.time()
# 要访问的目标页面
targetUrl = "http://httpbin.org/ip"

# 代理服务器
proxyHost = "t.16yun.cn"
proxyPort = "31111"

# 代理隧道验证信息
proxyUser = "username"
proxyPass = "password"

proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
    "host": proxyHost,
    "port": proxyPort,
    "user": proxyUser,
    "pass": proxyPass,
}

proxies = {
    "http": proxyMeta,
    "https": proxyMeta,
}

tunnel = random.randint(1, 1036)
print tunnel
count = linecache.getline('1000ua-pc.log', tunnel)
print count
headers = {"Proxy-Tunnel": str(tunnel)}
# resp = requests.get(targetUrl, proxies=proxies, headers=headers)

# print resp.status_code
# print resp.text

e_time = time.time()
d_time = e_time - s_time
print '完成! 用时%s' % d_time
