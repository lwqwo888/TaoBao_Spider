import requests

# url = 'https://cloud.video.taobao.com/play/u/108727117/p/1/e/6/t/1/50047688890.mp4'
# res = requests.get(url).content
# with open("shipin.mp4", 'wb') as f:
#     f.write(res)

url = "http://img.alicdn.com/bao/uploaded/i2/TB1R0ASh4PI8KJjSspfYXICFXXa_M2.SS2"
res = requests.get(url).content
with open("img.jpg", 'wb') as f:
    f.write(res)