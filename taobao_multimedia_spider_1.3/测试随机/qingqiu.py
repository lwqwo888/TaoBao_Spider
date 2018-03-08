# coding=utf-8
import re
import time
import random
import requests
import linecache
import sys
reload(sys)
sys.setdefaultencoding('utf-8')



# # 要访问的目标页面
# targetUrl = "http://httpbin.org/ip"

# 代理服务器
proxyHost = "n10.t.16yun.cn"
proxyPort = "6442"

# 代理隧道验证信息
proxyUser = "16SBYYUY"
proxyPass = "658666"

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

# tunnel = random.randint(1, 10000)
# headers = {"Proxy-Tunnel": str(tunnel)}
# resp = requests.get(targetUrl, proxies=proxies, headers=headers)
proxy = proxies



url = "http://img.alicdn.com/imgextra/i2/0/TB2f5T4X29TBuNjy1zbXXXpepXa_!!0-rate.jpg"
res = requests.get(url, proxies=proxy).content
with open("tupian.jpg", 'wb') as f:
    f.write(res)