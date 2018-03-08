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
import linecache
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
        # self.proxy = {"http": ""}
        self.sec = 0
        self.old_sec = 0

    def change_ip(self):
        new_sec = time.time()
        self.sec = new_sec - self.old_sec
        if self.sec > 0.3:
            # 代理服务器
            proxyHost = "n10.t.16yun.cn"
            proxyPort = "6442"

            # 代理隧道验证信息
            proxyUser = "16SBYYUY"
            proxyPass = "658666"

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
        tunnel = random.randint(1, 1036)
        # print tunnel
        user_agent = linecache.getline('1000ua-pc.log', tunnel)
        user_agent = user_agent.strip().replace('\n', '').replace('\r', '')
        # print user_agent
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
            "referer": "https://item.taobao.com/item.htm?spm=a219r.lmn002.14.174.6f516358W81jq9&id=561495525977&ns=1&abbucket=16",
            'user-agent': user_agent,
        }


    def video(self, sid, category_name, dir_name):
        url = 'https://detail.tmall.com/item.htm?&id=' + sid
        print '正在请求页面数据..'
        self.change_ua()
        # self.change_ip()
        try:
            response = requests.get(url, headers=self.headers)
            if response.status_code == 200:
                html = response.text
                # print self.headers
                # print self.proxy

        except Exception as e:
            print '数据请求失败...正在重试......', e
            self.log(str(e))
            # # global NETWORK_STATUS
            NETWORK_STATUS = False  # 请求超时改变状态

            if NETWORK_STATUS == False:
                #     '请求超时'
                for i in range(1, 11):
                    time.sleep(0.3)
                    print '请求失败，第%s次重复请求' % i
                    if i == 5:
                        print "[INFO]: 程序睡眠中......"
                        time.sleep(10)
                    self.change_ua()
                    # self.change_ip()
                    try:
                        response = requests.get(url, headers=self.headers)
                        if response.status_code == 200:
                            html = response.text
                            break
                    except:
                        print '第%s次重复请求失败! 继续重试...' % i
                        continue

                with open('request.log', 'a') as f:
                    f.write('%s 请求失败%s - %s\n' % (url, id, time.ctime()))
                print ('[INFO]:重发请求失败!!!!!!!!!!')
        time.sleep(1)
        print self.headers
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
        res = ""
        # taobao_multimedia_datas/女装/女装连衣裙/videos/
        path = "taobao_multimedia_datas/%s/%s/%s/videos/" % (category_name, dir_name, sid)
        if (not (os.path.exists(path))):
            os.makedirs(path)

        print '正在请求%s视频内容' % sid
        url = 'https://cloud.video.taobao.com/play/u/%s/p/1/e/6/t/1/%s.mp4' % (vid1, vid2)
        print url
        self.change_ua()
        self.change_ip()
        try:
            response = requests.get(url, headers=self.headers, proxies=self.proxy)
            if response.status_code == 200:
                res = response.content
                # print self.headers
                # print self.proxy

        except Exception as e:
            print '数据请求失败...正在重试......', e
            self.log(str(e))
            with open('request.log', 'a') as f:
                f.write('%s [代理]请求失败%s - %s\n' % (url, id, time.ctime()))
            # # global NETWORK_STATUS
            NETWORK_STATUS = False  # 请求超时改变状态

            if NETWORK_STATUS == False:
                #     '请求超时'
                for i in range(1, 11):
                    time.sleep(0.3)
                    print '请求失败，第%s次重复请求' % i
                    if i == 5:
                        print "[INFO]: 代理睡眠中......"
                        time.sleep(10)
                    self.change_ua()
                    self.change_ip()
                    try:
                        response = requests.get(url, headers=self.headers, proxies=self.proxy)
                        if response.status_code == 200:
                            res = response.content
                            with open('request.log', 'a') as f:
                                f.write('%s 重新请求成功%s - %s\n' % (url, id, time.ctime()))
                            print ('[INFO]:重发请求成功!!!!!!!!!!')
                            break
                    except:
                        with open('request.log', 'a') as f:
                            f.write('%s 重新请求失败, 继续重试...%s - %s\n' % (url, id, time.ctime()))
                        print ('[INFO]:重发请求失败!!!!!!!!!!')
                        print '第%s次重复请求失败! 继续重试...' % i
                        continue

                if response.status_code == 200:
                    with open('request.log', 'a') as f:
                        f.write('%s 最终请求成功!!!!!%s - %s\n' % (url, id, time.ctime()))
                    print ('[INFO]:重发请求成功!!!!!!!!!!')
                else:
                    with open('request.log', 'a') as f:
                        f.write('%s 最终请求失败! ! ! ! !%s - %s\n' % (url, id, time.ctime()))
                    print ('[INFO]:重发请求失败!!!!!!!!!!')
            # print self.headers

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
    category_name = 'ttttt'
    dir_name = 'ggggg'
    for line in lines:
        id = tv.url_process(line)
        print id
        id = "18322316303"
        tv.video(id, category_name, dir_name)
        time.sleep(0)
