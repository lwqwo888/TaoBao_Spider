# coding=utf-8
import re
import os
import time
import requests
from lxml import etree
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def find_last(string, str):
    last_position = -1
    while True:
        # 在string字符串的last_position+1下标后面找不到str会返回-1
        position = string.find(str, last_position + 1)
        # print position
        if position == -1:
            return last_position
        last_position = position

url = "https://detail.tmall.com/item.htm?&id=521310943964"
headers = {
    'authority': 'detail.tmall.com',
    'method': 'GET',
    # 'path':"/item.htm?spm=608.7065813.ne.1.128f6324pjwY0E&id=557200845972&tracelog=jubuybigpic&sku_properties=20509':28314",
    'scheme': "https",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "zh-CN,zh;q=0.9",
    'cache-control': "max-age=0",
    'cookie': "cna=XTyQEoI1uE4CAXBfh3IMFSpJ; cq=ccp%3D1; t=4d814acaeff7745d2b1df5c531cb7227; _tb_token_=3eb56ee77e988; cookie2=17B3F5F8A0D9CB4142FFBB0733EC948B; pnm_cku822=098%23E1hvApvUvbpvjQCkvvvvvjiPPL5wljtVP25hgjivPmPy1jYRRsdvzjiRR2z91jQPvpvhvvvvvvhCvvOvUvvvphvEvpCWh8%2Flvvw0zj7OD40OwoAQD7zheutYvtxr1RoKHkx%2F1RBlYb8rwZBleExreE9aWXxr1noK5FtffwLyaB4AVAdyaNoxdX3z8ikxfwoOddyCvm9vvvvvphvvvvvv96Cvpv9hvvm2phCvhRvvvUnvphvppvvv96CvpCCvkphvC99vvOC0B4yCvv9vvUvQud1yMsyCvvpvvvvviQhvCvvv9UU%3D; isg=ArOzZnnX7QJos6HBeuocdKfGQrcdQCLrPU38GWVQTFIJZNMG7bjX-hH2aqJx",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
}
html = requests.get(url, headers=headers).text
# print html
res = etree.HTML(html)
res_list = res.xpath('''//*//div[@class="tb-skin"]//dl/dd/ul/li/a/@style|//*//div[@class="tb-skin"]//dl/dd/ul/li/a[@style]/span/text()''')
print res_list

err_url = "background:url(//gd4.alicdn.com/imgextra/i3/1063738923/TB2qHFLXjgy_uJjSZSyXXbqvVXa_!!1063738923.jpg_30x30.jpg) center no-repeat;"
index_num = find_last(err_url, "_")
str1 = err_url[:index_num]
print str1
img_url_obj = re.compile(r'background:url\((.*?)', re.S)
img_url_list = img_url_obj.findall(str1)
print img_url_list
print str1.split("(")[1]
name = "图片文件"
id = "123456"
path = "img/%s/%s/" % (id, name)
if (not (os.path.exists(path))):
    os.makedirs(path)