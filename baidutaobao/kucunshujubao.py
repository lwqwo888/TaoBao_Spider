# coding=utf-8
# 根据商品ID获取商品参数(skuid,库存，价格)
import re
import time
import json
import jsonpath
import requests


import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Taobao_Cuckoo(object):
    def __init__(self):
        pass

    def main(self, id, skuid):
        t = time.time()
        times = (int(round(t * 1000)))

        # url参数中必须要有callback参数,不要xmpPromotion是聚划算，fqg也是垃圾数据
        url = '''https://detailskip.taobao.com/service/getData/1/p2/item/detail/sib.htm?itemId=557200845972&modules=qrcode,viewer,price,contract,duty,xmpPromotion,dynStock,delivery,upp,sellerDetail,activity,fqg,zjys,coupon&callback=onSibRequestSuccess'''

        headers = {

            "cookie": "miid=1416914392893341000; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; tracknick=%5Cu6211%5Cu6210%5Cu4F60%5Cu5669%5Cu68A6; _cc_=Vq8l%2BKCLiw%3D%3D; tg=0; l=ArS04f0dgYQRMtMqetwpb6bSBHkmodh3; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1; cna=5w2/EagEn1sCAbcnVm41KZrQ; t=41a78c0d4f8236cec127e49a3a1d7668; _m_h5_tk=22cd676b46cffe81b7111f72345a4001_1515316266867; _m_h5_tk_enc=594d3f94ed8fe96523affc4889339ae4; enc=LUFqvB76IYLq0NOBSAnqkWEGqx3%2BVDxCaFTpeHTRbd0shSzi6kJ4TKcjRtCKKhB5vGwnjUQpJXJWux06z0QC5w%3D%3D; cookie2=13A91D312332FF9E6F9441B09BD42AEF; v=0; _tb_token_=f385ee7fb8e5b; mt=ci%3D-1_1; isg=BEpKIf4uJNw9j6sTmsbzTbXNmzAsk8-R8Wr4btSFcR3_h-1BvMnkp5C_k_Nbd0Yt",
            "referer": "https://item.taobao.com/item.htm?id=557200845972",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        }
        html = requests.get(url, headers=headers).text
        print '库存数据',html
        res = re.compile(r'setMdskip\n\((.*?)\)', re.S)
        str_list = res.findall(html)
        # 指定商品库存
        for i in str_list:
            json_str1 = json.loads(i)
            # print json_str1
            json_res = jsonpath.jsonpath(json_str1, expr='$..inventoryDO.skuQuantity.%s.quantity'%skuid)
            # 库存
            if not json_res:
                json_res = jsonpath.jsonpath(json_str1, expr='$..inventoryDO.icTotalQuantity')
            print json_res


if __name__ == '__main__':

    tc = Taobao_Cuckoo()
    id = '557200845972'
    skuid = '3554339929557'
    tc.main(id, skuid)
