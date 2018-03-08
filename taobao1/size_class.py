# coding=utf-8
import re
import requests
from lxml import etree
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def size_count(id):
    # id = '562441235623'
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
    # print html
    res = etree.HTML(html)
    ron = res.xpath('''//*[@id="J_DetailMeta"]/div[1]/div[1]/div/div[4]/div/div/dl[1]/dd/ul/li//span''')
    # 尺码数量
    size_count = len(ron)
    # print size_count
    # 偏移量
    list = []
    size_num = 1
    while size_num <= size_count:
        xpath_str = '''//*[@id="J_DetailMeta"]/div[1]/div[1]/div/div[4]/div/div/dl[1]/dd/ul/li[%s]//span/text()'''%str(size_num)
        size_num_list = res.xpath(xpath_str)

        for x in size_num_list:
            size = x.replace('\n', '').replace('\t', '').replace('\r', '').strip()
            # print size
            list.append(size)

        size_num += 1
        print list
    return list
