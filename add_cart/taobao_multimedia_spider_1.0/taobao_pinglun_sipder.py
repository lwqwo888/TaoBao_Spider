# coding=utf-8
# 通过pvs直接找库存
# 优点：速度稍快
# 缺点：无货商品库存没有体现，需手动置0或置为＂无货＂
import re
import os
import time
import json
import jsonpath
import requests
import threading
import sys
reload(sys)
sys.setdefaultencoding('utf-8')



class Taobao_Comment(object):
    def __init__(self):
        current_path = os.path.split(os.path.realpath(__file__))[0]
        current_path = current_path + '/log'
        if (not (os.path.exists(current_path))):
            os.makedirs(current_path)
        print current_path
        self.__file_log = open('%s/comment_log%s.txt' % (current_path, time.strftime('%Y_%m_%d')), 'a+')
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
        self.num = 1

    def comment(self, id, category_name, dir_name):

        # 不携带currentPageNum参数看不到数据,不携带rateType参数数据顺序会乱
        url = 'https://rate.taobao.com/feedRateList.htm?auctionNumId=%s&currentPageNum=1&rateType=3' % id
        headers = {

            "cookie": "ubn=p; ucn=unsz; t=28edc35882e1fcf06bfaa67008da2a8f; cna=XTyQEoI1uE4CAXBfh3IMFSpJ; thw=cn; miid=6347655561018672771; uc3=sg2=WqIrBf2WEDhnXgIg9lOgUXQnkoTeDo019W%2BL27EjCfQ%3D&nk2=rUs9FkCy6Zs6Ew%3D%3D&id2=VWeZAHoeqUWF&vt3=F8dBzLgoJIN4WC0X30I%3D&lg2=VFC%2FuZ9ayeYq2g%3D%3D; lgc=%5Cu6211%5Cu6210%5Cu4F60%5Cu5669%5Cu68A6; tracknick=%5Cu6211%5Cu6210%5Cu4F60%5Cu5669%5Cu68A6; _cc_=WqG3DMC9EA%3D%3D; tg=0; enc=GtOY%2B8mhUi7LXIrV9LqmUl0PYsVpr9BbSzEB9GL%2Fq3i6Czwxxh5mE60CMJjep9GIq4iV04PvQsAGhzOIdrf6iw%3D%3D; mt=ci=-1_0; UM_distinctid=160fe373fd7c89-0f04cad75d123e-393d5f0e-1fa400-160fe373fd8e5a; hng=CN%7Czh-CN%7CCNY%7C156; _m_h5_tk=081b6ec244bfd7ba155325c85a14056e_1516103738466; _m_h5_tk_enc=8531a9b39cfb4a076e45dfad1fba7525; cookie2=16e0f40738dc82c43c53992cb5a26ebb; _tb_token_=3daeebbb3768e; v=0; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; uc1=cookie14=UoTdfYT5TUo4kA%3D%3D; isg=BDo6USLQNOpL5rgFeJZzPiuWi2CcQ9uEDF5FrkQyJ02YN9lxLHiA1B8ng8PrpzZd",
            "referer": "https://item.taobao.com/item.htm?spm=a219r.lmn002.14.174.6f516358W81jq9&id=561495525977&ns=1&abbucket=16",
            "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",

        }
        html = requests.get(url, headers=headers).text
        # html = str(html)
        html = html.strip()
        html = html.strip("()")
        res = json.loads(html)
        # 所有评论日期
        str_date = jsonpath.jsonpath(res, expr='$..comments[*].date')
        # 获取所有评论人
        str_name = jsonpath.jsonpath(res, expr='$..comments[*].user.nick')
        # 获取所有文字评论,除追加评论外
        str_info = jsonpath.jsonpath(res, expr='$..comments[*].content')
        # 获取所有评论图片,除视频外
        img_data = jsonpath.jsonpath(res, expr='$..comments[*].photos')
        # img_data1 = jsonpath.jsonpath(res, expr='$..comments[2]')
        # for i in img_data1:
        #     print i
        # return
        # 获取所有视频评论
        video_data = jsonpath.jsonpath(res, expr='$..comments[*].video')
        # print str_name, str_date, str_info
        if not str_name:
            return
        comment_data = [x for x in zip(str_name, str_date, str_info)]
        # taobao_multimedia_datas/女装/女装连衣裙1/id/评论/评论内容.txt
        path = "taobao_multimedia_datas/%s/%s/%s/评论/" % (category_name, dir_name, id)
        # print path
        if (not (os.path.exists(path))):
            os.makedirs(path)
        j = 0
        for p, d, i in comment_data:
            j += 1
            with open(path + '评论内容.txt', 'a') as f:
                f.write('评论' + str(j) + ' ' + p + '---' + d + ':' + i + '\n')
                # print p,'---', d, ':',  i

        length = len(img_data)
        print len(img_data)
        # print img_data
        img_big_list = []
        video_big_list = []
        x = 0
        for i in img_data:
            if i is None:
                pass
                # print i
            else:
                img_list = jsonpath.jsonpath(i, expr='$..url')
                print img_list
                if not img_list:
                    expr = '$..comments[%s].appendList..photos..url' % x
                    img_list = jsonpath.jsonpath(res, expr=expr)
                    expr = '$..comments[%s].appendList..content' % x
                    append_str = jsonpath.jsonpath(res, expr=expr)

                    with open(path + '评论内容.txt') as f:
                        lines = f.readlines()
                    with open(path + '评论内容.txt', 'w') as w:
                        for l in lines:
                            print l
                            str1 = '评论%s' % str(x + 1)
                            append_content = '\t--->追加评论内容:%s' % ''.join(append_str)
                            print str1, append_content
                            if (l.startswith(str1)):
                                w.write(l.replace(b'\n', append_content + '\n'))
                            else:
                                w.write(l)
                    print img_list
                img_big_list.append(img_list)
            x += 1
            # print x
        # return
        # print len(video_data)
        # print video_data
        for i in video_data:
            # print i
            if i is None:
                video_big_list.append(list('N'))
            else:
                video_list = jsonpath.jsonpath(i, expr='$.cloudVideoUrl')
                video_big_list.append(video_list)

        # 女装/女装连衣裙1/id/评论/评论1/img(or)video
        i = 0
        while i < length:
            # print img_big_list[i]
            img_big_list_len = len(img_big_list[i])
            self.download_data(img_big_list_len, img_big_list[i], id, category_name, dir_name)
            self.num += 1
            i += 1
        self.num = 0
        i = 0
        while i < length:
            video_big_list_len = len(video_big_list[i])
            self.num += 1
            self.download_data(video_big_list_len, video_big_list[i], id, category_name, dir_name)
            i += 1


    def download_data(self, list_length, list, id, category_name, dir_name):
        k = 0
        while k < list_length:
            data_url = list[k]
            if data_url == 'N':
                break
            # print data_url
            img_url = "http:" + data_url
            name = '评论' + str(self.num)
            # img_url = lines[k].replace('\n', '')
            # cid = str(num) + id
            # taobao_multimedia_datas/女装/女装连衣裙1/id/评论/name        /id+name
            path = "taobao_multimedia_datas/%s/%s/%s/评论/%s/" % (category_name, dir_name, id, name)
            # print name
            # print path
            if (not (os.path.exists(path))):
                os.makedirs(path)

            # 后缀名
            format = img_url[-4:]
            # print format
            # print '-----------------',self.num
            img_name = name + '_' + str(k + 1)
            print "正在请求　%s" % name
            try:
                data = requests.get(img_url, headers=self.headers, proxies=self.proxy).content
            except Exception as e:
                print '数据请求失败...', e
                self.log(str(e))
            print "正在保存　%s" % img_name
            with open(path + img_name + format, 'wb') as f:
                # print '******************',res
                f.write(data)
                # --------------------------------------------------------------------------------------
            print '共%s个　第%s个url: %s' % (list_length, k + 1, img_url)
            time.sleep(0)
            k += 1
        # print "[INFO]: %s商品所有评论内容已抓取完成！！\n" % (id)
        # return save()


if __name__ == '__main__':
    tc = Taobao_Comment()
    id = '563488767927'
    category_name = '女装'
    dir_name = '女装连衣裙1'
    tc.comment(id, category_name, dir_name)
    print "[INFO]: %s商品所有评论内容已抓取完成！！\n" % (id)

