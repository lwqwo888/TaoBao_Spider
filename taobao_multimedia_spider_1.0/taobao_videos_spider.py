# coding=utf-8
# version: 1.1
# 脚本功能: 淘宝商品视频获取
# 参数: sid(id), category_name(分类文件夹名), dir_name(商品文件夹名),
# date : 2018-02-11
# Creator: lwq
import os
import re
import time
import random
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
            'user-agent': self.change_ua()
        }
        self.proxy = {"http": ""}
        self.sec = 0
        self.old_sec = 0


    def change_ip(self):
        new_sec = time.time()
        self.sec = new_sec - self.old_sec
        if self.sec > 2:
            # 代理服务器
            proxyHost = "http-pro.abuyun.com"
            proxyPort = "9010"

            # 代理隧道验证信息
            proxyUser = "H936388O1A2K0GRP"
            proxyPass = "9B04BC6FBB2A0902"

            proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
                "host": proxyHost,
                "port": proxyPort,
                "user": proxyUser,
                "pass": proxyPass,
            }
            print proxyMeta
            proxies = {
                "http": proxyMeta,
                "https": proxyMeta,
            }
            self.proxy = proxies
        else:
            self.proxy = self.proxy

    def change_ua(self):
        ua_list  = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10",
            "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8",
            "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5",
            "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12",
            "Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
            "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.302.2 Safari/532.8",
            "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.464.0 Safari/534.3",
            "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_5; en-US) AppleWebKit/534.13 (KHTML, like Gecko) Chrome/9.0.597.15 Safari/534.13",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.186 Safari/535.1",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.54 Safari/535.2",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
            "Mozilla/5.0 (Macintosh; U; Mac OS X Mach-O; en-US; rv:2.0a) Gecko/20040614 Firefox/3.0.0 ",
            "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.0.3) Gecko/2008092414 Firefox/3.0.3",
            "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.1) Gecko/20090624 Firefox/3.5",
            "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.2.14) Gecko/20110218 AlexaToolbar/alxf-2.0 Firefox/3.6.14",
            "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
            "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
        ]
        ua_list_len = len(ua_list)-1
        user_agent = ua_list[random.randint(0, ua_list_len)]
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
            # 'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
            'user-agent': user_agent,
        }


    def video(self, sid, category_name, dir_name):
        url = 'https://detail.tmall.com/item.htm?&id=' + sid
        print '正在请求页面数据..'
        # self.change_ua()
        # self.change_ip()
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
            # self.change_ua()
            # self.change_ip()
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

if __name__ == '__main__':
    tv = Taobao_Videos()
    with open('taobaourl.txt', 'rb') as f:
        lines = f.readlines()
    category_name = '男鞋'
    dir_name = '运动鞋'
    for line in lines:
        id = tv.url_process(line)
        print id
        # id = "538955936213"
        tv.video(id, category_name, dir_name)
        time.sleep(1)
