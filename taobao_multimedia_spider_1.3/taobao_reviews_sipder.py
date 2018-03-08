# coding=utf-8
# version: 1.1
# 脚本功能: 淘宝商品评论获取
# 参数: id(id), category_name(分类文件夹名), dir_name(商品文件夹名),
# date : 2018-02-22
# Creator: lwq
import re
import os
import time
import json
import random
import jsonpath
import requests
import linecache
import threading
from lxml import etree
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class Taobao_Comment(object):
    def __init__(self):
        current_path = os.path.split(os.path.realpath(__file__))[0]
        current_path = current_path + '/log'
        if (not (os.path.exists(current_path))):
            os.makedirs(current_path)
        # print current_path
        self.__file_log = open('%s/reviews_log%s.txt' % (current_path, time.strftime('%Y_%m_%d')), 'a+')
        self.mutex = threading.Lock()
        # self.headers = {
        #     'authority': 'detail.tmall.com',
        #     'method': 'GET',
        #     'scheme': "https",
        #     'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        #     'accept-encoding': "gzip, deflate, br",
        #     'accept-language': "zh-CN,zh;q=0.9",
        #     'cache-control': "max-age=0",
        #     'cookie': "cna=XTyQEoI1uE4CAXBfh3IMFSpJ; cq=ccp%3D1; t=4d814acaeff7745d2b1df5c531cb7227; _tb_token_=3eb56ee77e988; cookie2=17B3F5F8A0D9CB4142FFBB0733EC948B; pnm_cku822=098%23E1hvApvUvbpvjQCkvvvvvjiPPL5wljtVP25hgjivPmPy1jYRRsdvzjiRR2z91jQPvpvhvvvvvvhCvvOvUvvvphvEvpCWh8%2Flvvw0zj7OD40OwoAQD7zheutYvtxr1RoKHkx%2F1RBlYb8rwZBleExreE9aWXxr1noK5FtffwLyaB4AVAdyaNoxdX3z8ikxfwoOddyCvm9vvvvvphvvvvvv96Cvpv9hvvm2phCvhRvvvUnvphvppvvv96CvpCCvkphvC99vvOC0B4yCvv9vvUvQud1yMsyCvvpvvvvviQhvCvvv9UU%3D; isg=ArOzZnnX7QJos6HBeuocdKfGQrcdQCLrPU38GWVQTFIJZNMG7bjX-hH2aqJx",
        #     'upgrade-insecure-requests': "1",
        #     "referer": "https://item.taobao.com/item.htm?spm=a219r.lmn002.14.174.6f516358W81jq9&id=561495525977&ns=1&abbucket=16",
        #     'user-agent': self.change_ua()
        # }
        # self.headers = ""
        # self.proxy = {"http": ""}
        self.num = 1
        self.count = 0
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
            # print proxyMeta
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


    def comment(self, id, category_name, dir_name):
        html = ""
        # 不携带currentPageNum参数看不到数据,不携带rateType参数数据顺序会乱
        url = 'https://rate.taobao.com/feedRateList.htm?auctionNumId=%s&currentPageNum=1&rateType=3' % id
        # headers = {
        #
        #     "cookie": "ubn=p; ucn=unsz; t=28edc35882e1fcf06bfaa67008da2a8f; cna=XTyQEoI1uE4CAXBfh3IMFSpJ; thw=cn; miid=6347655561018672771; uc3=sg2=WqIrBf2WEDhnXgIg9lOgUXQnkoTeDo019W%2BL27EjCfQ%3D&nk2=rUs9FkCy6Zs6Ew%3D%3D&id2=VWeZAHoeqUWF&vt3=F8dBzLgoJIN4WC0X30I%3D&lg2=VFC%2FuZ9ayeYq2g%3D%3D; lgc=%5Cu6211%5Cu6210%5Cu4F60%5Cu5669%5Cu68A6; tracknick=%5Cu6211%5Cu6210%5Cu4F60%5Cu5669%5Cu68A6; _cc_=WqG3DMC9EA%3D%3D; tg=0; enc=GtOY%2B8mhUi7LXIrV9LqmUl0PYsVpr9BbSzEB9GL%2Fq3i6Czwxxh5mE60CMJjep9GIq4iV04PvQsAGhzOIdrf6iw%3D%3D; mt=ci=-1_0; UM_distinctid=160fe373fd7c89-0f04cad75d123e-393d5f0e-1fa400-160fe373fd8e5a; hng=CN%7Czh-CN%7CCNY%7C156; _m_h5_tk=081b6ec244bfd7ba155325c85a14056e_1516103738466; _m_h5_tk_enc=8531a9b39cfb4a076e45dfad1fba7525; cookie2=16e0f40738dc82c43c53992cb5a26ebb; _tb_token_=3daeebbb3768e; v=0; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; uc1=cookie14=UoTdfYT5TUo4kA%3D%3D; isg=BDo6USLQNOpL5rgFeJZzPiuWi2CcQ9uEDF5FrkQyJ02YN9lxLHiA1B8ng8PrpzZd",
        #     "referer": "https://item.taobao.com/item.htm?spm=a219r.lmn002.14.174.6f516358W81jq9&id=561495525977&ns=1&abbucket=16",
        #     "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
        #     # "user-agent": user_agent,
        # }
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
            with open('request.log', 'a') as f:
                f.write('%s [程序]请求失败%s - %s\n' % (url, id, time.ctime()))

            # # global NETWORK_STATUS
            NETWORK_STATUS = False  # 请求超时改变状态

            if NETWORK_STATUS == False:
                #     '请求超时'
                for i in range(1, 11):
                    time.sleep(1)
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
        time.sleep(1)
        # print self.headers
        # print html
        # return
        html = html.strip()
        html = html.strip("()")
        res = json.loads(html)
        # 所有评论日期
        str_date = jsonpath.jsonpath(res, expr='$..comments[*].date')
        # 获取所有评论人
        str_name = jsonpath.jsonpath(res, expr='$..comments[*].user.nick')
        # 获取所有文字评论,除追加评论外
        str_info = jsonpath.jsonpath(res, expr='$..comments[*].content')
        # 获取所有评论图片,除追加图片和视频外
        img_data = jsonpath.jsonpath(res, expr='$..comments[*].photos')

        # 获取所有评论视频
        video_data = jsonpath.jsonpath(res, expr='$..comments[*].video')
        # print video_data
        # print str_name, str_date, str_info
        # 商品没有评价就退出
        if not str_name:
            print '此商品没有任何评价内容!!!!!'
            return
        comment_data = [x for x in zip(str_name, str_date, str_info)]
        # taobao_multimedia_datas/女装/女装连衣裙1/id/评论/评论内容.txt
        path = "taobao_multimedia_datas/%s/%s/%s/评论/" % (category_name, dir_name, id)
        # print path
        if (not (os.path.exists(path))):
            os.makedirs(path)
        j = 0
        for p, d, i in comment_data:   # p:评论人 d:评论时间 i:评论内容
            j += 1
            with open(path + '评论内容.txt', 'a') as f:
                f.write('评论' + str(j) + ' ' + p + '---' + d + ':' + i + '\r\n')
                # print p,'---', d, ':',  i

        # 获取所有文字追加评论,以及追加图片链接
        append_img_list = []
        num_length = len(str_date)
        num = 0
        while num < num_length:
            # 所有追加内容
            expr_str = '$..comments[%s].appendList[*].content' % num
            append_str_info = jsonpath.jsonpath(res, expr=expr_str)
            # 检查所有追加评论图片链接,即便是空
            expr_img_str = '$..comments[%s].appendList..photos..url' % num
            append_img_info = jsonpath.jsonpath(res, expr=expr_img_str)
            # print append_img_info, '+++++++++'
            # print append_str_info, '+++++++++'

            # 根据原评价追加写入追评
            if append_str_info:
                # print '---------------------'
                # print '评论%s' % str(num + 1),''.join(append_str_info)
                with open(path + '评论内容.txt') as f:
                    lines = f.readlines()
                # ---------------------------------------------------------------------------
                with open(path + '评论内容.txt', 'w') as w:
                    for l in lines:
                        # print l
                        str1 = '评论%s ' % str(num + 1)
                        append_content = '\t--->追加评论内容:%s' % ''.join(append_str_info)
                        # print str1, append_content
                        if (l.startswith(str1)):
                            # print '********************************************'
                            # print str1
                            w.write(l.replace(b'\n', append_content + '\r\n'))
                        else:
                            w.write(l)
            # 抽取出所有存在的追加图片链接
            if not append_img_info:
                append_img_list.append([])
            else:
                append_img_list.append(append_img_info)
            num += 1

        # 当前页面追加评论总条数
        s = 1
        for i in append_img_list:
            if i:
                self.count += 1
            s += 1
        # 下载追加图片链接
        s = 1
        for i in append_img_list:
            if i:
                name = '评论%s_追加' % s
                append_img_length = len(i)
                self.download_data(append_img_length, i, id, category_name, dir_name, name)
            s += 1

        img_big_list = []
        video_big_list = []
        # 解析所有图片链接,不包括追评
        length = len(img_data)
        # print img_data, '='*20
        # 保存当前页面评论总条数
        self.count = length
        x = 0
        for i in img_data:
            # print i, '666666666'
            if i is None:
                # print 777777777
                pass
            else:
                # 评论图片, 不包括追加评论图片
                img_list = jsonpath.jsonpath(i, expr='$..url')
                # 如果有图片就追加到图片大列表,如果这个图片评论没有图,就追加个列表N
                if img_list:
                    img_big_list.append(img_list)
                else:
                    img_big_list.append(list('N'))
            x += 1

        # print len(video_data)
        # 解析所有视频链接
        for i in video_data:
            if i is None:
                video_big_list.append(list('N'))
            else:
                video_list = jsonpath.jsonpath(i, expr='$.cloudVideoUrl')
                video_big_list.append(video_list)

        # 下载非追加图片
        i = 0
        while i < length:
            # print img_big_list[i]
            img_big_list_len = len(img_big_list[i])
            self.download_data(img_big_list_len, img_big_list[i], id, category_name, dir_name)
            self.num += 1
            i += 1
        self.num = 0

        # 下载视频
        i = 0
        while i < length:
            video_big_list_len = len(video_big_list[i])
            self.num += 1
            self.download_data(video_big_list_len, video_big_list[i], id, category_name, dir_name)
            i += 1
        self.num = 1

    def download_data(self, list_length, list, id, category_name, dir_name, *args):
        data = ''
        k = 0
        while k < list_length:
            data_url = list[k]
            if data_url == 'N':
                break
            # print data_url
            # 提取url,把400X400之类的分辨率限制去掉.
            img_url_obj = re.compile(r'(//(img|cloud).*?\.(jpg|png|SS2|gif|mp4))', re.S)
            img_url_list = img_url_obj.findall(data_url)
            url = img_url_list[0][0]

            img_url = "http:" + url
            name = '评论' + str(self.num)
            if args:
                name = args[0]

            # taobao_multimedia_datas/女装/女装连衣裙1/id/评论/name        /id+name
            path = "taobao_multimedia_datas/%s/%s/%s/评论/" % (category_name, dir_name, id)
            print '\n---------', name
            print path
            if (not (os.path.exists(path))):
                os.makedirs(path)

            # 后缀名
            format = img_url[-4:]
            # print format
            # print '-----------------',self.num
            img_name = name + '_' + str(k + 1)
            print '当前评论共%s张图　第%s张图url: %s' % (list_length, k + 1, img_url)
            print "正在请求第%s条评论, 共%s条评论" % (self.num, self.count)

            self.change_ua()
            self.change_ip()
            try:
                response = requests.get(img_url, headers=self.headers, proxies=self.proxy)
                if response.status_code == 200:
                    data = response.content
                    # print self.headers
                    # print self.proxy

            except Exception as e:
                print '数据请求失败...正在重试......', e
                self.log(str(e))
                with open('request.log', 'a') as f:
                    f.write('%s [代理]请求失败%s - %s\n' % (img_url, id, time.ctime()))
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
                            response = requests.get(img_url, headers=self.headers, proxies=self.proxy)
                            if response.status_code == 200:
                                data = response.content
                                with open('request.log', 'a') as f:
                                    f.write('%s 重新请求成功%s - %s\n' % (img_url, id, time.ctime()))
                                print ('[INFO]:重发请求成功!!!!!!!!!!')
                                break
                        except:
                            with open('request.log', 'a') as f:
                                f.write('%s 重新请求失败, 继续重试...%s - %s\n' % (img_url, id, time.ctime()))
                            print ('[INFO]:重发请求失败!!!!!!!!!!')
                            print '第%s次重复请求失败! 继续重试...' % i
                            continue

                    if response.status_code == 200:
                        with open('request.log', 'a') as f:
                            f.write('%s 最终请求成功!!!!!%s - %s\n' % (img_url, id, time.ctime()))
                        print ('[INFO]:重发请求成功!!!!!!!!!!')
                    else:
                        with open('request.log', 'a') as f:
                            f.write('%s 最终请求失败! ! ! ! !%s - %s\n' % (img_url, id, time.ctime()))
                        print ('[INFO]:重发请求失败!!!!!!!!!!')

            print "正在保存　%s" % img_name
            with open(path + img_name + format, 'wb') as f:
                # print '******************',res
                f.write(data)
                # --------------------------------------------------------------------------------------
            # print '当前评论共%s张图　第%s张图url: %s' % (list_length, k + 1, img_url)
            time.sleep(0)
            k += 1
            # print "[INFO]: %s商品所有评论内容已抓取完成！！\n" % (id)
            # return save()

    def log(self, msg):
        self.mutex.acquire()
        self.__file_log.write(msg.encode('utf-8'))
        self.__file_log.write(u'\n'.encode('utf-8'))
        self.mutex.release()


if __name__ == '__main__':
    tc = Taobao_Comment()
    id = '521435492569' # 521435492569 560301942354
    category_name = 'LHZ_0222'
    dir_name = '生活用品_家居用品'
    tc.comment(id, category_name, dir_name)
    print "[INFO]: %s商品所有评论内容已抓取完成！！\n" % (id)

