# coding=utf-8
# 通过pvs直接找库存
# 优点：速度稍快
# 缺点：无货商品库存没有体现，需手动置0或置为＂无货＂
import re
import time
import random
import requests
import linecache
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class Skuid_Color(object):
    def __init__(self):
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
            # # 要访问的目标页面
            # targetUrl = "http://httpbin.org/ip"

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

            proxies = {
                "http": proxyMeta,
                "https": proxyMeta,
            }

            # tunnel = random.randint(1, 10000)
            # headers = {"Proxy-Tunnel": str(tunnel)}
            # resp = requests.get(targetUrl, proxies=proxies, headers=headers)
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


    def skuid_num(self, id, pvs_list):
        html = ""
        url = 'https://detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm?itemId=%s&modules=dynStock&callback=onSibRequestSuccess'%id
        # headers = {
        #
        #     "cookie": "ubn=p; ucn=unsz; t=28edc35882e1fcf06bfaa67008da2a8f; cna=XTyQEoI1uE4CAXBfh3IMFSpJ; thw=cn; miid=6347655561018672771; uc3=sg2=WqIrBf2WEDhnXgIg9lOgUXQnkoTeDo019W%2BL27EjCfQ%3D&nk2=rUs9FkCy6Zs6Ew%3D%3D&id2=VWeZAHoeqUWF&vt3=F8dBzLgoJIN4WC0X30I%3D&lg2=VFC%2FuZ9ayeYq2g%3D%3D; lgc=%5Cu6211%5Cu6210%5Cu4F60%5Cu5669%5Cu68A6; tracknick=%5Cu6211%5Cu6210%5Cu4F60%5Cu5669%5Cu68A6; _cc_=WqG3DMC9EA%3D%3D; tg=0; enc=GtOY%2B8mhUi7LXIrV9LqmUl0PYsVpr9BbSzEB9GL%2Fq3i6Czwxxh5mE60CMJjep9GIq4iV04PvQsAGhzOIdrf6iw%3D%3D; mt=ci=-1_0; UM_distinctid=160fe373fd7c89-0f04cad75d123e-393d5f0e-1fa400-160fe373fd8e5a; hng=CN%7Czh-CN%7CCNY%7C156; _m_h5_tk=081b6ec244bfd7ba155325c85a14056e_1516103738466; _m_h5_tk_enc=8531a9b39cfb4a076e45dfad1fba7525; cookie2=16e0f40738dc82c43c53992cb5a26ebb; _tb_token_=3daeebbb3768e; v=0; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; uc1=cookie14=UoTdfYT5TUo4kA%3D%3D; isg=BDo6USLQNOpL5rgFeJZzPiuWi2CcQ9uEDF5FrkQyJ02YN9lxLHiA1B8ng8PrpzZd",
        #     "referer": "https://item.taobao.com/item.htm?spm=a219r.lmn002.14.174.6f516358W81jq9&id=%s&ns=1&abbucket=16"%id,
        #     "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
        #
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
        stock_list = []
        for pvs in pvs_list:
            res = re.compile(r'%s.*?"sellableQuantity":(.*?),'%pvs, re.S)
            single_stock = res.findall(html)
            if single_stock:
                stock_list.append(''.join(single_stock))
            else:
                stock_list.append(0)
        return stock_list


