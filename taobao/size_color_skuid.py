# coding=utf-8
import json
import re
import sys

import requests
from lxml import etree

import size_class

reload(sys)
sys.setdefaultencoding('utf-8')



id = '557200845972'
skuId = '3618163606223'
size_list = size_class.size_count(id)
size_list_len = len(size_list)
print size_list
print size_list_len
url = 'https://detail.tmall.com/item.htm?&id=%s'%id
# url = 'https://detail.tmall.com/item.htm?spm=a230r.1.14.154.29b70e2cmQb92Y&id=563134951881&ns=1&abbucket=15'
headers = {
    'authority':'detail.tmall.com',
    'method':'GET',
    'path':"/item.htm?spm=608.7065813.ne.1.128f6324pjwY0E&id=557200845972&tracelog=jubuybigpic&sku_properties=20509':28314",
    'scheme':"https",
    'accept':"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'accept-encoding':"gzip, deflate, br",
    'accept-language':"zh-CN,zh;q=0.9",
    'cache-control':"max-age=0",
    'cookie':"cna=XTyQEoI1uE4CAXBfh3IMFSpJ; cq=ccp%3D1; t=4d814acaeff7745d2b1df5c531cb7227; _tb_token_=3eb56ee77e988; cookie2=17B3F5F8A0D9CB4142FFBB0733EC948B; pnm_cku822=098%23E1hvApvUvbpvjQCkvvvvvjiPPL5wljtVP25hgjivPmPy1jYRRsdvzjiRR2z91jQPvpvhvvvvvvhCvvOvUvvvphvEvpCWh8%2Flvvw0zj7OD40OwoAQD7zheutYvtxr1RoKHkx%2F1RBlYb8rwZBleExreE9aWXxr1noK5FtffwLyaB4AVAdyaNoxdX3z8ikxfwoOddyCvm9vvvvvphvvvvvv96Cvpv9hvvm2phCvhRvvvUnvphvppvvv96CvpCCvkphvC99vvOC0B4yCvv9vvUvQud1yMsyCvvpvvvvviQhvCvvv9UU%3D; isg=ArOzZnnX7QJos6HBeuocdKfGQrcdQCLrPU38GWVQTFIJZNMG7bjX-hH2aqJx",
    'upgrade-insecure-requests':"1",
    'user-agent':"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
}
html = requests.get(url, headers=headers).text
# print html
res = etree.HTML(html)
# 解析出尺码,颜色,skuid数据,并去空格
ron = res.xpath('''/html/body/div[@id='page']/div[@id="content"]/div[@id="detail"]//div[@class="tm-clear"]/script[3]//text()''')

data = ''.join(ron)
res = re.compile(r'"skuList":\[(.*?)\],', re.S)
data = res.findall(data)
str_data = ''.join(data).replace(' ', '')
print str_data
size_color_dict = {}
skuid_dict = {}
i = 0
while i < size_list_len:
    # 匹配出所有对应该尺码的颜色
    print size_list[i]
    color_res = re.compile(r'"names":"%s(.*?)",' % size_list[i], re.S)
    color_data = color_res.findall(str_data)
    color_len = len(color_data)
    # 把尺码对应颜色存入字典
    # for x in color_data:
    #     size_color_dict[size_list[i]+x] = x
    j = 0
    while j < color_len:
        # 尺码加颜色
        size_color = size_list[i] + color_data[j]
        sku_res = re.compile(r'"names":"%s",.*?"skuId":"(.*?)"}' % size_color, re.S)
        # 符合当前尺码颜色的skuid
        skuid_data = sku_res.findall(str_data)
        # print size_color, ''.join(skuid_data)
        # 把对应当前尺码颜色的skuid存入字典
        skuid_dict[size_color] = ''.join(skuid_data)
        j += 1
    i += 1
# new_size_color_dict = json.dumps(size_color_dict, encoding="UTF-8", ensure_ascii=False)
new_skuid_dict = json.dumps(skuid_dict, encoding="UTF-8", ensure_ascii=False)
# print new_size_color_dict
print new_skuid_dict
