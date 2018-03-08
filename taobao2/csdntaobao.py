# coding=utf-8

import requests

import re, sys, os
import json
import threading
import pprint
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class spider:
    def __init__(self, sid, name):

        self.id = sid
        self.headers = {"Accept": "text/html,application/xhtml+xml,application/xml;",
                        "Accept-Encoding": "gzip",
                        "Accept-Language": "zh-CN,zh;q=0.8",
                        "Referer": "https://www.example.com/",
                        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"
                        }

        self.name = name

    def openurl(self, url):

        self.request = requests.get(url, headers=self.headers)
        if self.request.ok:
            return self.request.text

    def matchs(self):

        tmall_exp = r"Setup\(([\s\S]+?)\);"  ### 匹配商品数据的正则
        detail = r"src=\"(https://img\S+?[jpgifn]+?)\""  ###匹配 商品详情图的正则
        html = self.openurl("https://detail.tmall.com/item.htm?id=%s" % self.id)
        data = re.findall(tmall_exp, html)
        print('-----------------------------------------',data)
        data = json.loads(data[0])
        main_img = data['propertyPics']  ## 这里包括了主图和颜色图的地址
        color_data = data['valItemInfo']['skuList']  ### 这里获得商品的颜色信息列表   包括颜色编码  颜色名称,商品skuID
        print ('*******************************************',color_data)
        detail_html = self.openurl("http:" + data['api']["httpsDescUrl"])
        detail_image = re.findall(detail, detail_html)
        self.newdata = {"MAIN": main_img['default'], "DETAIL": detail_image, "id": self.id, }

        psvs = []
        self.newdata['COLOR'] = []

        for v in range(len(color_data)):
            if ";" in color_data[v]["pvs"]:
                psv = color_data[v]['pvs'][color_data[v]['pvs'].find(";") + 1:]
            else:
                psv = color_data[v]['pvs']
            if psv in psvs:
                continue
            psvs.append(psv)

            self.newdata['COLOR'].append({color_data[v]["names"]: main_img[";" + psv + ";"]})

        pprint.pprint(self.newdata)

        return self.newdata

    def download(self):
        if len(self.newdata) > 0:
            for x in range(len(self.newdata['MAIN'])):
                threading.Thread(target=self.download_main, args=(self.newdata['MAIN'][x], x)).start()

            for x in self.newdata['COLOR']:
                threading.Thread(target=self.download_color, args=(x,)).start()
            for x in range(len(self.newdata['DETAIL'])):
                threading.Thread(target=self.download_detail, args=(self.newdata['DETAIL'][x], x)).start()
        return

    def download_main(self, url, index):
        try:
            img = requests.get("http:" + url, stream=True, headers=self.headers, timeout=10)

        except:
            print(sys.exc_info())
            return
        if img.ok:
            if not os.path.exists(self.name + "/main"):
                try:
                    os.makedirs(self.name + "/main")
                except:
                    pass
            imgs = open(self.name + "/main/%s.jpg" % index, "wb")
            imgs.write(img.content)
            imgs.close()

    def download_color(self, url):

        try:
            img = requests.get("http:" + url[list(url.keys())[0]][0], stream=True, headers=self.headers, timeout=10)

        except:
            print(sys.exc_info())
            return
        if img.ok:
            if not os.path.exists(self.name + "/color"):
                try:
                    os.makedirs(self.name + "/color")
                except:
                    pass
            if "/" in list(url.keys())[0]:
                color = list(url.keys())[0].replace("/", "_")
            elif "\\" in list(url.keys())[0]:
                color = list(url.keys())[0].replace("\\", "_")
            else:
                color = list(url.keys())[0]
            imgs = open(self.name + "/color/%s.jpg" % color, "wb")
            imgs.write(img.content)
            imgs.close()

    def download_detail(self, url, index):

        try:
            img = requests.get(url, stream=True, headers=self.headers, timeout=10)

        except:
            print(sys.exc_info())
            return
        if img.ok:
            if not os.path.exists(self.name + "/detail"):
                try:
                    os.makedirs(self.name + "/detail")
                except:
                    pass

            imgs = open(self.name + "/detail/%s.jpg" % index, "wb")
            imgs.write(img.content)

            imgs.close()


if __name__ == "__main__":
    sid = 562441235623  ## 这里输入天猫宝贝ID

    taobao = spider(sid, "下载图片/T")

    taobao.matchs()

    taobao.download()
