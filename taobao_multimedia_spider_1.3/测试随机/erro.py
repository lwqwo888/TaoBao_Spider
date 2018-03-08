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


class IllegalException(Exception):
    def __init__(self, code=400, msg='参数错误', errorcode=10000):
        self.err = {}
        self.err['code'] = code
        self.err['msg'] = msg
        self.err['errorcode'] = errorcode

        Exception.__init__(self, self.err)


try:
    integer = None
    if integer != True:
        raise (IllegalException)
except IllegalException as x:
    print x
else:
    print('NO ERROR')