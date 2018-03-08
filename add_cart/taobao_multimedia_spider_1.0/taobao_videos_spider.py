# coding=utf-8
import os
import re
import time
import requests
import threading
from lxml import etree
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

class Taobao_Videos(object):
    def __init__(self):
        current_path = os.path.split(os.path.realpath(__file__))[0]
        self.__file_log = open('%s/log/videos_log%s.txt' % (current_path, time.strftime('%Y_%m_%d')), 'a+')
        self.mutex = threading.Lock()
        self.headers = {
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
        self.proxy = {"http": ""}
    def video(self, sid, category_name, dir_name):
        url = 'https://detail.tmall.com/item.htm?&id=' + sid
        print '正在请求页面数据..'
        html = requests.get(url, headers=self.headers, proxies=self.proxy).text
        res = etree.HTML(html)
        print '正在解析页面数据'
        title = res.xpath('/html/head/link[@rel="canonical"]/@href|//*[@id="mallLogo"]/span/a/@href')[0]

        if "taobao.com/" in title:
            print "淘宝", title
            mark_num = 1
        elif "tmall.com/" in title:
            print "天猫", title
            mark_num = 2
        elif "chaoshi.tmall.com" in title:
            print "天猫超市", title
            mark_num = 3
        else:
            print "其他", title
            mark_num = 4
        print mark_num
        if mark_num == 1:
            res1 = re.compile(r'"videoId":"(.*?)".*"videoOwnerId":"(.*?)",', re.S)
            vid = res1.findall(html)
            if vid:
                vid1 = vid[0][1]
                vid2 = vid[0][0]
                print 'vid1:', vid1
                print 'vid2:', vid2
                self.download_video(sid, vid1, vid2, category_name, dir_name)
            else:
                print "[INFO]: %s商品没有展示视频！" % sid

        elif mark_num == 2:
            res2 = re.compile(r'"imgVedioUrl":".*?u/(.*?)/p.*?8/(.*?)\.swf"', re.S)
            res2.findall(html)
            vid = res2.findall(html)
            if vid:
                vid1 = vid[0][0]
                vid2 = vid[0][1]
                print 'vid1:', vid1
                print 'vid2:', vid2
                self.download_video(sid, vid1, vid2, category_name, dir_name)
            else:
                print "[INFO]: %s商品没有展示视频！" % sid

    def download_video(self, sid, vid1, vid2, category_name, dir_name):
        # taobao_multimedia_datas/女装/女装连衣裙/videos/
        path = "taobao_multimedia_datas/%s/%s/%s/videos/" % (category_name, dir_name, sid)
        if (not (os.path.exists(path))):
            os.makedirs(path)
        try:
            print '正在请求%s视频内容' % sid
            url = 'https://cloud.video.taobao.com/play/u/%s/p/1/e/6/t/1/%s.mp4' % (vid1, vid2)
            res = requests.get(url, headers=self.headers, proxies=self.proxy).content
        except Exception as e:
            print e
            self.log(str("视频请求失败!",e))
        try:
            print '正在保存%s视频内容...' % sid
            with open(path + sid + "video.mp4", 'wb') as f:
                f.write(res)
            print '[INFO]: %s视频保存成功!!\n' % sid
        except Exception as e:
            print "视频保存失败!"
            self.log(str("视频保存失败!", e))

    def url_process(self, url):
        res = re.compile(r'(\?|&)id=(\d+).*?', re.S)
        id = res.search(url).group(2)
        # print id
        return ''.join(id)

    def log(self, msg):
        self.mutex.acquire()
        self.__file_log.write(msg.encode('utf-8'))
        self.__file_log.write(u'\n'.encode('utf-8'))
        self.mutex.release()

# if __name__ == '__main__':
#     tv = Taobao_Videos()
#     with open('taobaourl.txt', 'rb') as f:
#         lines = f.readlines()
#     for line in lines:
#         id = tv.url_process(line)
#         print id
#         # id = "538955936213"
#         tv.video(id)
#         time.sleep(1)
