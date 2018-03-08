# coding=utf-8
import os
import re
import sys
import time
from collections import Counter

reload(sys)
sys.setdefaultencoding('utf-8')


def url_process(url):
    res = re.compile(r'(\?|&)id=(\d+).*?', re.S)
    id = res.search(url).group(2)
    # print id
    return ''.join(id)


if __name__ == '__main__':
    start = time.time()
    with open('taobaourl.txt', 'rb') as f:
        lines = f.readlines()
    url_list = []
    dict = {}
    for line in lines:
        id = url_process(line)
        url_list.append(id)
    length = len(url_list)
    c = Counter()
    for ch in url_list:
        c[ch] = c[ch] + 1
    print c
    # print "去重前id数量:%s" % length
    # news_img_url_list = list(set(url_list))
    # news_img_url_list.sort()
    # new_length = len(news_img_url_list)
    # print '去重后url数量:', new_length