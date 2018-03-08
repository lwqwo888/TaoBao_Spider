# coding=utf-8
import re
import time
import requests
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def property_count(id):
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
    print html

    img_url_obj = re.compile(r'(//img.*?\.(jpg|png|SS2))', re.S)
    img_url_list = img_url_obj.findall(html)
    length = len(img_url_list)
    news_img_url_list = list(set(img_url_list))
    news_img_url_list.sort(key=img_url_list.index)
    # print length
    # print len(news_img_url_list)
    # for i in img_url_list:
    #     with open("taobao_img/img_url.txt", 'a') as f:
    #         f.write("http:" + i[0] + '\n')
    #         # print i[0]
    #         # print "http:" + i[0]
    # with open('taobao_img/img_url.txt', 'rb') as f:
    #     lines = f.readlines()
    #     # print '///////////////////////',len(lines)
    # # j = 0
    # # while j < length:
    # #     print lines[j]
    # #     j += 1
    # j = 0
    # # length = 1
    # while j < length:
    #     # print lines[j]
    #     url1 = lines[j].replace(' ', '').replace('\n', '').replace('\t', '').replace('r', '')
    #     # url1 = "http://img.alicdn.com/imgextra/i2/645039969/TB2SSGAXcrHK1Jjy1zdXXbTwXXa_!!645039969.jpg"
    #     res = requests.get(url1, headers=headers).content
    #     print url1
    #     print requests.get(url1, headers=headers).url
    #     print '\n'
    #     # print res
    #     format = url1[-5:]
    #     # print format
    #     name = "img" + str(j) + format
    #     with open("taobao_img/img/" + name, 'wb') as f:
    #         # print '******************',res
    #         f.write(res)
    #     time.sleep(1)
    #     j += 1
    # print len(img_url_list)


def url_process(url):
    res = re.compile(r'(\?|&)id=(\d+).*?', re.S)
    id = res.search(url).group(2)
    # print id
    return ''.join(id)



if __name__ == '__main__':
    url = "https://item.taobao.com/item.htm?spm=a219r.lmn002.14.174.6f516358W81jq9&id=562441235623&ns=1&abbucket=16"
    # url = 'https://item.taobao.com/item.htm?spm=a219r.lm874.14.31.5dc9e78e7Fcl7j&id=557200845972&ns=1&abbucket=16#detail'
    id = url_process(url)
    property_count(id)
