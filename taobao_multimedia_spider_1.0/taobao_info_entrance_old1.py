# coding=utf-8
# 通过html抓取商品尺码和颜色
import re
import os
from pvs_find_stock import Skuid_Color
from get_pvs import PVS
import requests
from lxml import etree
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def property_count(id, category_name, dir_name):
    path = "taobao_multimedia_datas/%s/%s/%s/商品详情/" % (category_name, dir_name, id)
    # print path
    if (not (os.path.exists(path))):
        os.makedirs(path)
    url = 'https://detail.tmall.com/item.htm?&id=%s' % id
    headers = {
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
    html = requests.get(url, headers=headers).text
    # print html
    res = etree.HTML(html)
    product_parameters_list = []
    title = res.xpath('/html/head/title/text()')[0]
    product_parameters_list.append(id)
    product_parameters_list.append('< 商品标题 >')
    product_parameters_list.append(title)
    product_parameters_list.append('-'*50)
    # 统计有多少个需要用到的商品属性分类
    content = res.xpath('''//*//div[@class="tb-skin"]//dl//dd/ul[@data-property]''')

    # 商品属性分类数
    property_count = len(content)
    i = 1
    j = 1
    x = 1
    y = 0
    product_attributes = []
    big_list = []
    data_property_list = []
    data_pvs_list = []
    data_property_dict = {}

    # 获取页面所有属性分类名
    product_parameters_list.append('< 商品属性分类 >')
    while x <= property_count:
        # 分类名
        xpath_str = '''//*//div[@class="tb-skin"]//dl[%s]/dt//text()''' % str(x)
        content = res.xpath(xpath_str)
        for con in content:
            product_attributes.append(con)
            product_parameters_list.append(con)

        x += 1
    product_parameters_list.append('-' * 50)

    # 获取页面所有属性详细信息
    while i <= property_count:
        xpath_str = '''//*//dl[%s]//dd/ul/li//span//text()''' % str(i)
        size_list = res.xpath(xpath_str)
        big_list.append(size_list)
        print size_list
        # 尺码数量
        for size_l in size_list:
            data_property_list.append(size_l)
        i += 1

    # 商品属性详细分类
    product_parameters_list.append('< 商品属性详细分类 >')
    content_length = len(product_attributes)
    while y < content_length:
        info_str = product_attributes[y] + ': ' + ', '.join(big_list[y])
        print info_str
        print '-+-+-+-+-+-+-+-+-+-'
        product_parameters_list.append(info_str)
        y += 1
    product_parameters_list.append('-' * 50)

    # 获取页面中所有pvs
    while j <= property_count:
        xpath_str = '''//*//dl[%s]//dd/ul/li/@data-value''' % str(j)
        pvs_list = res.xpath(xpath_str)
        # pvs值
        for value in pvs_list:
            data_pvs_list.append(value)
        j += 1

    # 循环将两个列表中的型号和pvs读取出来存入一个列表，再循环以键值的方式写入字典
    all_data_list = [x for x in zip(data_property_list, data_pvs_list)]
    for size, color in all_data_list:
        data_property_dict[size] = color
    Product_attributes_list, pvs_list = PVS().pvs(property_count, big_list, data_property_dict)
    for i in Product_attributes_list:
        print i
    stock_list = Skuid_Color().skuid_num(id, pvs_list)
    commodity_stock_list = [x for x in zip(Product_attributes_list, stock_list)]
    product_parameters_list.append('< 商品分类组合 >')
    for product_attributes, sellableQuantity in commodity_stock_list:
        product_parameters_list.append(product_attributes + '的库存数量为：' + sellableQuantity)
    product_parameters_list.append('-' * 50)

    # 商品详情介绍
    details_description = res.xpath('''/html/body/div[@id="page"]/div[@id="content"]/div[@id="bd"]//div[@id="attributes"]//ul//li//text()''')
    product_parameters_list.append('< 产品参数 >')
    for i in details_description:
        parameter = i.replace('\t', '').replace('\r', '').replace('\n', '')
        product_parameters_list.append(parameter)

    for product_parameters in product_parameters_list:
        # print product_parameters
        with open(path + '淘宝产品参数.txt', 'a') as f:
            f.write(product_parameters + '\r\n')


def url_process(url):
    res = re.compile(r'(\?|&)id=(\d+).*?', re.S)
    id = res.search(url).group(2)
    return ''.join(id)

# if __name__ == '__main__':
#
#     # url = raw_input('请输入您要查看的淘宝商品链接:')
#     with open('taobaourl.txt', 'rb') as f:
#         lines = f.readlines()
#     id = '560538155798'
#     category_name = '手机'
#     dir_name = '手机1'
#     property_count(id, category_name, dir_name)
#     # for line in lines:
#     #     id = url_process(line)
#     #     property_count(id, category_name, dir_name)
#     print '\n'