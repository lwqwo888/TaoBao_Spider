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


try:
    i = 100
    url = "http://img01.taokbaocdn.com/imgextra/i1/414224286/TB2w65WaFXXXXcpXXXXXXXXXXXX-41422cvbcv4286.png"
    res = requests.get(url)
    code = res.status_code
    print code
    # print res.text
    if i == 200:
        print i

except Exception as e:
    print 'erro', e

# finally:
#     code = res.status_code
#     print code