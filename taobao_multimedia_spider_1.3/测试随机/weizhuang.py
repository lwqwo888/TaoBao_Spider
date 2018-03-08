# coding=utf-8
import re
import time
import random
import requests
import linecache
from lxml import etree
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

list = [
    "http://gd2.alicdn.com/imgextra/i1/54507609/TB2KrNid7fb_uJkSnaVXXXFmVXa_!!54507609.jpg",
    "http://gd2.alicdn.com/imgextra/i2/54507609/TB2Hd3SXXkoBKNjSZFEXXbrEVXa_!!54507609.jpg",
    "http://gd2.alicdn.com/imgextra/i2/54507609/TB2fGH3mcnI8KJjSsziXXb8QpXa_!!54507609.jpg",
    "http://gd4.alicdn.com/imgextra/i4/54507609/TB2cK7CmnnI8KJjy0FfXXcdoVXa_!!54507609.jpg",
    "http://gd3.alicdn.com/imgextra/i3/54507609/TB2l4f0mgvD8KJjy0FlXXagBFXa_!!54507609.jpg",
    "http://gd3.alicdn.com/imgextra/i3/54507609/TB13UIXXborBKNjSZFjXXc_SpXa_!!0-item_pic.jpg"
]
headers = {

    "cookie": "ubn=p; ucn=unsz; t=28edc35882e1fcf06bfaa67008da2a8f; cna=XTyQEoI1uE4CAXBfh3IMFSpJ; thw=cn; miid=6347655561018672771; uc3=sg2=WqIrBf2WEDhnXgIg9lOgUXQnkoTeDo019W%2BL27EjCfQ%3D&nk2=rUs9FkCy6Zs6Ew%3D%3D&id2=VWeZAHoeqUWF&vt3=F8dBzLgoJIN4WC0X30I%3D&lg2=VFC%2FuZ9ayeYq2g%3D%3D; lgc=%5Cu6211%5Cu6210%5Cu4F60%5Cu5669%5Cu68A6; tracknick=%5Cu6211%5Cu6210%5Cu4F60%5Cu5669%5Cu68A6; _cc_=WqG3DMC9EA%3D%3D; tg=0; enc=GtOY%2B8mhUi7LXIrV9LqmUl0PYsVpr9BbSzEB9GL%2Fq3i6Czwxxh5mE60CMJjep9GIq4iV04PvQsAGhzOIdrf6iw%3D%3D; mt=ci=-1_0; UM_distinctid=160fe373fd7c89-0f04cad75d123e-393d5f0e-1fa400-160fe373fd8e5a; hng=CN%7Czh-CN%7CCNY%7C156; _m_h5_tk=081b6ec244bfd7ba155325c85a14056e_1516103738466; _m_h5_tk_enc=8531a9b39cfb4a076e45dfad1fba7525; cookie2=16e0f40738dc82c43c53992cb5a26ebb; _tb_token_=3daeebbb3768e; v=0; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; uc1=cookie14=UoTdfYT5TUo4kA%3D%3D; isg=BDo6USLQNOpL5rgFeJZzPiuWi2CcQ9uEDF5FrkQyJ02YN9lxLHiA1B8ng8PrpzZd",
    "referer": "https://item.taobao.com/item.htm?spm=a219r.lmn002.14.174.6f516358W81jq9&id=561495525977&ns=1&abbucket=16",
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",

}

srequest = requests.Session()
i = 1
url = "http://gd2.alicdn.com/imgextra/i2/54507609/TB2fGH3mcnI8KJjSsziXXb8QpXa_!!54507609.jpg",

while True:
    name = 'taobao%s.jpg' % i
    print name
    res = srequest.get(url, headers=headers, proxies={'http': 'http://16SBYYUY:658666@n10.t.16yun.cn:6442', 'https': 'http://16SBYYUY:658666@n10.t.16yun.cn:6442'})
    print res.status_code
    time.sleep(0.3)
    # with open(name, 'wb') as f:
    #     f.write(res.content)
    i += 1

print ''
j = 0
while j < 6:
    res = requests.get("http://2017.ip138.com/ic.asp", proxies={'http': 'http://16SBYYUY:658666@n10.t.16yun.cn:6442', 'https': 'http://16SBYYUY:658666@n10.t.16yun.cn:6442'})
    print res.status_code
    resp = res.content
    html = etree.HTML(resp)
    ip_code = html.xpath("/html/body/center//text()")
    print ip_code[0]
    j += 1



def pro():
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
    print proxy
    return proxy