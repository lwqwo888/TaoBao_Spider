# coding=utf-8
# 通过pvs直接找库存
# 优点：速度稍快
# 缺点：无货商品库存没有体现，需手动置0或置为＂无货＂
import re
import time
import random
import requests
import linecache
import sys
reload(sys)
sys.setdefaultencoding('utf-8')



def request(url, retries):
    proxies = {
        "http": '61.132.93.14:6441',
        "https": '61.132.93.14:6441',
    }

    # res = requests.get(url, proxies=proxies)
    # print res.text
    # res = res.status_code
    # print 'tttt', res
    try:
        res = requests.get(url, proxies=proxies)
        res_num = res.status_code
        print res_num
    except Exception, e:
        print e.message
        if retries > 0:
            time.sleep(1)
            return request(url=url, retries=retries - 1)
        else:
            print 'GET Failed'
            return ''

    if res_num != 200:
        return None
    return res


url = "http://baidu.com/"
retries = 5
request(url, retries)




# NETWORK_STATUS = True # 判断状态变量
# try:
#     url = "http://baidu.com"
#     response = requests.post(url, headers=self.headers, data=data, timeout=5)
#     if response.status_code == 200:
#         return response
# except requests.exceptions.Timeout:
#     global NETWORK_STATUS
#     NETWORK_STATUS = False # 请求超时改变状态
#
#     if NETWORK_STATUS == False:
#         '''请求超时'''
#         for i in range(1, 10):
#             print '请求超时，第%s次重复请求' % i
#             response = requests.post(url, headers=self.headers, data=data, timeout=5)
#             if response.status_code == 200:
#                 return response
# return -1  # 当所有请求都失败，返回  -1  ，此时有极大的可能是网络问题或IP被封。