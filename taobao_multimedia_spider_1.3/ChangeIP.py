# coding=utf-8
import time


def change_ip():
    new_sec = time.time()
    sec = new_sec - old_sec
    if sec > 0.3:
        # # 要访问的目标页面
        # targetUrl = "http://httpbin.org/ip"

        # 代理服务器
        proxyHost = "n5.t.16yun.cn"
        proxyPort = "6441"

        # 代理隧道验证信息
        proxyUser = "username"
        proxyPass = "password"

        proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
            "host": proxyHost,
            "port": proxyPort,
            "user": proxyUser,
            "pass": proxyPass,
        }

        proxies = {
            "http": proxyMeta,
            "https": proxyMeta,
        }

        # tunnel = random.randint(1, 10000)
        # headers = {"Proxy-Tunnel": str(tunnel)}
        # resp = requests.get(targetUrl, proxies=proxies, headers=headers)
        self.proxy = proxies
    else:
        self.proxy = self.proxy
