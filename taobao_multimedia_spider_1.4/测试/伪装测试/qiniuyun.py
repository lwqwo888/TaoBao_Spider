# coding=utf-8
import time
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


headers = {
    "cookie": "ubn=p; ucn=unsz; t=28edc35882e1fcf06bfaa67008da2a8f; cna=XTyQEoI1uE4CAXBfh3IMFSpJ; thw=cn; miid=6347655561018672771; uc3=sg2=WqIrBf2WEDhnXgIg9lOgUXQnkoTeDo019W%2BL27EjCfQ%3D&nk2=rUs9FkCy6Zs6Ew%3D%3D&id2=VWeZAHoeqUWF&vt3=F8dBzLgoJIN4WC0X30I%3D&lg2=VFC%2FuZ9ayeYq2g%3D%3D; lgc=%5Cu6211%5Cu6210%5Cu4F60%5Cu5669%5Cu68A6; tracknick=%5Cu6211%5Cu6210%5Cu4F60%5Cu5669%5Cu68A6; _cc_=WqG3DMC9EA%3D%3D; tg=0; enc=GtOY%2B8mhUi7LXIrV9LqmUl0PYsVpr9BbSzEB9GL%2Fq3i6Czwxxh5mE60CMJjep9GIq4iV04PvQsAGhzOIdrf6iw%3D%3D; mt=ci=-1_0; UM_distinctid=160fe373fd7c89-0f04cad75d123e-393d5f0e-1fa400-160fe373fd8e5a; hng=CN%7Czh-CN%7CCNY%7C156; _m_h5_tk=081b6ec244bfd7ba155325c85a14056e_1516103738466; _m_h5_tk_enc=8531a9b39cfb4a076e45dfad1fba7525; cookie2=16e0f40738dc82c43c53992cb5a26ebb; _tb_token_=3daeebbb3768e; v=0; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; uc1=cookie14=UoTdfYT5TUo4kA%3D%3D; isg=BDo6USLQNOpL5rgFeJZzPiuWi2CcQ9uEDF5FrkQyJ02YN9lxLHiA1B8ng8PrpzZd",
    # "referer": "https://item.taobao.com/item.htm?spm=a219r.lmn002.14.174.6f516358W81jq9&id=561495525977&ns=1&abbucket=16",
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
}
# url = "https://t11img.yangkeduo.com/images/2018-02-28/90a4190a764cf19e0899ba01989da209.jpeg"
url = "https://img01.taobaocdn.com/imgextra/i1/414224286/TB2w65WaFXXXXcpXXXXXXXXXXXX-414224286.png"
# url = "http://dsc.taobaocdn.com/i8/550/150/557156122382/TB13lKSXSYTBKNjSZKb8qtJ8pla.desc%7Cvar%5Edesc%3Bsign%5Eb9b931bf2a0ad0b5a7d20095043315cc%3Blang%5Egbk%3Bt%5E1519630932"
proxies = {'https': 'http://16SBYYUY:658666@n10.t.16yun.cn:6442', 'http': 'http://16SBYYUY:658666@n10.t.16yun.cn:6442'}

def test(url,proxies,headers):
    srequest = requests.Session()
    i = 1
    total_s = time.time()
    ok_count = 0
    for i in range(20):
        name = 'taobao%s.jpg' % i
        print name
        res = srequest.get(url, headers=headers, proxies=proxies)
        print res.status_code
        if res.status_code == 200:
            ok_count += 1
    total_e = time.time()
    print total_e-total_s
    print ok_count / (total_e-total_s)

test(url,proxies,headers)