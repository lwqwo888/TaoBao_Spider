# coding=utf-8
import os
import re
import time
import Queue
import requests
import threading
from multiprocessing import Pool
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def img_url_process(list):
    list_length = len(list)
    k = 0
    # new_length = 1
    while k < list_length:
        img_url = list[k]
        img_url = "http:" + img_url
        # img_url = lines[k].replace('\n', '')
        k += 1
    map(downloading(img_url, ))

def downloading1(img_url, id, name, k, length_num, *args):
    proxy = {"http": ""}
    headers = {
        'authority': 'detail.tmall.com',
        'method': 'GET',
        'scheme': "https",
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "zh-CN,zh;q=0.9",
        'cache-control': "max-age=0",
        'cookie': "cna=XTyQEoI1uE4CAXBfh3IMFSpJ; cq=ccp%3D1; t=4d814acaeff7745d2b1df5c531cb7227; _tb_token_=3eb56ee77e988; cookie2=17B3F5F8A0D9CB4142FFBB0733EC948B; pnm_cku822=098%23E1hvApvUvbpvjQCkvvvvvjiPPL5wljtVP25hgjivPmPy1jYRRsdvzjiRR2z91jQPvpvhvvvvvvhCvvOvUvvvphvEvpCWh8%2Flvvw0zj7OD40OwoAQD7zheutYvtxr1RoKHkx%2F1RBlYb8rwZBleExreE9aWXxr1noK5FtffwLyaB4AVAdyaNoxdX3z8ikxfwoOddyCvm9vvvvvphvvvvvv96Cvpv9hvvm2phCvhRvvvUnvphvppvvv96CvpCCvkphvC99vvOC0B4yCvv9vvUvQud1yMsyCvvpvvvvviQhvCvvv9UU%3D; isg=ArOzZnnX7QJos6HBeuocdKfGQrcdQCLrPU38GWVQTFIJZNMG7bjX-hH2aqJx",
        'upgrade-insecure-requests': "1",
        'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    }
    path = "taobao_multimedia_data/%s/img/%s/" % (id, name)
    if (not (os.path.exists(path))):
        os.makedirs(path)

    format = img_url[-4:]
    # print format
    if args:
    # if isinstance(args[0], list):
        img_name = args[0][k]
    else:
        img_name = id + name + str(k+1)
    print "正在请求　%s" % name
    try:
        data = requests.get(img_url, headers=headers, proxies=proxy).content
    except Exception as e:
        print '图片请求失败...',e
    print "正在保存　%s" % img_name
    with open("taobao_multimedia_data/" + id + "/img/" + name + "/" + img_name + format, 'wb') as f:
        # print '******************',res
        f.write(data)
# --------------------------------------------------------------------------------------
    print '共%s个　第%s个url: %s' % (length_num, k+1, img_url)
    time.sleep(0.3)

    print "[INFO]: %s商品%s图片已抓取完成！！\n" % (id, name)
def downloading(img_url):
    num = 0
    headers = {
        'authority': 'detail.tmall.com',
        'method': 'GET',
        'scheme': "https",
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "zh-CN,zh;q=0.9",
        'cache-control': "max-age=0",
        'cookie': "cna=XTyQEoI1uE4CAXBfh3IMFSpJ; cq=ccp%3D1; t=4d814acaeff7745d2b1df5c531cb7227; _tb_token_=3eb56ee77e988; cookie2=17B3F5F8A0D9CB4142FFBB0733EC948B; pnm_cku822=098%23E1hvApvUvbpvjQCkvvvvvjiPPL5wljtVP25hgjivPmPy1jYRRsdvzjiRR2z91jQPvpvhvvvvvvhCvvOvUvvvphvEvpCWh8%2Flvvw0zj7OD40OwoAQD7zheutYvtxr1RoKHkx%2F1RBlYb8rwZBleExreE9aWXxr1noK5FtffwLyaB4AVAdyaNoxdX3z8ikxfwoOddyCvm9vvvvvphvvvvvv96Cvpv9hvvm2phCvhRvvvUnvphvppvvv96CvpCCvkphvC99vvOC0B4yCvv9vvUvQud1yMsyCvvpvvvvviQhvCvvv9UU%3D; isg=ArOzZnnX7QJos6HBeuocdKfGQrcdQCLrPU38GWVQTFIJZNMG7bjX-hH2aqJx",
        'upgrade-insecure-requests': "1",
        'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    }
    try:
        data = requests.get(img_url, headers=headers).content
    except Exception as e:
        print '图片请求失败...',e
    time.sleep(3)
    Queue.Queue().put(data)
    num += 1
    print num

def main(url_list):
    # # 多线程
    # thread_list = []
    # for url in url_list:
    #     # 创建一个线程，并指定执行的任务
    #     thread = threading.Thread(target=downloading, args=[url])
    #     # 启动线程
    #     thread.start()
    #     thread_list.append(thread)
    #     # thread.join()
    #
    # # 让主线程阻塞，等待所有的子线程结束，再继续执行。
    # for thread in thread_list:
    #     thread.join()

    # 创建10个线程的线程池
    pool = Pool(20)
    # map()高阶函数，用来批量处理函数传参
    pool.map(downloading, url_list)
    # 关闭线程池
    pool.close()
    # 阻塞主线程，等待子线程结束
    pool.join()

    # # 单线程
    # for i in url_list:
    #     downloading(i)


if __name__ == '__main__':
    list = [
        "http://gd3.alicdn.com/imgextra/i2/0/TB1wbYaatrJ8KJjSspaXXXuKpXa_!!0-item_pic.jpg",
        "http://gd1.alicdn.com/imgextra/i1/667831702/TB2SI9AaRY85uJjSZPcXXaGGpXa_!!667831702.jpg",
        "http://gd1.alicdn.com/imgextra/i1/2187095381/TB2fcw3s90jpuFjy0FlXXc0bpXa_!!2187095381.jpg",
        "http://gd1.alicdn.com/imgextra/i1/2187095381/TB2PqE2s3xlpuFjSszbXXcSVpXa_!!2187095381.jpg",
        "http://gd2.alicdn.com/imgextra/i2/2187095381/TB2zpxnw9FmpuFjSZFrXXayOXXa_!!2187095381.jpg",
        "http://img.alicdn.com/imgextra/i1/2187095381/TB2VHFmtmFjpuFjSspbXXXagVXa_!!2187095381.jpg",
        "http://img.alicdn.com/imgextra/i3/2187095381/TB2PJxltl8lpuFjSspaXXXJKpXa_!!2187095381.jpg",
        "http://img.alicdn.com/imgextra/i1/2187095381/TB2BPADs80kpuFjy1zdXXXuUVXa_!!2187095381.jpg",
        "http://img.alicdn.com/imgextra/i4/2187095381/TB2W4N4tmFjpuFjSszhXXaBuVXa_!!2187095381.jpg",
        "http://img.alicdn.com/imgextra/i1/2187095381/TB2.iUCs4XkpuFjy0FiXXbUfFXa_!!2187095381.jpg",
        "http://img.alicdn.com/imgextra/i3/2187095381/TB2y4n.wHBnpuFjSZFGXXX51pXa_!!2187095381.jpg",
        "http://img.alicdn.com/imgextra/i3/2187095381/TB23pv5s30kpuFjSspdXXX4YXXa_!!2187095381.jpg",
        "http://img.alicdn.com/imgextra/i3/2187095381/TB2v8A6wUdnpuFjSZPhXXbChpXa_!!2187095381.jpg",
        "http://img.alicdn.com/imgextra/i1/2187095381/TB2aoJfw5pnpuFjSZFkXXc4ZpXa_!!2187095381.jpg",
        "http://img.alicdn.com/imgextra/i2/2187095381/TB2j.Jfw5pnpuFjSZFkXXc4ZpXa_!!2187095381.jpg",
        "http://img.alicdn.com/imgextra/i2/2187095381/TB2KC0iclU4h1JjSZFLXXaFMpXa_!!2187095381.jpg",
        "http://img.alicdn.com/imgextra/i4/2187095381/TB2Njg9wUhnpuFjSZFEXXX0PFXa_!!2187095381.jpg",
        "http://img.alicdn.com/imgextra/i4/2187095381/TB2NFdcwZtnpuFjSZFvXXbcTpXa_!!2187095381.jpg",
    ]
    t1 = time.time()
    main(list)
    t2 = time.time()
    print t2-t1