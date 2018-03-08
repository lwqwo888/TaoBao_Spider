# coding=utf-8
# 根据商品ID获取商品参数
import re
import time
import urllib
import requests
from lxml import etree
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

t = time.time()
times = (int(round(t * 1000)))
id = '557200845972'
skuId = '3618163606209'
# 添加到购物车api
# url = 'https://cart.taobao.com/add_cart_item.htm?item_id=557200845972'


# url = urllib.unquote('7e056b706dfe4&')
# print urllib.quote('{"deliveryCityCode":440300,"campaignId":0,"from_etao":"","umpkey":"","items":[{"itemId":"560217830586","skuId":"3664600867959","iChannel":"","quantity":1,"serviceInfo":"","extraAttribute":{}}]}')
add_str = urllib.urlencode({'add':'{"deliveryCityCode":440300,"campaignId":0,"from_etao":"","umpkey":"","items":[{"itemId":"560217830586","skuId":"3664600867959","iChannel":"","quantity":1,"serviceInfo":"","extraAttribute":{}}]}'})
print add_str
# sellerId:卖家ID
# categoryId:类别ID
params = {
    "_tb_token_": "30783b151de8b",
    "tsid": "41a78c0d4f8236cec127e49a3a1d7668",
    "itemId": id,
    "sellerId": "3432882180",
    "categoryId": "50011744",
    "root_refer": "",
    "_ksTS": "1515951261320_1665",
    "callback": "jsonp1666",

}
# print params
params_str = urllib.urlencode(params) + '&' + add_str
print params_str
url = '''https://fbuy.tmall.com/cart/addCartItems.do?''' + params_str
# url = '''https://fbuy.tmall.com/cart/addCartItems.do?_tb_token_=7e056b706dfe4&add=%7B%22deliveryCityCode%22%3A440300%2C%22campaignId%22%3A0%2C%22from_etao%22%3A%22%22%2C%22umpkey%22%3A%22%22%2C%22items%22%3A%5B%7B%22itemId%22%3A%22560217830586%22%2C%22skuId%22%3A%223664600867959%22%2C%22iChannel%22%3A%22%22%2C%22quantity%22%3A1%2C%22serviceInfo%22%3A%22%22%2C%22extraAttribute%22%3A%7B%7D%7D%5D%7D&tsid=4d814acaeff7745d2b1df5c531cb7227&itemId=560217830586&sellerId=3432882180&categoryId=50011744&root_refer=&item_url_refer=&_ksTS=1515999130398_1272&callback=jsonp1273'''
print url
headers = {
    # "authority": "mdskip.taobao.com",
    "method": "GET",
    # "path": "/core/initItemDetail.htm?cartEnable=true&queryMemberRight=true&tmallBuySupport=true&tryBeforeBuy=false&isSecKill=false&cachedTimestamp=1515846164558&isAreaSell=false&isForbidBuyItem=false&service3C=false&isPurchaseMallPage=false&itemId=557200845972&isUseInventoryCenter=false&addressLevel=2&offlineShop=false&isRegionLevel=false&household=false&showShopProm=false&isApparel=true&sellerPreview=false&callback=setMdskip&timestamp=1515847105682&isg=null&isg2=AtjYd2VcNuKz1Bl5_wUsFM5yqQaqaT1Pr_CqmBLKjZPGrXiXutEM2-7NkdNm",
    # "scheme": "https",
    # "accept": "*/*",
    # "accept-encoding": "gzip, deflate, br",
    # "accept-language": "zh-CN,zh;q=0.9",
    'Connection': 'keep-alive',
    "cookie": "t=28edc35882e1fcf06bfaa67008da2a8f; cna=XTyQEoI1uE4CAXBfh3IMFSpJ; thw=cn; miid=6347655561018672771; lgc=%5Cu6211%5Cu6210%5Cu4F60%5Cu5669%5Cu68A6; tracknick=%5Cu6211%5Cu6210%5Cu4F60%5Cu5669%5Cu68A6; tg=0; enc=GtOY%2B8mhUi7LXIrV9LqmUl0PYsVpr9BbSzEB9GL%2Fq3i6Czwxxh5mE60CMJjep9GIq4iV04PvQsAGhzOIdrf6iw%3D%3D; UM_distinctid=160fe373fd7c89-0f04cad75d123e-393d5f0e-1fa400-160fe373fd8e5a; hng=CN%7Czh-CN%7CCNY%7C156; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; mt=np=&ci=43_1; _m_h5_tk=ba6cf2e64816a6388cbf7791ba54cd27_1516680322523; _m_h5_tk_enc=6b5ac3710bcaa6838991dc4a8dc759d1; cookie2=15c64bd8f687b2a4a3b971f45d200604; _tb_token_=58a03fece1638; v=0; uc3=sg2=WqIrBf2WEDhnXgIg9lOgUXQnkoTeDo019W%2BL27EjCfQ%3D&nk2=rUs9FkCy6Zs6Ew%3D%3D&id2=VWeZAHoeqUWF&vt3=F8dBzLlgyRO3h6jgHCM%3D&lg2=W5iHLLyFOGW7aA%3D%3D; existShop=MTUxNjg1MTIwMg%3D%3D; uss=VFCrGVQarc5fRZuloY2201S78KUXFfygvLSw2rpMzPv6IEZd6u0rtzHHOA%3D%3D; sg=%E6%A2%A657; cookie1=W8sivp9OeD7CvuVdh6i1LLRCZWfw5Of6GKWiySUCS9Q%3D; unb=688489285; skt=ea485d5d0965e812; _cc_=VFC%2FuZ9ajQ%3D%3D; _l_g_=Ug%3D%3D; _nk_=%5Cu6211%5Cu6210%5Cu4F60%5Cu5669%5Cu68A6; cookie17=VWeZAHoeqUWF; uc1=cookie16=UIHiLt3xCS3yM2h4eKHS9lpEOw%3D%3D&cookie21=VT5L2FSpczFp&cookie15=U%2BGCWk%2F75gdr5Q%3D%3D&existShop=true&pas=0&cookie14=UoTdfY33wa4kXA%3D%3D&cart_m=0&tag=8&lng=zh_CN; whl=-1%260%260%260; isg=BDAwbBKoHlq2RsJr1kTJeO3kAf5C0XGCCmwfACqBbAte5dCP0onkU4ZbOe-F9cyb",
    "referer": "https://detail.tmall.com/item.htm?spm=a1z0d.6639537.1997196601.15.7a770906Ceta8O&id=%s&skuId=3618163606209"%id,
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
}
requests_session = requests.Session()
html = requests_session.get(url, headers=headers).text
print html
