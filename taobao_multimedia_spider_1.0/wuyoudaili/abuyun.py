# coding=utf-8
import json
import re
import random
import requests
from lxml import etree
from multiprocessing.dummy import Pool
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# # 要访问的目标页面
# targetUrl = "http://proxy.abuyun.com/switch-ip"
#
# # 代理服务器
# proxyHost = "http-pro.abuyun.com"
# proxyPort = "9010"
#
# # 代理隧道验证信息
# proxyUser = "H936388O1A2K0GRP"
# proxyPass = "9B04BC6FBB2A0902"


targetUrl = "http://test.abuyun.com/proxy.php"

# 代理服务器
proxyHost = "http-dyn.abuyun.com"
proxyPort = "9020"

# 代理隧道验证信息
proxyUser = "HT61EH124W76BT0D"
proxyPass = "4ACBA2E4CA543ED8"

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
print proxyMeta

# resp = requests.get(targetUrl, proxies=proxies)
html = requests.get("http://2017.ip138.com/ic.asp", proxies=proxies).content
res = etree.HTML(html)
title = res.xpath("/html/body/center//text()")
for i in title:
    print i

# print resp.status_code
# print resp.text