# coding=utf-8
# 通过html抓取商品尺码和颜色
import re
import requests
from lxml import etree
from pvs import PVS
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def property_count(id):
    id = '563394241094'
    url = 'https://detail.tmall.com/item.htm?&id=%s'%id
    # url = 'https://detail.tmall.com/item.htm?spm=a230r.1.14.154.29b70e2cmQb92Y&id=563134951881&ns=1&abbucket=15'
    headers = {
        'authority':'detail.tmall.com',
        'method':'GET',
        # 'path':"/item.htm?spm=608.7065813.ne.1.128f6324pjwY0E&id=557200845972&tracelog=jubuybigpic&sku_properties=20509':28314",
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
    print html
    res = etree.HTML(html)
    # 统计有多少个需要用到的商品属性分类
    content = res.xpath('''//*//div[@class="tb-skin"]//dl//dd/ul[@data-property]''')
    # 商品属性分类数
    property_count = len(content)
    print property_count
    i = 1
    j = 1
    x = 1
    big_list = []
    data_property_list = []
    data_pvs_list = []
    data_property_dict = {}
    # 获取页面所有属性分类
    while x <= property_count:
        # 分类名
        xpath_str = '''//*//div[@class="tb-skin"]//dl[%s]/dt//text()''' % str(x)
        content = res.xpath(xpath_str)
        # for con in content:
            # print con
        x += 1

    # 获取页面所有属性详细信息
    while i <= property_count:
        xpath_str = '''//*//dl[%s]//dd/ul/li//span//text()''' % str(i)
        size_list = res.xpath(xpath_str)
        big_list.append(size_list)
        big_list_len = len(big_list)
        # print test
        # 尺码数量
        for size_l in size_list:
            data_property_list.append(size_l)
            size_length = len(data_property_list)
            print size_l
        # 根据分类名数量，创建相应数量的列表
        i += 1
    # 获取页面中所有pvs
    while j <= property_count:
        xpath_str = '''//*//dl[%s]//dd/ul/li/@data-value''' % str(j)
        pvs_list = res.xpath(xpath_str)
        # pvs值
        for value in pvs_list:
            data_pvs_list.append(value)
            pvs_length = len(data_pvs_list)
            # print value
        j += 1
    # 循环将两个列表中的型号和pvs读取出来存入一个列表，再循环以键值的方式写入字典
    all_data_list = [x for x in zip(data_property_list, data_pvs_list)]
    for size, color in all_data_list:
        data_property_dict[size] = color
    for key in data_property_dict:
        print key, '---', data_property_dict[key]

    pvs_list = PVS().pvs(property_count, big_list, data_property_dict)
    for li in pvs_list:
        print li
property_count('c')