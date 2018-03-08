# coding=utf-8
import os
import re
import time
import requests
from multiprocessing import Pool
from taobao_img_spider import Taobao_Img
from taobao_videos_spider import Taobao_Videos
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


if __name__ == '__main__':
    start = time.time()
    ti = Taobao_Img()
    tv = Taobao_Videos()
    with open('taobaourl.txt', 'rb') as f:
        lines = f.readlines()
    length = len(lines)
    print length
    i = 0
    while i < length:
        line = lines[i]
        id = ti.url_process(line)
        # id = "546019442312"
        ti.page_data(id)
        ti.turn_img(id)
        ti.color_img(id)
        ti.detail_img(id)
        print "%s商品所有图片抓取完成！！！！！！！！\n\n" % id
        tv.video(id)
        i += 1
        print "第%s件商品 已完成抓取!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" % str(i)


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
