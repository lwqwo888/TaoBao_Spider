# coding=utf-8
import re
import time
import random
import requests
import linecache
import sys
reload(sys)
sys.setdefaultencoding('utf-8')



def add():
    res = ""
    url = "http://baidu.com"
    try:
        res = requests.get(url).text
    except Exception as e:
        print "cuowu"
    print res

while True:
    add()
