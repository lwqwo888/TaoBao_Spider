# coding=utf-8
import time
import requests
import urllib
from mtranslate import translate
from lxml import etree
import sys
reload(sys)
sys.setdefaultencoding('utf-8')



# print translate("การจัดหมวดหมู่สี: สีแดงเข้มคู่ปีกส่วนหมวกวรรคสีม่วงสีฟ้าคู่คู่คู่หมวกสีฟ้าปีกวรรควรรควรรคสีม่วงแดงหมวกสีเหลืองคู่คู่หมวกคู่ส่วนหมวกปีกวรรคสีแดงคู่สีน้ำเงินเข้มลายพรางชมพูความเหนื่อยล้าพรางสีแดงสีเหลืองสีฟ้าจุดสีดำ", "zh-CN", "auto")
t = time.time()
ts =  int(round(t * 1000))
# 1520060127631
# 1520061833644
# url = "https://qiang.taobao.com/category.htm?categoryId=320000".format(ts)
url = "https://unszacs.m.taobao.com/h5/mtop.msp.qianggou.queryitembycategoryid/3.0/?v=3.0&api=mtop.msp.qianggou.queryItemByCategoryId&appKey=12574478&t=1520070584202&callback=mtopjsonp2&type=jsonp&sign=be18171dee52388a8535c28deeec51e6&data=%7B%22categoryId%22%3A%22320000%22%2C%22offset%22%3A50%2C%22limit%22%3A50%7D"
headers = {
    # # "Accept":"*/*",
    # # "Accept-Encoding":"gzip, deflate, br",
    # # "Accept-Language":"zh-CN,zh;q=0.9",
    # # "Connection":"keep-alive",
    # "Host":"unszacs.m.taobao.com",
    # "Referer":"https://qiang.taobao.com/category.htm?categoryId=312000",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
}

res = requests.get(url=url, headers=headers).text
# print res
# html = etree.HTML(res)
# str = html.xpath("/html/body/div[2]/div[2]/div/div[1]/div/div[2]/a")
# print len(str)
# for i in str:
#     print i
