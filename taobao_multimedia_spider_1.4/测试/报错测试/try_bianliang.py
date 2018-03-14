# coding=utf-8
import time
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


# i = 0
# def f():
#     global i
#     i = 8
#     print i
# f()
# print i
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
}
proxy = {'http': 'http://16SBYYUY:658666@n10.t.16yun.cn:6442', 'https': 'http://16SBYYUY:658666@n10.t.16yun.cn:6442'}
url = "https://t11img.yangkeduo.com/images/2018-02-28/90a4190a764cf19e0899ba01989da209.jpeg"
# url = "http://img01.taobaocdn.com/imgextra/i1/414224286/TB2w65WaFXXXXcpXXXXXXXXXXXX-41422cvbcv4286.png"
# url = "https://item.taobao.com/item.htm?spm=a217f.8051907.312171.29.5dcd3308XI4dyi&id=559530770578"

srequests = requests.Session()
while True:
    try:
        i = 100
        res = requests.get(url, headers=headers, proxies=proxy)
        code = res.status_code
        print code, "-"*60
        # print res.text
        if code != 200:
            print "错误1", code

            j = 0
            while True:
                res = requests.get(url, headers=headers, proxies=proxy)
                code = res.status_code
                if code == 200:
                    break
                time.sleep(1)
                j += 1
                print "错误2", code

    except requests.ConnectionError as e:
        print 'erro', e

    print 6666

    # finally:
    #     code = res.status_code
    #     print code