# coding=utf-8
import urllib2
import cookielib
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

url = 'https://login.taobao.com/'
params = {
    'TPL_username': '我成你噩梦',
    'TPL_password_2': '5af25f13704a7288bb6436d7eb1832db238d67cc13c760b0ffa1f2587256168b79a6fef840b262c24cf069ee0265c1e01564e19b5a5e39b5daf1b4241bd667b2843a578c91673f543485f826943aeac266a15ff9c58f8cf3f7998d44b4038927dea10ae7f4e58c6460e6e15e5e8b87c43ceb2ec9f3e813da51fc8f154d590c25'
}
headers = {
    'origin': 'https://login.taobao.com',
    'content-type': 'application/x-www-form-urlencoded',
    'Connection': 'keep-alive',
    # "cookie": "cna=5w2/EagEn1sCAbcnVm41KZrQ; x=__ll%3D-1%26_ato%3D0; hng=CN%7Czh-CN%7CCNY%7C156; uc1=cookie14=UoTdfkKtks6l8w%3D%3D&lng=zh_CN&cookie16=UtASsssmPlP%2Ff1IHDsDaPRu%2BPw%3D%3D&existShop=true&cookie21=URm48syIYn73&tag=8&cookie15=W5iHLLyFOGW7aA%3D%3D&pas=0; uc3=sg2=WqIrBf2WEDhnXgIg9lOgUXQnkoTeDo019W%2BL27EjCfQ%3D&nk2=rUs9FkCy6Zs6Ew%3D%3D&id2=VWeZAHoeqUWF&vt3=F8dBzLgrpMV1BvHSmJg%3D&lg2=VFC%2FuZ9ayeYq2g%3D%3D; tracknick=%5Cu6211%5Cu6210%5Cu4F60%5Cu5669%5Cu68A6; _l_g_=Ug%3D%3D; unb=688489285; lgc=%5Cu6211%5Cu6210%5Cu4F60%5Cu5669%5Cu68A6; cookie1=W8sivp9OeD7CvuVdh6i1LLRCZWfw5Of6GKWiySUCS9Q%3D; login=true; cookie17=VWeZAHoeqUWF; cookie2=38518becf2aaeff0e67d62c772aaf1da; _nk_=%5Cu6211%5Cu6210%5Cu4F60%5Cu5669%5Cu68A6; uss=V33DdgQCI1MgOSGAMSNlX2eByPhz9fYofocO29hW%2FrleKN2N%2FIEXsK64cQ%3D%3D; sg=%E6%A2%A657; t=41a78c0d4f8236cec127e49a3a1d7668; _tb_token_=30783b151de8b; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; whl=-1%260%260%260; isg=Ai8v8rAvqf2eaq7cDFBD2S0vvkP5fILyLP09vUG8yx6lkE-SSaQTRi1CZrZV",
    "referer": 'https://login.taobao.com/member/login.jhtml?',
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
}
html = requests.post(url, data=params, headers=headers).text
print html
