# coding=utf-8
import time
import requests
import sys
reload(sys)
# 设置编码格式，python2默认是ascii码，python3默认utf-8
sys.setdefaultencoding("utf-8")


NETWORK_STATUS = True # 判断状态变量
url = 'https://cloud.video.taobao.com/play/u/645039969/p/1/e/6/t/1/50035884952.mp4'
headers = {"User-Agent": "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0 )"}

def run():
    proxies = {
        "http": '61.132.93.14:6441',
        "https": '61.132.93.14:6441',
    }
    try:
        response = requests.get(url, timeout=2, proxies=proxies)
        if response.status_code == 200:
            print (response.content)

    except Exception as e:
        # # global NETWORK_STATUS
        NETWORK_STATUS = False # 请求超时改变状态
        #
        if NETWORK_STATUS == False:
        #     '请求超时'
            for i in range(1,5):
                print '请求超时，第%s次重复请求'% i
                try:
                    response = requests.get(url, timeout=6, headers=headers, proxies=proxies)
                    if response.status_code == 200:
                        print (response.headers)
                        break
                except:
                    print (i)
                    continue

            with open('request.log', 'a') as f:
                f.write('%s 请求失败 - %s\n' % (url, time.ctime()))
            print ('[INFO]:重发请求失败!!!!!!!!!!')

if __name__=="__main__":
    run()