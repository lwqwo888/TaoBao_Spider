# coding=utf-8
# 根据商品ID获取商品参数
import json
import re
import sys
import time

import jsonpath
import requests

import size_class
from size_color_skuid_formal import Skuid_Color

reload(sys)
sys.setdefaultencoding('utf-8')

class Taobao_Cuckoo(object):
    def __init__(self):
        pass

    def retrieve_data(self, id, size):
        size_color_dict, skuid_dict = Skuid_Color().skuid_num(id)
        color_list = size_color_dict[size]
        color_list = color_list.split(' ')
        # length = len(color_list)
        # new_color_list = []
        # i = 0
        # while i < length:
        #     number = str(i+1)
        #     new_color_list.append(number + '-' + color_list[i])
        #     i += 1
        return '  '.join(color_list), skuid_dict

    def main(self, id, skuid_dict, size_color):
        t = time.time()
        times = (int(round(t * 1000)))

        skuId = skuid_dict[size_color]
        # url参数中必须要有callback参数
        url = '''https://mdskip.taobao.com/core/initItemDetail.htm?cachedTimestamp=%s&itemId=%s&callback=setMdskip&timestamp=%s''' % (str(times-315000), id, str(times))
        # url = '''https://mdskip.taobao.com/core/initItemDetail.htm?cartEnable=true&queryMemberRight=true&cachedTimestamp=%s&itemId=%s&callback=setMdskip&timestamp=%s''' % (str(times-315000), id, str(times))
        # url = '''https://mdskip.taobao.com/core/initItemDetail.htm?cartEnable=true&queryMemberRight=true&isSecKill=false&cachedTimestamp=%s&isAreaSell=false&isForbidBuyItem=false&service3C=false&isPurchaseMallPage=false&itemId=%s&isUseInventoryCenter=false&addressLevel=2&offlineShop=false&isRegionLevel=false&household=false&showShopProm=false&isApparel=true&sellerPreview=false&callback=setMdskip&timestamp=%s&isg=null&isg2=AtjYd2VcNuKz1Bl5_wUsFM5yqQaqaT1Pr_CqmBLKjZPGrXiXutEM2-7NkdNm'''%(str(times-315000), id, str(times))'''
        # url = 'https://detail.tmall.com/item.htm?spm=a230r.1.14.154.29b70e2cmQb92Y&id=563134951881&ns=1&abbucket=15'
        headers = {
            # "authority": "mdskip.taobao.com",
            # "method": "GET",
            # "path": "/core/initItemDetail.htm?cartEnable=true&queryMemberRight=true&tmallBuySupport=true&tryBeforeBuy=false&isSecKill=false&cachedTimestamp=1515846164558&isAreaSell=false&isForbidBuyItem=false&service3C=false&isPurchaseMallPage=false&itemId=557200845972&isUseInventoryCenter=false&addressLevel=2&offlineShop=false&isRegionLevel=false&household=false&showShopProm=false&isApparel=true&sellerPreview=false&callback=setMdskip&timestamp=1515847105682&isg=null&isg2=AtjYd2VcNuKz1Bl5_wUsFM5yqQaqaT1Pr_CqmBLKjZPGrXiXutEM2-7NkdNm",
            # "scheme": "https",
            # "accept": "*/*",
            # "accept-encoding": "gzip, deflate, br",
            # "accept-language": "zh-CN,zh;q=0.9",
            "cookie": "miid=1416914392893341000; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; tracknick=%5Cu6211%5Cu6210%5Cu4F60%5Cu5669%5Cu68A6; _cc_=Vq8l%2BKCLiw%3D%3D; tg=0; l=ArS04f0dgYQRMtMqetwpb6bSBHkmodh3; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1; cna=5w2/EagEn1sCAbcnVm41KZrQ; t=41a78c0d4f8236cec127e49a3a1d7668; _m_h5_tk=22cd676b46cffe81b7111f72345a4001_1515316266867; _m_h5_tk_enc=594d3f94ed8fe96523affc4889339ae4; enc=LUFqvB76IYLq0NOBSAnqkWEGqx3%2BVDxCaFTpeHTRbd0shSzi6kJ4TKcjRtCKKhB5vGwnjUQpJXJWux06z0QC5w%3D%3D; cookie2=13A91D312332FF9E6F9441B09BD42AEF; v=0; _tb_token_=f385ee7fb8e5b; mt=ci%3D-1_1; isg=BEpKIf4uJNw9j6sTmsbzTbXNmzAsk8-R8Wr4btSFcR3_h-1BvMnkp5C_k_Nbd0Yt",
            "referer": "https://detail.tmall.com/item.htm?spm=a230r.1.14.1.29b70e2cmQb92Y&id=%s&ns=1&abbucket=13"%id,
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        }
        html = requests.get(url, headers=headers).text
        # print '库存数据',html
        res = re.compile(r'setMdskip\n\((.*?)\)', re.S)
        str_list = res.findall(html)
        # 指定商品库存
        for i in str_list:
            json_str1 = json.loads(i)
            # print json_str1
            json_res = jsonpath.jsonpath(json_str1, expr='$..inventoryDO.skuQuantity.%s.quantity'%skuId)
            # 库存
            for num in json_res:
                print '%s码  %s  剩余件数: %s' % (size, color, num)

        # for i in str_list:
        #     json_str1 = json.loads(i)
        #     print json_str1
        #     json_res = jsonpath.jsonpath(json_str1, expr='$..itemPriceResultDO.priceInfo.%s.suggestivePromotionList..price'%skuId)
        #     # 指定商品价格
        #     print json_res
        # 指定店铺详细
        # 'https://hdc1.alicdn.com/asyn.htm?pageId=1303352866&userId=645039969'

    def url_process(self, url):
        res = re.compile(r'&id=(\d+).*?', re.S)
        id = res.findall(url)
        return ''.join(id)

    # def color_classified(self, num):
    #     if num == number or num == color_list[i]:

if __name__ == '__main__':

    tc = Taobao_Cuckoo()
    url = raw_input('请输入您要查看的淘宝商品链接:')
    # '557200845972'
    url = 'https://detail.tmall.com/item.htm?spm=608.7065813.ne.1.128f6324pjwY0E&id=557200845972&tracelog=jubuybigpic'
    id = tc.url_process(url)
    size_list = size_class.size_count(id)
    size_list = '  '.join(size_list)
    print '此件商品的尺码选择范围: %s' % size_list
    size = raw_input('请输入您要查看的尺码:')
    size = size.upper()
    color_list, skuid_dict = tc.retrieve_data(id, size)
    print '此件商品的颜色选择范围: %s' % color_list
    color = raw_input('请输入您要查看的颜色:')
    # color = tc.color_classified(num)
    size_color = size + color
    tc.main(id, skuid_dict, size_color)