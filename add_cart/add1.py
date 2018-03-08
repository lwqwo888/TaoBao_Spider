# coding=utf-8
import sys
import requests
reload(sys)
sys.setdefaultencoding('utf-8')



id = '557200845972'
url = "https://cart.taobao.com/add_cart_item.htm?item_id=557200845972"
headers = {

    "method": "GET",
    'Connection': 'keep-alive',
    "cookie": "t=28edc35882e1fcf06bfaa67008da2a8f; cna=XTyQEoI1uE4CAXBfh3IMFSpJ; thw=cn; miid=6347655561018672771; lgc=%5Cu6211%5Cu6210%5Cu4F60%5Cu5669%5Cu68A6; tracknick=%5Cu6211%5Cu6210%5Cu4F60%5Cu5669%5Cu68A6; tg=0; enc=GtOY%2B8mhUi7LXIrV9LqmUl0PYsVpr9BbSzEB9GL%2Fq3i6Czwxxh5mE60CMJjep9GIq4iV04PvQsAGhzOIdrf6iw%3D%3D; UM_distinctid=160fe373fd7c89-0f04cad75d123e-393d5f0e-1fa400-160fe373fd8e5a; hng=CN%7Czh-CN%7CCNY%7C156; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; mt=np=&ci=43_1; _m_h5_tk=ba6cf2e64816a6388cbf7791ba54cd27_1516680322523; _m_h5_tk_enc=6b5ac3710bcaa6838991dc4a8dc759d1; cookie2=15c64bd8f687b2a4a3b971f45d200604; _tb_token_=58a03fece1638; v=0; uc3=sg2=WqIrBf2WEDhnXgIg9lOgUXQnkoTeDo019W%2BL27EjCfQ%3D&nk2=rUs9FkCy6Zs6Ew%3D%3D&id2=VWeZAHoeqUWF&vt3=F8dBzLlgyRO3h6jgHCM%3D&lg2=W5iHLLyFOGW7aA%3D%3D; existShop=MTUxNjg1MTIwMg%3D%3D; uss=VFCrGVQarc5fRZuloY2201S78KUXFfygvLSw2rpMzPv6IEZd6u0rtzHHOA%3D%3D; sg=%E6%A2%A657; cookie1=W8sivp9OeD7CvuVdh6i1LLRCZWfw5Of6GKWiySUCS9Q%3D; unb=688489285; skt=ea485d5d0965e812; _cc_=VFC%2FuZ9ajQ%3D%3D; _l_g_=Ug%3D%3D; _nk_=%5Cu6211%5Cu6210%5Cu4F60%5Cu5669%5Cu68A6; cookie17=VWeZAHoeqUWF; uc1=cookie16=UIHiLt3xCS3yM2h4eKHS9lpEOw%3D%3D&cookie21=VT5L2FSpczFp&cookie15=U%2BGCWk%2F75gdr5Q%3D%3D&existShop=true&pas=0&cookie14=UoTdfY33wa4kXA%3D%3D&cart_m=0&tag=8&lng=zh_CN; whl=-1%260%260%260; isg=BDAwbBKoHlq2RsJr1kTJeO3kAf5C0XGCCmwfACqBbAte5dCP0onkU4ZbOe-F9cyb",
    "referer": "https://detail.tmall.com/item.htm?spm=a230r.1.14.1.29b70e2cmQb92Y&id=%s&ns=1&abbucket=13" % id,
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",

}
res = requests.get(url, headers=headers).text
print res

