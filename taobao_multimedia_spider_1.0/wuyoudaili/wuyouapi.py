# coding=utf-8
import requests
from multiprocessing.dummy import Pool
import json
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def change_ip():
    # 这里填写无忧代理IP提供的API订单号（请到用户中心获取）
    order = "c8e8aaa741a90db677477445e3874372"
    # 获取IP的API接口
    apiUrl = "http://api.ip.data5u.com/dynamic/get.html?order=" + order
    res = requests.get(apiUrl).text
    print res
    return res

if __name__ == '__main__':
    proxy = change_ip()
    ips = proxy.split("\n")[0]
    proxies = {"http": ips}
    print proxies
    html = requests.get("http://img.alicdn.com/imgextra/i1/0/TB2HDYnXAZmBKNjSZPiXXXFNVXa_!!0-rate.jpg", proxies=proxies).text
    print '-' * 80
    print html