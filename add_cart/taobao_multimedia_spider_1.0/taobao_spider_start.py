# coding=utf-8
import os
import re
import time
import copy
import requests
from collections import Counter
from multiprocessing import Pool
from taobao_img_spider import Taobao_Img
from taobao_videos_spider import Taobao_Videos
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def go_repeat():
    with open('taobaourl.txt', 'rb') as f:
        lines = f.readlines()
        new_lines = copy.deepcopy(lines)
    print '去重前--------------------------------------------'
    # print lines
    print len(lines)
    print '------------------------------------------------------'

    url_list = []
    for line in lines:
        id = url_process(line)
        url_list.append(id)

    c = Counter()
    for ch in url_list:
        c[ch] = c[ch] + 1
    # count_list = list(c.values())
    # print count_list
    # max_value = max(count_list)
    max_list = []
    repeat_dict = {}
    for k, v in c.items():
        if v > 1:
            repeat_dict[k] = v
            max_list.append(k)
    # max_list = sorted(max_list)
    length = len(max_list)
    # print max_list
    # print repeat_dict
    print '共有%s个id重复, 如需查看重复ID请打开"重复商品ID.txt"' % length
    for i in repeat_dict:
        with open('重复商品ID.txt', 'a') as f:
            f.write(i + " ID出现次数: " + str(repeat_dict[i]) + '\n')

    i = 0
    # 用来存放重复的索引的列表
    repeat_index_list = []
    while i < length:
        key = max_list[i]
        value_num = repeat_dict[key]
        lines_length = len(lines)
        j = 0
        while j < lines_length:
            if key in lines[j]:
                if value_num > 1:
                    repeat_index_list.append(j)
                    value_num -= 1
            j += 1
        i += 1

    # 翻转列表,从后往前删
    new_repeat_index_list = list(reversed(repeat_index_list))
    for i in new_repeat_index_list:
        new_lines.pop(i)
    print '去重后--------------------------------------------'
    # print new_lines
    print len(new_lines)
    for j in new_lines:
        with open('淘宝商品.txt', 'a') as f:
            f.write(j)
    print '---------------------------------------------------'
    return new_lines
    # for i in new_lines:

    # url_list_length = len(new_lines)
    # print "去重前url数量:%s" % url_list_length
    # news_img_url_list = list(set(new_lines))
    # news_img_url_list.sort()
    # new_length = len(news_img_url_list)
    # print '去重后url数量:', new_length

def url_process(url):
    res = re.compile(r'(\?|&)id=(\d+).*?', re.S)
    id = res.search(url).group(2)
    # print id
    return ''.join(id)

if __name__ == '__main__':
    start = time.time()
    ti = Taobao_Img()
    tv = Taobao_Videos()
    start = time.time()
    new_lines = go_repeat()
    new_length = len(new_lines)
    i = 0
    while i < new_length:
        line = new_lines[i]
        dir_name_list = line.split("*")
        category_name = dir_name_list[1]
        dir_name = dir_name_list[2]
        id = url_process(line)
        print category_name
        print dir_name
        # id = "546019442312"
        print "[INFO]开始抓取...................................."
        ti.page_data(id)
        ti.turn_img(id, category_name, dir_name)
        ti.color_img(id, category_name, dir_name)
        ti.detail_img(id, category_name, dir_name)
        print "%s商品所有图片抓取完成！！！！！！！！\n" % id
        tv.video(id, category_name, dir_name)
        i += 1
        print "第%s件商品 已完成抓取!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n" % str(i)


    end = time.time()
    time_s = end-start
    print "所有抓取任务已完成！共计用时%s秒\n\n" % time_s




    # for line in lines:
    #     id = ti.url_process(line)
    #     ti.page_data(id)
    #     ti.turn_img(id)
    #     ti.color_img(id)
    #     ti.detail_img(id)
    #     print "%s商品所有图片抓取完成！！！！！！！！\n\n" % id
    #     tv.video(id)
